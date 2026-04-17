---
name: threads-archiver
description: Threads.com(스레드) 포스트를 수집하여 Obsidian 최적화 Markdown 파일로 저장하는 스킬. 단일 URL 아카이브, 프로필 전체 벌크 수집, 날짜 범위 필터, 병렬 다운로드, 로그인 인증을 모두 지원한다. "스레드 저장해줘", "threads 아카이브", "프로필 전체 다운로드", "최신 포스트 수집", "스레드 업데이트 확인" 같은 요청에 이 스킬을 사용할 것.
---

# Threads Archiver

Threads.com 포스트를 수집하여 **Obsidian 최적화 Markdown 파일**로 저장한다.  
단일 URL 아카이브부터 프로필 전체 벌크 수집까지 지원하며, 다중 계정·대량 수집 시 Claude Agent를 병렬로 실행한다.

## 스크립트 구성

| 스크립트 | 역할 |
|---|---|
| `scripts/fetch_threads.py` | 단일 포스트 URL → 시리즈 전체 수집 → .md 저장 |
| `scripts/fetch_profile_urls.py` | 프로필 페이지 스크롤 → 날짜 범위 내 포스트 URL 목록 추출 |
| `scripts/bulk_download.py` | URL 목록 → 병렬 일괄 다운로드 |
| `scripts/split_urls.py` | URL 목록 파일 → N개 청크 파일로 균등 분할 |
| `scripts/save_login.py` | 브라우저 로그인 → 쿠키 저장 (프로필 벌크 수집 시 필요) |

스킬 기본 디렉토리: `D:/Web_Dev/ClaudeSkills/threads-archiver`  
쿠키 저장 위치: `scripts/threads_cookies.json` (save_login.py 실행 후 자동 생성)

---

## 등록된 계정

수집 대상 계정, 저장 경로, 마지막 수집일은 `references/accounts.md`에서 관리한다.  
"업데이트 수집해줘" 요청 시 이 파일을 먼저 읽어 등록된 계정 목록과 마지막 수집일을 확인한다.  
다른 사용자가 이 스킬을 사용할 때는 `references/accounts.md`의 계정 정보를 본인 계정으로 교체한다.

---

## 사용 시점

- **단일 URL 저장**: Threads 링크 하나를 저장하거나 내용을 정리하고 싶을 때
- **신규 계정 벌크 수집**: 특정 계정을 처음 등록하고 과거 포스트를 날짜 범위로 수집할 때
- **최신 업데이트 수집**: "업데이트 수집해줘" → `references/accounts.md` 확인 → 등록된 계정 전체를 계정당 1개 Agent로 병렬 수집

---

## 의존성 확인

처음 사용 시 설치:

```bash
pip install playwright
playwright install chromium
```

---

## 워크플로우 A: 단일 URL 아카이브

```bash
cd D:/Web_Dev/ClaudeSkills/threads-archiver
PYTHONIOENCODING=utf-8 python scripts/fetch_threads.py "<THREADS_URL>" --output "<저장할_경로>"
```

완료 후 생성된 `.md` 파일 경로, 포스트 수, 이미지 수를 사용자에게 알린다.

---

## 워크플로우 B: 신규 계정 벌크 수집

### Step 1: 로그인 (처음 한 번만)

```bash
cd D:/Web_Dev/ClaudeSkills/threads-archiver
PYTHONIOENCODING=utf-8 python scripts/save_login.py
```

### Step 2: URL 목록 수집

```bash
PYTHONIOENCODING=utf-8 python scripts/fetch_profile_urls.py "<프로필_URL>" \
  --start-date <YYYY-MM-DD> \
  [--end-post <포스트_코드>] \
  --max-scrolls 100 \
  > /tmp/urls.txt
```

### Step 3: URL 수에 따라 분기 처리

URL 개수를 확인한다:

```bash
wc -l /tmp/urls.txt
```

**≤ 50개**: 바로 다운로드

```bash
PYTHONIOENCODING=utf-8 python scripts/bulk_download.py \
  --file /tmp/urls.txt --output "<저장할_경로>" --workers 3
```

