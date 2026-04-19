#!/usr/bin/env python3
"""
bulk_download.py
URL 목록에서 각 포스트를 병렬로 다운로드한다.

사용법:
  python bulk_download.py <url1> [url2 ...] --output <저장할_경로> [--workers N]
  python bulk_download.py --file <url_list.txt> --output <저장할_경로> [--workers N]

중복 방지:
  출력 폴더에 _collected.log 파일을 유지한다.
  이미 수집된 URL은 건너뛰며, 성공 시 URL·수집일시·파일명을 기록한다.
  파일을 이동·이름 변경해도 로그가 남아 중복 수집을 막는다.
"""

import sys
import subprocess
import argparse
import os
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

print_lock = threading.Lock()
log_lock = threading.Lock()


def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, flush=True, **kwargs)


def load_collected_log(log_path: Path) -> set:
    """_collected.log에서 이미 수집된 URL 집합을 반환"""
    if not log_path.exists():
        return set()
    collected = set()
    for line in log_path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            url = line.split('\t')[0]
            if url.startswith('http'):
                collected.add(url)
    return collected


def append_collected_log(log_path: Path, url: str, filename: str):
    """성공한 URL을 _collected.log에 추가"""
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    entry = f'{url}\t{timestamp}\t{filename}\n'
    with log_lock:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(entry)


def download_one(args_tuple):
    idx, total, url, output_dir, timeout, fetch_script, translate, log_path = args_tuple
    safe_print(f'[{idx}/{total}] 시작: {url}')
    try:
        cmd = [sys.executable, str(fetch_script), url, '--output', str(output_dir), '--timeout', str(timeout)]
        if translate:
            cmd += ['--translate', translate]
        result = subprocess.run(
            cmd,
            capture_output=True,
            encoding='utf-8',
            errors='replace',
            timeout=180,
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
        )
        stdout = result.stdout or ''
        stderr = result.stderr or ''
        # 저장된 파일명 추출
        saved_line = next((l for l in stdout.splitlines() if '[완료] 저장:' in l), '')
        if result.returncode == 0:
            safe_print(f'  ✓ [{idx}/{total}] {saved_line.strip() or "저장 완료"}')
            # 파일명 파싱 및 로그 기록
            filename = ''
            if saved_line:
                parts = saved_line.strip().split('[완료] 저장:')
                if len(parts) > 1:
                    filename = parts[1].strip().rsplit('/', 1)[-1].rsplit('\\', 1)[-1]
            append_collected_log(log_path, url, filename)
            return url, True, None
        else:
            combined = (stderr or stdout).strip().splitlines()
            err = combined[-1] if combined else '알 수 없는 오류'
            safe_print(f'  ✗ [{idx}/{total}] 실패: {url}')
            safe_print(f'      오류: {err}')
            return url, False, err
    except subprocess.TimeoutExpired:
        safe_print(f'  ✗ [{idx}/{total}] 타임아웃: {url}')
        return url, False, 'timeout'
    except Exception as e:
        safe_print(f'  ✗ [{idx}/{total}] 오류: {url} — {e}')
        return url, False, str(e)


def main():
    parser = argparse.ArgumentParser(description='Threads 포스트 병렬 일괄 다운로드')
    parser.add_argument('urls', nargs='*', help='다운로드할 Threads URL 목록')
    parser.add_argument('--file', '-f', help='URL 목록 파일 (한 줄에 하나)')
    parser.add_argument('--output', required=True, help='저장할 디렉토리 경로')
    parser.add_argument('--timeout', type=int, default=60000, help='페이지 로드 타임아웃(ms, 기본: 60000)')
    parser.add_argument('--workers', type=int, default=3, help='병렬 워커 수 (기본: 3)')
    parser.add_argument('--translate', metavar='LANG', default='',
                        help='번역할 언어 코드 (예: ko). fetch_threads.py에 그대로 전달됨')
    parser.add_argument('--no-dedup', action='store_true',
                        help='중복 체크 건너뜀 (_collected.log 무시)')
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 수집 로그 경로
    log_path = output_dir / '_collected.log'
    if not log_path.exists():
        log_path.write_text(
            '# Threads Archiver - Collected URLs Log\n'
            '# Format: url<TAB>collected_at<TAB>filename\n',
            encoding='utf-8'
        )

    # URL 수집
    urls = list(args.urls) if args.urls else []
    if args.file:
        fpath = Path(args.file)
        if fpath.exists():
            for line in fpath.read_text(encoding='utf-8').splitlines():
                line = line.strip()
                if line and not line.startswith('#') and line.startswith('http'):
                    urls.append(line)

    # 중복 제거 (순서 유지)
    seen = set()
    unique_urls = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique_urls.append(u)
    urls = unique_urls

    if not urls:
        print('오류: 다운로드할 URL이 없습니다.')
        sys.exit(1)

    # 이미 수집된 URL 필터링
    skipped_count = 0
    if not args.no_dedup:
        collected = load_collected_log(log_path)
        if collected:
            filtered = [u for u in urls if u not in collected]
            skipped_count = len(urls) - len(filtered)
            urls = filtered

    script_dir = Path(__file__).parent
    fetch_script = script_dir / 'fetch_threads.py'

    if skipped_count:
        print(f'[중복 건너뜀] {skipped_count}개 URL은 이미 수집됨 (_collected.log 참조)')

    if not urls:
        print('[완료] 새로 수집할 URL이 없습니다. 모두 이미 수집된 항목입니다.')
        return

    workers = min(args.workers, len(urls))
    print(f'[시작] 총 {len(urls)}개 URL, 병렬 워커: {workers}개')
    print(f'[저장 경로] {output_dir}')
    print()

    tasks = [
        (i + 1, len(urls), url, output_dir, args.timeout, fetch_script, args.translate, log_path)
        for i, url in enumerate(urls)
    ]

    success_count = 0
    failed_urls = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(download_one, t): t for t in tasks}
        for future in as_completed(futures):
            url, ok, err = future.result()
            if ok:
                success_count += 1
            else:
                failed_urls.append((url, err))

    print()
    print('=' * 55)
    print(f'[완료] 성공: {success_count}개 / 전체: {len(urls)}개')
    if skipped_count:
        print(f'[건너뜀] 기수집: {skipped_count}개')
    if failed_urls:
        print(f'[실패] {len(failed_urls)}개:')
        for u, e in failed_urls:
            print(f'  - {u}  ({e})')
        fail_file = output_dir / '_failed_urls.txt'
        fail_file.write_text('\n'.join(u for u, _ in failed_urls), encoding='utf-8')
        print(f'  → 실패 목록 저장: {fail_file}')
    else:
        print('  모든 URL 다운로드 성공!')


if __name__ == '__main__':
    main()
