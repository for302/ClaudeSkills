---
name: threads-archiver
description: Threads.com(스레드) 포스트 URL을 받아 연결된 시리즈 포스트 전체를 자동 수집하고 Obsidian 최적화 Markdown 파일로 저장하는 스킬. 스레드 링크 저장, 컨텐츠 아카이브, 시리즈 글 정리 시 사용. URL 하나만 주면 1/N~N/N 순서로 모든 포스트 텍스트와 이미지/동영상을 하나의 .md 파일에 정리해준다. "스레드 저장해줘", "threads 아카이브", "스레드 내용 정리" 같은 요청에 항상 이 스킬을 사용할 것.
---

# Threads Archiver

Threads.com 포스트 URL을 받아 해당 스레드와 연결된 모든 시리즈 포스트(1/N, 2/N, ...)를 순서대로 수집하여 **Obsidian 최적화 Markdown 파일**로 저장한다.

## 목적

- 스레드 컨텐츠를 영구 보존 (Obsidian 지식창고에 저장)
- 시리즈 포스트(1/5, 2/5 ... 5/5)를 자동으로 전부 수집
- 이미지와 동영상 링크를 인라인으로 포함
- YAML frontmatter로 메타데이터 구조화 (검색/필터 가능)

## 사용 시점

- Threads 링크를 저장하거나 내용을 정리하고 싶을 때
- 시리즈 포스트 전체를 한 파일에 모으고 싶을 때
- 스레드 컨텐츠를 Obsidian에 아카이브할 때

---

## 워크플로우

### Step 1: 의존성 확인

처음 사용 시 아래 명령으로 Playwright를 설치한다:

```bash
pip install playwright
playwright install chromium
```

이미 설치되어 있으면 Skip.

### Step 2: 스크립트 실행

스킬 디렉토리(`threads-archiver/`)에서 실행:

```bash
cd /d/Web_Dev/ClaudeSkills/threads-archiver
PYTHONIOENCODING=utf-8 python scripts/fetch_threads.py "<THREADS_URL>" --output "<저장할_경로>"
```

**예시:**
```bash
PYTHONIOENCODING=utf-8 python scripts/fetch_threads.py "https://www.threads.com/@specal1849/post/DW6xjIhEQsn" --output "C:/Users/username/Obsidian/threads"
```

> Windows 환경에서는 한글 출력을 위해 `PYTHONIOENCODING=utf-8` 환경변수 설정이 필요합니다.

`--output`을 생략하면 현재 디렉토리에 저장.

### Step 3: 결과 확인

스크립트가 완료되면:
- 생성된 `.md` 파일 경로를 사용자에게 알린다
- YAML frontmatter, 포스트 수, 이미지 수를 요약해서 보여준다

---

## 출력 파일 형식

**파일명:** `스레드_@username_YYYYMMDD.md`

**내용 구조:**

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

제미나이에 새로운 기능이 업데이트 되었습니다.
시각자료 표시라는 이름으로 ...

![](https://cdn.threads.net/image_url_here)

---

## 2/5

아무리 오류가 있어도 가장 정확하게 기능을 활용하는건 ...

![](https://cdn.threads.net/image_url_here)

---
```

---

## YAML Frontmatter 필드

| 필드 | 설명 | 예시 |
|------|------|------|
| `thread_url` | 원본 스레드 URL | `"https://www.threads.com/@user/post/ID"` |
| `author` | 작성자 @username | `"@specal1849"` |
| `date` | 작성일 (상대→절대 변환) | `"2026-04-11"` |
| `total_posts` | 시리즈 전체 포스트 수 | `5` |
| `tags` | Obsidian 태그 | `["threads", "archive"]` |

**날짜 변환 규칙:**
- "5일" → 오늘 - 5일
- "1주" → 오늘 - 7일
- "2시간" / "30분" → 오늘
- "5d" / "1w" / "2h" → 동일 방식 처리
- 절대 날짜 표시 시 → 그대로 사용

---

## 이미지 & 동영상 처리

- **이미지**: CDN URL을 `![](url)` 마크다운 문법으로 삽입 → Obsidian에서 인라인 미리보기
- **동영상**: `[동영상 보기](url)` 링크로만 삽입 (다운로드 없음)
- 로그인 없이 공개 포스트 CDN URL 직접 사용

---

## 주의사항

- 공개 포스트만 수집 가능 (비공개 계정 불가)
- Playwright가 헤드리스 브라우저를 실행하므로 첫 실행 시 수 초 소요
- 이미지 CDN URL은 일정 기간 후 만료될 수 있음
- 시리즈 패턴(X/N)이 없는 단독 포스트도 저장 가능 (total_posts: 1)
