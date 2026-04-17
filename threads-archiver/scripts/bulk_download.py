#!/usr/bin/env python3
"""
bulk_download.py
URL 목록에서 각 포스트를 병렬로 다운로드한다.

사용법:
  python bulk_download.py <url1> [url2 ...] --output <저장할_경로> [--workers N]
  python bulk_download.py --file <url_list.txt> --output <저장할_경로> [--workers N]
"""

import sys
import subprocess
import argparse
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

print_lock = threading.Lock()


def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, flush=True, **kwargs)


def download_one(args_tuple):
    idx, total, url, output_dir, timeout, fetch_script = args_tuple
    safe_print(f'[{idx}/{total}] 시작: {url}')
    try:
        result = subprocess.run(
            [sys.executable, str(fetch_script), url, '--output', str(output_dir), '--timeout', str(timeout)],
            capture_output=True,
            encoding='utf-8',
            errors='replace',
            timeout=120,
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
        )
        stdout = result.stdout or ''
        stderr = result.stderr or ''
        # 저장된 파일명 추출
        saved_line = next((l for l in stdout.splitlines() if '[완료] 저장:' in l), '')
        if result.returncode == 0:
            safe_print(f'  ✓ [{idx}/{total}] {saved_line.strip() or "저장 완료"}')
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
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

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

    script_dir = Path(__file__).parent
    fetch_script = script_dir / 'fetch_threads.py'

    workers = min(args.workers, len(urls))
    print(f'[시작] 총 {len(urls)}개 URL, 병렬 워커: {workers}개')
    print(f'[저장 경로] {output_dir}')
    print()

    tasks = [
        (i + 1, len(urls), url, output_dir, args.timeout, fetch_script)
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
    if failed_urls:
        print(f'[실패] {len(failed_urls)}개:')
        for u, e in failed_urls:
            print(f'  - {u}  ({e})')
        # 실패 URL 파일로도 저장
        fail_file = output_dir / '_failed_urls.txt'
        fail_file.write_text('\n'.join(u for u, _ in failed_urls), encoding='utf-8')
        print(f'  → 실패 목록 저장: {fail_file}')
    else:
        print('  모든 URL 다운로드 성공!')


if __name__ == '__main__':
    main()
