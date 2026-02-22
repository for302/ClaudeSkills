---
name: hwp-autofill
description: 엑셀 파일에서 교육과정 데이터를 읽어 한글(HWP/HWPX) 자동입력 매크로 코드가 포함된 .md 파일을 시트별로 생성합니다. 사용자가 엑셀 파일을 제공하면 각 시트의 변수(A열)와 값(C열)을 추출하여 HWP 스크립트 매크로 코드를 자동 생성합니다. 이 스킬은 사용자가 HWP 매크로 생성, 교육과정 자동입력, 엑셀에서 HWP 변환 등을 요청할 때 사용됩니다.
---

# HWP 자동입력 매크로 생성기

## Overview

엑셀 파일의 각 시트에서 `{{변수명}}` 패턴의 변수(A열)와 해당 값(C열)을 읽어, 한글(HWP/HWPX) 문서에 자동 삽입할 수 있는 스크립트 매크로 코드를 `.md` 파일로 생성합니다.

## 엑셀 파일 구조

처리 대상 엑셀 파일은 다음 구조를 따릅니다:

| 열 | 내용 | 예시 |
|---|---|---|
| A열 (A3:A41) | 변수명 (`{{...}}` 패턴) | `{{edu_title}}` |
| B열 | 라벨 (참고용, 미사용) | 훈련과정명 |
| C열 | 실제 값 | 의료·바이오 AI 리터러시 입문 |

- 각 시트가 1개의 `.md` 파일을 생성하며, 파일명은 시트명으로 합니다
- `{{...}}` 패턴이 없는 시트는 자동으로 건너뜁니다
- 여러 줄 값은 HWP 문단 구분자 `\r` + 문자열 연결 패턴으로 변환됩니다

## 지원하는 변수 목록

A3:A41 범위에서 다음 변수들을 인식합니다:

`{{edu_title}}`, `{{edu_cate01}}` ~ `{{edu_cate05}}`, `{{edu_ncslevel}}`, `{{edu_time}}`, `{{edu_target}}`, `{{edu_job}}`, `{{edu_limit}}`, `{{edu_feature}}`, `{{edu_summary}}`, `{{edu_ncsreason}}`, `{{edu_goal}}`, `{{edu_guidegoal}}`, `{{edu_guidegoaldetail}}`, `{{edu_guidegoaldetail-1}}` ~ `{{edu_guidegoaldetail-3}}`, `{{edu_learnhow}}`, `{{edu_testhow}}`, `{{edu_book}}`, `{{edu_needreason}}`, `{{edu_curri}}`, `{{edu_edutime}}`, `{{time_day_1}}` ~ `{{time_day_5}}`, `{{topic_day_1}}` ~ `{{topic_day_5}}`

### `{{edu_future}}` 파생 변수

`{{edu_future}}` (A28)의 내용은 `[Basic]`, `[Advance]`, `[Expert]` 섹션으로 구분되며, 각 섹션의 줄을 개별 변수로 추출합니다:

| 변수명 | 소스 |
|---|---|
| `{{edu_future-Basic-1}}` | [Basic] 아래 1번째 줄 |
| `{{edu_future-Basic-2}}` | [Basic] 아래 2번째 줄 |
| `{{edu_future-Basic-3}}` | [Basic] 아래 3번째 줄 |
| `{{edu_future-Advance-4}}` | [Advance] 아래 1번째 줄 |
| `{{edu_future-Advance-5}}` | [Advance] 아래 2번째 줄 |
| `{{edu_future-Advance-6}}` | [Advance] 아래 3번째 줄 |
| `{{edu_future-Advance-7}}` | [Advance] 아래 4번째 줄 |
| `{{edu_future-Expert-1}}` | [Expert] 아래 1번째 줄 |

## Workflow

### 1. 엑셀 파일 확인

사용자가 엑셀 파일 경로를 제공하면, 파일 존재 여부와 시트 목록을 확인합니다.

### 2. 매크로 생성 스크립트 실행

`scripts/generate_macros.py` 스크립트를 실행하여 `.md` 파일을 생성합니다:

```bash
python scripts/generate_macros.py <엑셀파일경로> [출력디렉토리] [값열번호]
```

**파라미터:**
- `엑셀파일경로` (필수): 처리할 .xlsx 파일 경로
- `출력디렉토리` (선택): .md 파일 저장 위치. 기본값: 엑셀 파일 옆 `output/` 폴더
- `값열번호` (선택): 값이 있는 열 번호. 기본값: `3` (C열)

### 3. 결과 확인

생성된 `.md` 파일을 확인하여 매크로 코드가 올바르게 생성되었는지 검증합니다.

## 여러 줄 값 처리 규칙

엑셀 셀 내 줄바꿈(`\n`)이 포함된 값은 HWP 매크로 형식으로 변환됩니다:

**한 줄 값:**
```javascript
"{{edu_title}}": "교육과정명",
```

**여러 줄 값:**
```javascript
"{{edu_guidegoaldetail-1}}":
      "1교시: 주제1\r" +
      "- 세부내용1\r" +
      "- 세부내용2\r" +
      "- 세부내용3",
```

## Resources

### scripts/
- `generate_macros.py`: 엑셀 파일을 읽어 시트별 HWP 매크로 .md 파일을 생성하는 메인 스크립트
