# 수집 대상 계정 설정

이 파일을 수정하여 수집할 Threads 계정과 저장 경로를 관리한다.  
다른 사용자가 이 스킬을 사용할 때는 아래 계정 정보를 본인의 계정으로 교체하면 된다.

---

## 등록된 계정

| 계정 | 프로필 URL | 저장 경로 | 마지막 수집일 | 번역 |
|---|---|---|---|---|
| @specal1849 | https://www.threads.com/@specal1849 | D:\Dropbox\00_Note\Project\43.AI Curriculum\_Inbox | 2026-04-19 | - |
| @unclejobs.ai | https://www.threads.com/@unclejobs.ai | D:\Dropbox\00_Note\Project\43.AI Curriculum\_Inbox | 2026-04-19 | - |
| @choi.openai | https://www.threads.com/@choi.openai | D:\Dropbox\00_Note\Project\43.AI Curriculum\_Inbox | 2026-04-19 | - |
| @flowkater | https://www.threads.com/@flowkater | D:\Dropbox\00_Note\Project\43.AI Curriculum\_Inbox | 2026-04-19 | - |
| @claudeai | https://www.threads.com/@claudeai | D:\Dropbox\00_Note\Project\43.AI Curriculum\AI-Official-Threads\@claudeai | 2026-04-19 | ko |
| @chatgpt | https://www.threads.com/@chatgpt | D:\Dropbox\00_Note\Project\43.AI Curriculum\AI-Official-Threads\@chatgpt | 2026-04-19 | ko |
| @google | https://www.threads.com/@google | D:\Dropbox\00_Note\Project\43.AI Curriculum\AI-Official-Threads\@google | 2026-04-19 | ko |

---

## 계정 추가 방법

아래 행을 복사하여 표에 추가한다:

```
| @계정명 | https://www.threads.com/@계정명 | C:/저장/경로 | YYYY-MM-DD | - |
```

번역이 필요한 계정은 마지막 컬럼에 언어 코드(예: `ko`)를 입력한다.

---

## 필드 설명

| 필드 | 설명 |
|---|---|
| 계정 | Threads @username |
| 프로필 URL | 프로필 페이지 전체 URL |
| 저장 경로 | 수집한 .md 파일을 저장할 로컬 경로 |
| 마지막 수집일 | 가장 최근에 수집한 날짜 (업데이트 수집 시 이 날짜 다음 날부터 수집) |
| 번역 | 번역 대상 언어 코드 (예: `ko`). `-`이면 번역 안 함. 업데이트 수집 시 `--translate <코드>` 옵션 자동 적용 |
