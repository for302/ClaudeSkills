#!/usr/bin/env python3
"""
fetch_profile_urls.py
Threads.com 프로필 페이지를 크롤링하여 날짜 범위 내 포스트 URL을 수집한다.

사용법:
  python fetch_profile_urls.py https://www.threads.com/@specal1849 --start-date 2026-01-01
  python fetch_profile_urls.py https://www.threads.com/@specal1849 --start-date 2026-01-01 --end-post DVhRSueEtZn

출력:
  - URL 목록 (stdout, 1줄 1개)
  - 진행 상황 (stderr)
"""

import sys
import re
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path


# ─────────────────────────────────────────────
# 유틸
# ─────────────────────────────────────────────

def eprint(*args, **kwargs):
    """진행 상황을 stderr에 출력"""
    print(*args, file=sys.stderr, flush=True, **kwargs)


def extract_username_from_url(url: str) -> str:
    match = re.search(r'threads\.(?:com|net)/@([^/?#]+)', url)
    return match.group(1).lower() if match else ''


def ts_to_date(ts: int) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime('%Y-%m-%d')


# ─────────────────────────────────────────────
# JSON 구조 탐색 헬퍼
# ─────────────────────────────────────────────

def find_all_values(obj, key: str, depth: int = 0, max_depth: int = 25):
    """JSON 전체에서 특정 key의 모든 값을 재귀 수집"""
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


# ─────────────────────────────────────────────
# 포스트 코드 추출
# ─────────────────────────────────────────────

def scan_all_posts(obj, target_username: str, out: dict, depth: int = 0):
    """
    JSON 트리 전체를 재귀 탐색하여 code+taken_at+username을 가진 포스트 dict를 찾는다.
    out: {code: {'code':..., 'taken_at':..., 'username':...}}
    """
    if depth > 30:
        return
    if isinstance(obj, dict):
        code = obj.get('code')
        taken_at = obj.get('taken_at')
        user = obj.get('user')
        # 포스트처럼 생긴 dict: code(문자열), taken_at(숫자), user(dict) 모두 있음
        if (
            code and taken_at
            and isinstance(code, str) and len(code) >= 5
            and isinstance(taken_at, (int, float))
            and isinstance(user, dict)
        ):
            username = user.get('username', '').lower()
            if not target_username or username == target_username:
                if code not in out:
                    out[code] = {
                        'code': code,
                        'taken_at': int(taken_at),
                        'username': username,
                    }
        # 계속 재귀
        for v in obj.values():
            scan_all_posts(v, target_username, out, depth + 1)
    elif isinstance(obj, list):
        for item in obj:
            scan_all_posts(item, target_username, out, depth + 1)


def extract_entries_from_json(json_text: str, target_username: str) -> dict:
    """JSON 문자열 하나에서 포스트 엔트리 dict를 추출. 빠른 사전 필터 적용."""
    if target_username and target_username not in json_text:
        return {}
    if 'taken_at' not in json_text:
        return {}
    try:
        data = json.loads(json_text)
    except Exception:
        return {}
    out = {}
    scan_all_posts(data, target_username, out)
    return out


# ─────────────────────────────────────────────
# 페이지에서 포스트 수집
# ─────────────────────────────────────────────

def collect_all_entries(page, target_username: str, intercepted_jsons: list) -> dict:
    """
    현재 페이지(script 태그) + 인터셉트된 JSON 응답 전체에서
    target_username의 포스트 엔트리를 모두 수집한다.
    반환: {code: entry_dict}
    """
    all_entries: dict = {}

    # 1) script 태그 내 JSON
    try:
        scripts = page.query_selector_all('script[type="application/json"]')
        for s in scripts:
            txt = s.inner_text() or ''
            entries = extract_entries_from_json(txt, target_username)
            all_entries.update(entries)
    except Exception:
        pass

    # 2) 인터셉트된 네트워크 응답
    for json_text in intercepted_jsons:
        entries = extract_entries_from_json(json_text, target_username)
        all_entries.update(entries)

    return all_entries


