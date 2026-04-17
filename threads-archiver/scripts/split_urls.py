#!/usr/bin/env python3
"""
split_urls.py
URL 목록 파일을 N개 청크 파일로 균등 분할한다.

사용법:
  python split_urls.py <url_file> --chunks <N> --output-dir <dir>

출력:
  - <output-dir>/chunk_01.txt, chunk_02.txt, ... (각 청크 파일)
  - stdout: 생성된 청크 파일 경로 (한 줄에 하나)
"""

import sys
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='URL 목록 파일을 N개 청크로 분할')
    parser.add_argument('url_file', help='분할할 URL 목록 파일')
    parser.add_argument('--chunks', type=int, required=True, help='분할할 청크 수')
    parser.add_argument('--output-dir', required=True, help='청크 파일을 저장할 디렉토리')
    args = parser.parse_args()

    url_file = Path(args.url_file)
    if not url_file.exists():
        print(f'오류: 파일을 찾을 수 없습니다: {url_file}', file=sys.stderr)
        sys.exit(1)

    urls = [
        line.strip()
        for line in url_file.read_text(encoding='utf-8').splitlines()
        if line.strip() and not line.strip().startswith('#')
    ]

    if not urls:
        print('오류: URL이 없습니다.', file=sys.stderr)
        sys.exit(1)

    n_chunks = min(args.chunks, len(urls))  # URL 수보다 청크 수가 많으면 안 됨
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 균등 분할 (앞 청크가 1개 더 가질 수 있음)
    base_size, remainder = divmod(len(urls), n_chunks)
    chunks = []
    start = 0
    for i in range(n_chunks):
        size = base_size + (1 if i < remainder else 0)
        chunks.append(urls[start:start + size])
        start += size

    print(f'[분할] 총 {len(urls)}개 URL → {n_chunks}개 청크', file=sys.stderr)

    chunk_files = []
    for i, chunk in enumerate(chunks, 1):
        chunk_file = output_dir / f'chunk_{i:02d}.txt'
        chunk_file.write_text('\n'.join(chunk), encoding='utf-8')
        print(f'  chunk_{i:02d}.txt: {len(chunk)}개 URL', file=sys.stderr)
        chunk_files.append(str(chunk_file))

    # stdout에 청크 파일 경로 출력
    for f in chunk_files:
        print(f)


if __name__ == '__main__':
    main()