**51~150개**: 2개 청크로 분할 → **2개 Agent 병렬 실행**

```bash
# 청크 분할
PYTHONIOENCODING=utf-8 python scripts/split_urls.py /tmp/urls.txt \
  --chunks 2 --output-dir /tmp/chunks
```

단일 메시지에서 2개 Agent를 동시에 실행한다. 각 Agent에게 전달:
- 맡은 청크 파일 경로 (`/tmp/chunks/chunk_01.txt`, `/tmp/chunks/chunk_02.txt`)
- 저장 경로
- 스킬 디렉토리: `D:/Web_Dev/ClaudeSkills/threads-archiver`
- 실행할 명령: `PYTHONIOENCODING=utf-8 python scripts/bulk_download.py --file <청크파일> --output <저장경로> --workers 2`

**151개 이상**: 3개 청크로 분할 → **3개 Agent 병렬 실행**

```bash
PYTHONIOENCODING=utf-8 python scripts/split_urls.py /tmp/urls.txt \
  --chunks 3 --output-dir /tmp/chunks
```

단일 메시지에서 3개 Agent를 동시에 실행한다 (각 Agent: --workers 2).  
전체 동시 브라우저 수 = 청크 수(3) × workers(2) = 6개.

### Step 4: 완료 후 처리

- 각 Agent의 결과(성공/실패 수)를 취합하여 사용자에게 보고한다.
- 실패 URL이 있으면 재시도하거나 목록을 사용자에게 전달한다.
- `references/accounts.md`에 새 계정과 오늘 날짜를 추가한다.

---

## 워크플로우 C: 등록 계정 업데이트 수집 (병렬 Agent)

"업데이트 수집해줘" 또는 유사한 요청 시 실행한다.

### Step 1: 계정 목록 확인

`references/accounts.md`를 읽어 등록된 모든 계정과 마지막 수집일을 확인한다.

### Step 2: 계정당 1개 Agent 병렬 실행

**등록된 계정 수만큼 Agent를 단일 메시지에서 동시에 실행한다.**  
각 Agent에게 전달할 내용:

```
다음 Threads 계정의 새 포스트를 수집해줘:
- 프로필 URL: <계정_프로필_URL>
- start-date: <마지막_수집일 + 1일>  (예: 마지막 수집일이 2026-04-18이면 2026-04-19)
- 저장 경로: <저장_경로>
- 스킬 디렉토리: D:/Web_Dev/ClaudeSkills/threads-archiver

실행 순서:
1. fetch_profile_urls.py로 URL 목록 수집 (--max-scrolls 20)
2. URL 수 확인 후 적절한 방법으로 bulk_download 실행
   (≤50개: workers 3 직접 실행 / >50개: split_urls.py로 분할 후 서브 Agent 병렬 실행)
3. 성공/실패 수 보고
```

### Step 3: 결과 취합 및 accounts.md 업데이트

- 모든 Agent 완료 후 각 계정의 성공/실패를 취합하여 사용자에게 보고한다.
- `references/accounts.md`의 각 계정 마지막 수집일을 오늘 날짜로 업데이트한다.

---

## 출력 파일 형식

**파일명:** `{첫번째_포스트_첫 문장}.md`

```markdown
---
thread_url: "https://www.threads.com/@specal1849/post/DW6xjIhEQsn"
author: "@specal1849"
date: "2026-04-11"
total_posts: 5
tags:
  - threads
  - archive
---

# 제미나이에 새로운 기능이 업데이트 되었습니다

## 1/5
...
```

---

## 주의사항

- 로그인 쿠키(`threads_cookies.json`)는 일정 기간 후 만료된다. 수집 실패 시 `save_login.py`를 재실행한다.
- 전체 동시 브라우저 수가 6개를 초과하면 IP 차단 위험이 있다. Agent 수 × workers ≤ 6을 유지한다.
- 비공개 계정은 수집 불가.
- Windows에서는 반드시 `PYTHONIOENCODING=utf-8` 환경변수를 붙여서 실행한다.
- 이미지 CDN URL은 일정 기간 후 만료될 수 있다.
