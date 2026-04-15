#!/usr/bin/env python3
"""
Threads Archiver - fetch_threads.py
Threads.com 포스트 URL에서 시리즈 포스트 전체를 수집하여 Obsidian MD 파일로 저장
"""

import sys
import re
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path


# ─────────────────────────────────────────────
# 날짜 유틸리티
# ─────────────────────────────────────────────

def parse_relative_date(date_str: str, today: datetime) -> str:
    """한국어/영어 상대 날짜 문자열을 YYYY-MM-DD 형식으로 변환"""
    date_str = date_str.strip()
    num_match = re.search(r'(\d+)', date_str)
    num = int(num_match.group(1)) if num_match else 1

    if '일' in date_str and '월' not in date_str:
        result = today - timedelta(days=num)
    elif '주' in date_str:
        result = today - timedelta(weeks=num)
    elif '달' in date_str or '개월' in date_str:
        result = today - timedelta(days=num * 30)
    elif '년' in date_str:
        result = today - timedelta(days=num * 365)
    elif '시간' in date_str or '분' in date_str or '초' in date_str:
        result = today
    elif date_str.endswith('d') or 'day' in date_str:
        result = today - timedelta(days=num)
    elif date_str.endswith('w') or 'week' in date_str:
        result = today - timedelta(weeks=num)
    elif date_str.endswith('h') or 'hour' in date_str:
        result = today
    elif date_str.endswith('m') or 'min' in date_str:
        result = today
    else:
        for fmt in ('%Y년 %m월 %d일', '%Y-%m-%d', '%B %d, %Y', '%b %d, %Y'):
            try:
                return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
            except ValueError:
                continue
        result = today

    return result.strftime('%Y-%m-%d')


# ─────────────────────────────────────────────
# 시리즈 감지
# ─────────────────────────────────────────────

def detect_series(text: str):
    """텍스트 끝부분에서 'X/N' 패턴 감지. (current, total) 또는 (None, None)"""
    match = re.search(r'(\d+)\s*/\s*(\d+)\s*$', text.strip())
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None


def get_first_sentence(text: str) -> str:
    """첫 문장 추출 (시리즈 마커 제거)"""
    text = re.sub(r'\s*\d+\s*/\s*\d+\s*$', '', text.strip())
    first_line = text.split('\n')[0].strip()
    sentence_match = re.match(r'^(.+?[.!?。！？])', first_line)
    if sentence_match:
        return sentence_match.group(1).strip()
    return first_line[:80].strip() if len(first_line) > 80 else first_line


# ─────────────────────────────────────────────
# 포스트 데이터 추출
# ─────────────────────────────────────────────

def extract_best_image_url(image_versions2: dict) -> str:
    """image_versions2 객체에서 가장 좋은 해상도의 이미지 URL 반환"""
    if not isinstance(image_versions2, dict):
        return ''
    candidates = image_versions2.get('candidates', [])
    if not candidates:
        return ''
    # 해상도가 가장 높은 것 선택 (width 기준)
    best = max(candidates, key=lambda c: c.get('width', 0) if isinstance(c, dict) else 0)
    return best.get('url', '') if isinstance(best, dict) else ''


def extract_post_data(post: dict) -> dict:
    """포스트 dict에서 필요 필드 추출"""
    if not isinstance(post, dict):
        return {}

    author = post.get('user', {}).get('username', '') if isinstance(post.get('user'), dict) else ''
    taken_at = post.get('taken_at', 0)
    date_str = datetime.fromtimestamp(taken_at).strftime('%Y-%m-%d') if taken_at else ''

    # 텍스트
    caption = post.get('caption') or {}
    text = caption.get('text', '') if isinstance(caption, dict) else str(caption) if caption else ''

    # 이미지 URL 수집
    image_urls = []

    # 단일 이미지 (image_versions2)
    img_v2 = post.get('image_versions2') or {}
    single_img = extract_best_image_url(img_v2)
    if single_img:
        image_urls.append(single_img)

    # 카루셀 (carousel_media) - 여러 장 이미지
    carousel = post.get('carousel_media') or []
    if carousel:
        image_urls.clear()  # 카루셀이 있으면 카루셀 이미지로 교체
        for item in carousel:
            if isinstance(item, dict):
                url = extract_best_image_url(item.get('image_versions2') or {})
                if url:
                    image_urls.append(url)

    # 동영상 URL - video_url 또는 video_versions (해상도 리스트)
    video_urls = []
    vid = post.get('video_url', '')
    if vid:
        video_urls.append(vid)
    if not video_urls:
        vid_versions = post.get('video_versions') or []
        if vid_versions:
            # 첫 번째(보통 최고화질) 사용
            v = vid_versions[0].get('url', '') if isinstance(vid_versions[0], dict) else ''
            if v:
                video_urls.append(v)
    # 카루셀 내 동영상
    for item in (carousel or []):
        if isinstance(item, dict):
            v = item.get('video_url', '') or ''
            if not v:
                vv = item.get('video_versions') or []
                v = vv[0].get('url', '') if vv and isinstance(vv[0], dict) else ''
            if v and v not in video_urls:
                video_urls.append(v)

    if not author and not text:
        return {}

    return {
        'author': author,
        'text': text,
        'image_urls': [u for u in image_urls if u],
        'video_urls': [u for u in video_urls if u],
        'date_str': date_str,
        'taken_at': taken_at,
    }


