#!/usr/bin/env python3
"""
save_login.py
브라우저 창을 열어 Threads.com에 직접 로그인하고 쿠키를 저장한다.

사용법:
  python save_login.py

저장 위치: scripts/threads_cookies.json
"""

import json
import sys
from pathlib import Path

COOKIE_FILE = Path(__file__).parent / 'threads_cookies.json'


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print('오류: playwright가 설치되지 않았습니다.')
        print('설치: pip install playwright && playwright install chromium')
        sys.exit(1)

    print('=' * 55)
    print('Threads 로그인 도우미')
    print('=' * 55)
    print()
    print('브라우저 창이 열립니다.')
    print('Threads.com에 로그인한 후, 로그인이 완료되면')
    print('이 창(터미널)으로 돌아와서 Enter를 누르세요.')
    print()

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,   # 사용자가 직접 볼 수 있는 창
            args=['--start-maximized'],
        )
        context = browser.new_context(
            viewport=None,
            user_agent=(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/124.0.0.0 Safari/537.36'
            ),
        )
        page = context.new_page()

        print('[브라우저] Threads.com 열는 중...')
        page.goto('https://www.threads.com/login', timeout=30000)

        print('[대기] 브라우저에서 로그인하세요. 로그인 감지 시 자동으로 쿠키를 저장합니다.')
        print('       최대 5분 대기...')

        # 로그인 완료 자동 감지: sessionid 쿠키가 생길 때까지 폴링
        import time
        deadline = time.time() + 300  # 5분
        logged_in = False
        while time.time() < deadline:
            cookies = context.cookies()
            session_cookies = [c for c in cookies if c.get('name') in ('sessionid', 'ds_user_id') and ('threads' in c.get('domain', '') or 'instagram' in c.get('domain', ''))]
            if session_cookies:
                print(f'\n[감지] 로그인 완료! (쿠키 {len(session_cookies)}개 확인)')
                logged_in = True
                break
            # 홈 피드로 이동했으면 로그인된 것
            cur = page.url
            if 'threads.com' in cur and '/login' not in cur and '/accounts/' not in cur:
                print(f'\n[감지] 로그인 완료! (URL: {cur})')
                logged_in = True
                break
            time.sleep(3)

        if not logged_in:
            print('\n[타임아웃] 5분 내 로그인이 감지되지 않았습니다.')
            browser.close()
            sys.exit(1)

        # 쿠키 저장 (잠깐 대기 후)
        import time
        time.sleep(2)
        cookies = context.cookies()
        browser.close()

        if not cookies:
            print('오류: 쿠키를 가져오지 못했습니다.')
            sys.exit(1)

        # threads.com 쿠키만 필터링
        threads_cookies = [c for c in cookies if 'threads' in c.get('domain', '') or 'instagram' in c.get('domain', '')]

        COOKIE_FILE.write_text(json.dumps(threads_cookies, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'\n[완료] 쿠키 저장됨: {COOKIE_FILE}')
        print(f'       저장된 쿠키 수: {len(threads_cookies)}개')
        print()
        print('이제 bulk_download.py 또는 fetch_profile_urls.py에서')
        print('자동으로 이 쿠키를 사용하여 로그인 상태로 크롤링합니다.')


if __name__ == '__main__':
    main()