# ─────────────────────────────────────────────
# 메인
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Threads 프로필 페이지에서 날짜 범위 내 포스트 URL 수집'
    )
    parser.add_argument('url', help='Threads 프로필 URL (예: https://www.threads.com/@specal1849)')
    parser.add_argument(
        '--start-date', required=True,
        help='수집 시작 날짜 (이 날짜 이후 포스트 포함, 형식: YYYY-MM-DD)'
    )
    parser.add_argument(
        '--end-post', default='',
        help=(
            '가장 최신 포스트 코드 (이 포스트부터 포함하여 수집 시작). '
            '생략 시 현재까지 전체 수집.'
        )
    )
    parser.add_argument(
        '--max-scrolls', type=int, default=60,
        help='최대 스크롤 횟수 (기본: 60)'
    )
    parser.add_argument(
        '--scroll-pause', type=float, default=2.5,
        help='스크롤 후 대기 시간(초) (기본: 2.5)'
    )
    args = parser.parse_args()

    profile_url = args.url.rstrip('/')
    target_username = extract_username_from_url(profile_url)
    if not target_username:
        eprint(f'오류: URL에서 사용자명을 추출할 수 없습니다: {profile_url}')
        sys.exit(1)

    # start_date → unix timestamp
    try:
        start_dt = datetime.strptime(args.start_date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        start_ts = int(start_dt.timestamp())
    except ValueError:
        eprint(f'오류: --start-date 형식이 올바르지 않습니다 (YYYY-MM-DD): {args.start_date}')
        sys.exit(1)

    end_post_code = args.end_post.strip()

    eprint(f'[설정] 프로필: @{target_username}')
    eprint(f'[설정] 수집 시작 날짜: {args.start_date} (ts={start_ts})')
    if end_post_code:
        eprint(f'[설정] end-post 코드: {end_post_code} (이 포스트부터 포함하여 수집)')
    eprint(f'[설정] 최대 스크롤 횟수: {args.max_scrolls}')

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        eprint('오류: playwright가 설치되지 않았습니다.')
        eprint('설치: pip install playwright && playwright install chromium')
        sys.exit(1)

    scroll_pause_ms = int(args.scroll_pause * 1000)

    # 저장된 쿠키 로드 (로그인 상태 유지)
    cookie_file = Path(__file__).parent / 'threads_cookies.json'
    saved_cookies = []
    if cookie_file.exists():
        try:
            saved_cookies = json.loads(cookie_file.read_text(encoding='utf-8'))
            eprint(f'[인증] 저장된 쿠키 {len(saved_cookies)}개 로드됨 (로그인 상태)')
        except Exception:
            eprint('[인증] 쿠키 로드 실패, 비로그인 상태로 진행')
    else:
        eprint('[인증] 쿠키 없음 → 비로그인 상태 (스크롤 제한 있음)')
        eprint('        로그인하려면: python save_login.py')

    # 누적 인터셉트 버퍼
    intercepted_jsons: list = []

    with sync_playwright() as p:
        eprint('[1/3] Playwright 브라우저 시작...')
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/124.0.0.0 Safari/537.36'
            ),
            locale='ko-KR',
            viewport={'width': 1280, 'height': 900},
        )
        # 쿠키 주입
        if saved_cookies:
            try:
                context.add_cookies(saved_cookies)
            except Exception as e:
                eprint(f'[인증] 쿠키 주입 실패: {e}')
        page = context.new_page()

        # 네트워크 응답 인터셉트 (GraphQL/Ajax 응답용)
        def handle_response(response):
            try:
                ct = response.headers.get('content-type', '')
                url = response.url
                # Threads가 Ajax로 추가 포스트를 로드할 때 사용하는 엔드포인트
                if 'json' in ct or (
                    'javascript' in ct and (
                        '/ajax/' in url or 'graphql' in url or 'api' in url
                    )
                ):
                    body = response.text()
                    if len(body) > 100:
                        intercepted_jsons.append(body)
            except Exception:
                pass

        page.on('response', handle_response)

        eprint(f'[2/3] 프로필 페이지 로드 중: {profile_url}')
        try:
            page.goto(profile_url, wait_until='networkidle', timeout=45000)
        except Exception:
            try:
                page.goto(profile_url, wait_until='domcontentloaded', timeout=45000)
                page.wait_for_timeout(6000)
            except Exception as e:
                eprint(f'오류: 페이지 로드 실패 - {e}')
                browser.close()
                sys.exit(1)

        eprint('[3/3] 포스트 수집 시작 (스크롤 중)...')

        # 마지막으로 확인한 포스트 집합 (이전 스크롤과 비교하여 새 포스트 감지)
        prev_all_codes: set = set()
        # 전체 누적 엔트리
        all_entries_map: dict = {}

        stop_scrolling = False
        stagnant_scrolls = 0  # 새 포스트가 없는 스크롤 횟수

        for scroll_num in range(args.max_scrolls + 1):
            # 현재 페이지 + 인터셉트에서 전체 엔트리 수집
            current_map = collect_all_entries(page, target_username, intercepted_jsons)
            all_entries_map.update(current_map)

            new_codes = set(current_map.keys()) - prev_all_codes
            if scroll_num == 0:
                eprint(f'  초기 로드: {len(current_map)}개 포스트 발견')
            elif new_codes:
                eprint(f'  스크롤 {scroll_num}: {len(new_codes)}개 새 포스트 발견 (누계: {len(all_entries_map)}개)')
                stagnant_scrolls = 0
            else:
                stagnant_scrolls += 1

            prev_all_codes = set(all_entries_map.keys())

            if stop_scrolling:
                break

            if scroll_num >= args.max_scrolls:
                eprint(f'최대 스크롤 횟수({args.max_scrolls}) 도달')
                break

            # 3회 연속 새 포스트 없으면 피드 끝으로 판단
            if stagnant_scrolls >= 3 and scroll_num > 2:
                eprint(f'  → 3회 연속 새 포스트 없음, 피드 끝 판단')
                break

            # 스크롤
            prev_height = page.evaluate('document.body.scrollHeight')
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            page.wait_for_timeout(scroll_pause_ms)

            new_height = page.evaluate('document.body.scrollHeight')
            if new_height == prev_height and scroll_num > 1:
                # 한 번 더 대기 후 재확인
                page.wait_for_timeout(3000)
                final_height = page.evaluate('document.body.scrollHeight')
                if final_height == prev_height:
                    eprint(f'  스크롤 {scroll_num+1}: 페이지 높이 변화 없음 → 피드 끝')
                    break

        browser.close()

    eprint(f'\n[분석] 총 {len(all_entries_map)}개 포스트 발견, 날짜 필터 적용 중...')

    # 날짜 필터 및 end_post 처리
    # 타임스탬프 기준 최신순 정렬
    sorted_entries = sorted(all_entries_map.values(), key=lambda e: e['taken_at'], reverse=True)

    # end_post 처리: end_post_code가 있으면 그 코드부터 수집 시작
    # (피드는 최신순으로 정렬되므로 end_post 이전 포스트는 더 최신 포스트)
    if end_post_code:
        end_post_found = any(e['code'] == end_post_code for e in sorted_entries)
        if not end_post_found:
            eprint(f'경고: --end-post 코드({end_post_code})를 피드에서 찾지 못했습니다.')
            eprint('  해당 포스트가 이미 만료되었거나, 로딩 범위 밖에 있을 수 있습니다.')
        # end_post_code가 있으면: end_post_code 인덱스 이후부터 수집
        # (최신순 정렬이므로, end_post_code를 찾으면 그 이후가 "오래된" 포스트)
        # end_post는 "가장 최신 포스트로 포함" → 즉 이 코드와 같은 taken_at 이하만 포함
        end_ts = None
        for e in sorted_entries:
            if e['code'] == end_post_code:
                end_ts = e['taken_at']
                break
        if end_ts is not None:
            sorted_entries = [e for e in sorted_entries if e['taken_at'] <= end_ts]

    # start_date 필터
    result = [e for e in sorted_entries if e['taken_at'] >= start_ts]

    eprint(f'[완료] 날짜 범위 내 포스트: {len(result)}개')

    # URL 출력 (최신순)
    for e in result:
        url = f"https://www.threads.com/@{e['username']}/post/{e['code']}"
        print(url)


if __name__ == '__main__':
    main()