# ─────────────────────────────────────────────
# JSON 구조 탐색
# ─────────────────────────────────────────────

def find_all_values(obj, key: str, depth=0, max_depth=20):
    """JSON 전체에서 특정 key를 가진 값 모두 수집"""
    if depth > max_depth:
        return []
    results = []
    if isinstance(obj, dict):
        if key in obj:
            results.append(obj[key])
        for v in obj.values():
            results.extend(find_all_values(v, key, depth + 1, max_depth))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(find_all_values(item, key, depth + 1, max_depth))
    return results


def extract_posts_from_thread_items_list(thread_items: list, target_author: str) -> list[dict]:
    """thread_items 배열에서 target_author의 포스트만 추출"""
    posts = []
    for item in (thread_items or []):
        if not isinstance(item, dict) or 'post' not in item:
            continue
        data = extract_post_data(item['post'])
        if not data:
            continue
        if target_author and data.get('author', '').lower() != target_author.lower():
            continue
        posts.append(data)
    return posts


def extract_posts_from_edges(edges: list, target_author: str) -> list[dict]:
    """
    data.data.edges 구조에서 target_author의 시리즈 포스트 추출.
    각 edge의 node.thread_items를 순서대로 처리.
    """
    all_posts = []
    for edge in (edges or []):
        node = edge.get('node', {}) if isinstance(edge, dict) else {}
        thread_items = node.get('thread_items', []) if isinstance(node, dict) else []
        posts = extract_posts_from_thread_items_list(thread_items, target_author)
        all_posts.extend(posts)
    return all_posts


def extract_posts_from_page(page, target_author: str) -> list[dict]:
    """Playwright page에서 포스트 추출. 두 가지 경로를 시도."""
    all_posts = []

    scripts = page.query_selector_all('script[type="application/json"]')

    for s in scripts:
        txt = s.inner_text() or ''
        # target_author가 없거나 텍스트에 포함된 script만 처리
        if target_author and target_author not in txt:
            continue
        if 'taken_at' not in txt:
            continue

        try:
            data = json.loads(txt)
        except (json.JSONDecodeError, Exception):
            continue

        # 방법 1: data.data.edges 구조 (주 스레드 포스트)
        edges_lists = find_all_values(data, 'edges')
        for edges in edges_lists:
            if not isinstance(edges, list) or not edges:
                continue
            # node.thread_items 구조 확인
            first = edges[0] if edges else {}
            if isinstance(first, dict) and 'node' in first:
                node = first['node']
                if isinstance(node, dict) and 'thread_items' in node:
                    posts = extract_posts_from_edges(edges, target_author)
                    all_posts.extend(posts)

        # 방법 2: relatedPosts.threads 구조 (관련 포스트 - 보통 스킵)
        # 이건 다른 유저 포스트이므로 제외

    return all_posts


# ─────────────────────────────────────────────
# 마크다운 생성
# ─────────────────────────────────────────────

