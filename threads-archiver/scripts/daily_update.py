#!/usr/bin/env python3
"""
daily_update.py
accounts.md에 등록된 모든 계정의 새 포스트를 수집한다.
Windows 작업 스케줄러 등으로 매일 자동 실행하도록 설계되었다.

사용법:
  python daily_update.py
  python daily_update.py --dry-run   # 실제 수집 없이 계획만 출력
"""

import sys
import subprocess
import argparse
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
SCRIPTS_DIR = SKILL_DIR / 'scripts'
ACCOUNTS_MD = SKILL_DIR / 'references' / 'accounts.md'
LOG_FILE = SKILL_DIR / 'logs' / f'daily_update_{datetime.now().strftime("%Y%m%d")}.log'

MAX_SCROLLS = 30   # 업데이트 수집은 최근 포스트만 확인
WORKERS = 3


def log(msg: str, also_print=True):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{timestamp}] {msg}'
    if also_print:
        print(line, flush=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def parse_accounts(md_path: Path) -> list[dict]:
    """accounts.md 테이블에서 계정 목록 파싱"""
    accounts = []
    in_table = False
    for line in md_path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line.startswith('| @') or (line.startswith('|') and '@' in line and 'threads.com' in line):
            cells = [c.strip() for c in line.strip('|').split('|')]
            if len(cells) >= 4:
                account = cells[0].lstrip('@')
                profile_url = cells[1]
                output_path = cells[2]
                last_date = cells[3]
                translate = cells[4] if len(cells) > 4 else '-'
                # 템플릿/예시 행 건너뜀
                if not account or not profile_url.startswith('http'):
                    continue
                if not re.match(r'\d{4}-\d{2}-\d{2}', last_date):
                    continue
                accounts.append({
                    'account': account,
                    'profile_url': profile_url,
                    'output_path': output_path,
                    'last_date': last_date,
                    'translate': translate.strip() if translate.strip() != '-' else '',
                })
    return accounts


def update_last_date(md_path: Path, account: str, new_date: str):
    """accounts.md의 마지막 수집일 업데이트"""
    content = md_path.read_text(encoding='utf-8')
    # @account 로 시작하는 행의 날짜 필드 업데이트
    pattern = rf'(\|\s*@{re.escape(account)}\s*\|[^|]+\|[^|]+\|)\s*[\d]{{4}}-[\d]{{2}}-[\d]{{2}}\s*(\|)'
    new_content = re.sub(pattern, rf'\g<1> {new_date} \g<2>', content)
    if new_content != content:
        md_path.write_text(new_content, encoding='utf-8')


def fetch_urls(profile_url: str, start_date: str) -> list[str]:
    """fetch_profile_urls.py 실행 → URL 목록 반환"""
    cmd = [
        sys.executable,
        str(SCRIPTS_DIR / 'fetch_profile_urls.py'),
        profile_url,
        '--start-date', start_date,
        '--max-scrolls', str(MAX_SCROLLS),
    ]
    result = subprocess.run(
        cmd,
        capture_output=True,
        encoding='utf-8',
        errors='replace',
        timeout=300,
        env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
        cwd=str(SKILL_DIR),
    )
    urls = [
        line.strip()
        for line in (result.stdout or '').splitlines()
        if line.strip().startswith('https://www.threads.com/')
    ]
    return urls


def bulk_download(urls: list[str], output_path: str, translate: str) -> tuple[int, int]:
    """bulk_download.py 실행 → (성공수, 실패수) 반환"""
    if not urls:
        return 0, 0

    # URL을 임시 파일에 저장
    tmp_file = SKILL_DIR / 'tmp' / f'urls_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    tmp_file.parent.mkdir(parents=True, exist_ok=True)
    tmp_file.write_text('\n'.join(urls), encoding='utf-8')

    cmd = [
        sys.executable,
        str(SCRIPTS_DIR / 'bulk_download.py'),
        '--file', str(tmp_file),
        '--output', output_path,
        '--workers', str(WORKERS),
    ]
    if translate:
        cmd += ['--translate', translate]

    result = subprocess.run(
        cmd,
        capture_output=True,
        encoding='utf-8',
        errors='replace',
        timeout=3600,
        env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
        cwd=str(SKILL_DIR),
    )

    # 결과 파싱
    output = result.stdout or ''
    success = 0
    failed = 0
    for line in output.splitlines():
        m = re.search(r'성공:\s*(\d+)개\s*/\s*전체:\s*(\d+)개', line)
        if m:
            success = int(m.group(1))
            total = int(m.group(2))
            failed = total - success
            break

    tmp_file.unlink(missing_ok=True)
    return success, failed


def main():
    parser = argparse.ArgumentParser(description='Threads 계정 일일 업데이트 수집')
    parser.add_argument('--dry-run', action='store_true', help='실제 수집 없이 계획만 출력')
    args = parser.parse_args()

    today = datetime.now().strftime('%Y-%m-%d')
    log(f'=== 일일 업데이트 시작: {today} ===')

    if not ACCOUNTS_MD.exists():
        log(f'오류: accounts.md 없음: {ACCOUNTS_MD}')
        sys.exit(1)

    accounts = parse_accounts(ACCOUNTS_MD)
    if not accounts:
        log('오류: 등록된 계정이 없습니다.')
        sys.exit(1)

    log(f'등록된 계정: {len(accounts)}개')

    total_success = 0
    total_failed = 0

    for acc in accounts:
        account = acc['account']
        profile_url = acc['profile_url']
        output_path = acc['output_path']
        last_date = acc['last_date']
        translate = acc['translate']

        # start_date = 마지막 수집일 + 1일
        try:
            last_dt = datetime.strptime(last_date, '%Y-%m-%d')
            start_date = (last_dt + timedelta(days=1)).strftime('%Y-%m-%d')
        except ValueError:
            start_date = today

        # 오늘 이후면 건너뜀
        if start_date > today:
            log(f'[@{account}] 건너뜀 (마지막 수집일: {last_date}, 새 포스트 없음)')
            continue

        log(f'[@{account}] 수집 시작: {start_date} ~ {today}, 저장: {output_path}')

        if args.dry_run:
            log(f'  [DRY RUN] fetch_profile_urls.py {profile_url} --start-date {start_date}')
            log(f'  [DRY RUN] bulk_download.py --output {output_path} --translate {translate or "없음"}')
            continue

        # URL 수집
        try:
            urls = fetch_urls(profile_url, start_date)
        except Exception as e:
            log(f'  오류: URL 수집 실패 — {e}')
            total_failed += 1
            continue

        log(f'  수집된 URL: {len(urls)}개')

        if not urls:
            log(f'  새 포스트 없음')
            update_last_date(ACCOUNTS_MD, account, today)
            continue

        # 다운로드
        try:
            success, failed = bulk_download(urls, output_path, translate)
        except Exception as e:
            log(f'  오류: 다운로드 실패 — {e}')
            total_failed += len(urls)
            continue

        log(f'  완료: 성공 {success}개, 실패 {failed}개')
        total_success += success
        total_failed += failed

        # accounts.md 마지막 수집일 업데이트
        update_last_date(ACCOUNTS_MD, account, today)
        # D드라이브 스킬과 동기화된 C드라이브 경로도 업데이트
        c_accounts = Path('C:/Users/for30/.claude/skills/threads-archiver/references/accounts.md')
        if c_accounts.exists():
            update_last_date(c_accounts, account, today)

    log(f'=== 완료: 전체 성공 {total_success}개, 실패 {total_failed}개 ===')


if __name__ == '__main__':
    main()