def build_markdown(posts: list[dict], url: str, author: str, today: datetime) -> str:
    """포스트 목록으로 Obsidian 최적화 Markdown 문서 생성"""

    if not posts:
        return ''

    # taken_at 기준 정렬
    posts_sorted = sorted(posts, key=lambda p: p.get('taken_at', 0))

    first_post = posts_sorted[0]
    first_text = first_post.get('text', '')

    # 날짜
    date_str = first_post.get('date_str', '')
    if not date_str:
        date_str = today.strftime('%Y-%m-%d')

    # 제목
    title = get_first_sentence(first_text) or f'@{author} 스레드'

    # 시리즈 정보
    _, total = detect_series(first_text)
    total_posts = total if total else len(posts_sorted)

    # YAML frontmatter
    yaml_lines = [
        '---',
        f'thread_url: "{url}"',
        f'author: "@{author}"',
        f'date: "{date_str}"',
        f'total_posts: {total_posts}',
        'tags:',
        '  - threads',
        '  - archive',
        '---',
        '',
    ]

    body_lines = [f'# {title}', '']

    for i, post in enumerate(posts_sorted, 1):
        text = post.get('text', '')
        images = post.get('image_urls', [])
        videos = post.get('video_urls', [])

        current, total_n = detect_series(text)
        if current is not None and total_n is not None:
            section_title = f'## {current}/{total_n}'
            clean_text = re.sub(r'\s*\d+\s*/\s*\d+\s*$', '', text.strip())
        else:
            section_title = f'## {i}'
            clean_text = text.strip()

        body_lines.append(section_title)
        body_lines.append('')

        if clean_text:
            body_lines.append(clean_text)
            body_lines.append('')

        for img_url in images:
            body_lines.append(f'![]({img_url})')
            body_lines.append('')

        for vid_url in videos:
            body_lines.append(f'[동영상 보기]({vid_url})')
            body_lines.append('')

        body_lines.append('---')
        body_lines.append('')

    return '\n'.join(yaml_lines + body_lines)


# ─────────────────────────────────────────────
# 메인
# ─────────────────────────────────────────────

def extract_username_from_url(url: str) -> str:
    match = re.search(r'threads\.(?:com|net)/@([^/]+)', url)
    return match.group(1) if match else 'unknown'


def main():
    parser = argparse.ArgumentParser(
        description='Threads.com 포스트를 Obsidian Markdown 파일로 저장'
    )
    parser.add_argument('url', help='Threads 포스트 URL')
    parser.add_argument('--output', '-o', default='.', help='저장 디렉토리 (기본: 현재 디렉토리)')
    parser.add_argument('--timeout', type=int, default=30000, help='페이지 로드 타임아웃 ms (기본: 30000)')
    args = parser.parse_args()

    url = args.url
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now()

    author = extract_username_from_url(url)

    print(f'[1/4] Playwright 브라우저 시작...', flush=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print('오류: playwright가 설치되지 않았습니다.', file=sys.stderr)
        print('설치: pip install playwright && playwright install chromium', file=sys.stderr)
        sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/120.0.0.0 Safari/537.36'
            ),
            locale='ko-KR',
        )
        page = context.new_page()

        print(f'[2/4] 페이지 로드 중: {url}', flush=True)

        try:
            page.goto(url, wait_until='networkidle', timeout=args.timeout)
        except Exception:
            try:
                page.goto(url, wait_until='domcontentloaded', timeout=args.timeout)
                page.wait_for_timeout(5000)
            except Exception as e:
                print(f'오류: 페이지 로드 실패 - {e}', file=sys.stderr)
                browser.close()
                sys.exit(1)

        print('[3/4] 포스트 데이터 추출 중...', flush=True)
        posts = extract_posts_from_page(page, author)

        browser.close()

    if not posts:
        print(f'경고: @{author} 포스트를 찾지 못했습니다.', file=sys.stderr)
        print('페이지 구조가 변경되었거나 비공개 계정일 수 있습니다.', file=sys.stderr)
        sys.exit(1)

    # 중복 제거 (동일 taken_at)
    seen = set()
    unique_posts = []
    for post in posts:
        key = post.get('taken_at', 0)
        if key and key not in seen:
            seen.add(key)
            unique_posts.append(post)
        elif not key:
            unique_posts.append(post)
    posts = unique_posts

    print(f'[4/4] Markdown 생성 중... (포스트 {len(posts)}개)', flush=True)

    md_content = build_markdown(posts, url, author, today)

    if not md_content:
        print('오류: Markdown 생성에 실패했습니다.', file=sys.stderr)
        sys.exit(1)

    posts_sorted_for_name = sorted(posts, key=lambda p: p.get('taken_at', 0))
    first_text_for_name = posts_sorted_for_name[0].get('text', '') if posts_sorted_for_name else ''
    title_for_name = get_first_sentence(first_text_for_name) or f'@{author}_스레드'
    filename = f'{title_for_name}.md'
    filename = re.sub(r'[<>:"/\\|?*\n\r\t]', '_', filename)
    output_path = output_dir / filename

    output_path.write_text(md_content, encoding='utf-8')

    print(f'\n[완료] 저장: {output_path}')
    print(f'   - 작성자: @{author}')
    print(f'   - 포스트 수: {len(posts)}')
    total_images = sum(len(p.get('image_urls', [])) for p in posts)
    total_videos = sum(len(p.get('video_urls', [])) for p in posts)
    print(f'   - 이미지: {total_images}개, 동영상: {total_videos}개')


if __name__ == '__main__':
    main()
