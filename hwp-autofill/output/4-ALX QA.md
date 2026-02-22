# 4-ALX QA - HWP 자동입력 매크로

## 사용법
1. 한글(HWP/HWPX) 문서를 엽니다
2. 도구 > 스크립트 매크로 에서 아래 코드를 붙여넣고 실행합니다

## 매크로 코드

```javascript
function OnScriptMacro_자동입력매크로() {
  // 치환 맵: 값 중 줄바꿈은 \r 로 표기 (한글에서 문단 구분)
  var map = {
    "{{edu_title}}": " ISO 13485 기반 QMS 반복문서 AI 자동화 구현 (18h)",
    "{{edu_cate01}}": "20.정보통신",
    "{{edu_cate02}}": "01.정보기술",
    "{{edu_cate03}}": "07.인공지능 ",
    "{{edu_cate04}}": "07.생성형AI엔지니어링",
    "{{edu_cate05}}": "2001070707_25v1",
    "{{edu_ncslevel}}": "5",
    "{{edu_time}}": "18시간( 3일)",
    "{{edu_target}}": "의료기기 개발·제조 기업의 품질관리(QA/QC) 담당자 및 품질경영시스템(QMS) 운영 관련 임직원",
    "{{edu_job}}": "의료기기 품질관리(QA/QC), 품질경영시스템(QMS) 운영, 내부감사, 규제대응 등",
    "{{edu_limit}}": "20명",
    "{{edu_feature}}": "의료기기 품질관리 담당자를 대상으로 ISO 13485 기반 QMS 반복문서(SOP, CAPA, 내부감사 문서)의 구조를 이해하고, 생성형 AI(ChatGPT, Claude)와 n8n을 활용하여 문서 자동 생성·검증 체계를 구축하는 AI 전환(AX) 심화 과정으로, 실제 QMS 문서 자동화 실습 중심의 교육을 통해 품질관리 업무 혁신 역량을 강화하는 신기술·융복합 훈련과정",
    "{{edu_summary}}": "QMS 문서의 구조와 유형을 이해하고, ISO 13485 요구사항과 문서 항목 간 관계를 분석한다. ChatGPT를 활용한 프롬프트 기반 문서 생성 기법을 습득하고, 기존 QMS 문서를 프롬프트 설계를 통해 생성하는 실습을 진행한다. Office for Claude를 활용하여 문서 템플릿을 설계하고 문서 AI 자동화 체계를 구현하는 실습을 수행한다. 최종적으로 문서 작성부터 검증까지의 자동 흐름을 설계하여 QMS 문서 자동화 역량을 완성한다.",
    "{{edu_ncsreason}}": "본 훈련과정은 의료기기 품질관리(QA) 현장의 QMS 문서 자동화 AI 전환(AX) 수요에 맞춰 ISO 13485 기반 문서 자동화 역량 강화를 목적으로 설계된 과정으로, 기존 NCS 분류체계에 정확히 부합하는 능력단위가 부재하여 산업 현장 맞춤형 커리큘럼으로 자체 구성함",
    "{{edu_goal}}": "의료기기 품질관리 담당자가 QMS 문서의 구조와 ISO 13485 요구사항을 이해하고, 프롬프트 기반 문서 생성(ChatGPT)과 문서 템플릿 설계 및 AI 자동화 구현(Office for Claude)을 통해 QMS 문서의 작성부터 검증까지 자동 흐름을 직접 설계·구축할 수 있는 QMS 문서 자동화 역량을 습득하는 것을 목표로 함",
    "{{edu_guidegoal}}": "ISO 13485 기반 QMS 문서의 구조와 AI 활용 자동화 방법론을 명확히 이해하고, 실습을 통해 생성형 AI 기반 문서 자동 생성·검증 능력을 키워 의료기기 품질관리 업무 현장에서 반복문서 작성 시간을 획기적으로 단축하고 문서 품질을 향상시킬 수 있는 실무 역량을 갖추어 업무 효율성을 높입니다.",
    "{{edu_guidegoaldetail}}":
      "* QMS 문서의 구조와 유형(SOP, CAPA, 내부감사 등) 이해 및 문서 작성 요건 분석\r" +
      "* ISO 13485 요구사항의 이해 및 문서 항목 간 매핑 체계 설계 능력 습득\r" +
      "* ChatGPT를 활용한 프롬프트 기반 QMS 문서 생성 기법 배양\r" +
      "* Office for Claude를 활용한 문서 템플릿 설계 실습\r" +
      "* Office for Claude를 활용한 문서 AI 자동화 설계 및 구현 실습\r" +
      "* 문서 작성–검증 자동 흐름 설계 역량 함양",
    "{{edu_guidegoaldetail-1}}":
      "[QMS 문서 및 ISO 13485 요구사항 이해]\r" +
      "- QMS 문서의 구조와 유형(SOP, CAPA, 내부감사) 분석 및 작성 요건 이해\r" +
      "- ISO 13485 요구사항 분석 및 문서 항목 간 매핑 체계 설계",
    "{{edu_guidegoaldetail-2}}":
      "[프롬프트 기반 문서 생성 및 템플릿 설계]\r" +
      "- ChatGPT를 활용한 프롬프트 설계 기반 기존 QMS 문서 생성 실습\r" +
      "- Office for Claude를 활용한 문서 템플릿 설계 실습",
    "{{edu_guidegoaldetail-3}}":
      "[문서 AI 자동화 구현 및 자동 흐름 설계]\r" +
      "- Office for Claude를 활용한 문서 AI 자동화 설계 및 구현 실습\r" +
      "- 문서 작성–검증 자동 흐름 설계 및 최종 산출물 완성",
    "{{edu_learnhow}}":
      "강의: 슬라이드 및 ISO 13485 QMS 문서 사례 자료를 활용하여 QMS 문서 구조와 ISO 요구사항, AI 자동화 방법론을 시각적으로 설명\r" +
      "실습: ChatGPT를 활용한 프롬프트 기반 문서 생성 실습, Office for Claude를 활용한 템플릿 설계 및 문서 AI 자동화 구현 실습, 문서 작성–검증 자동 흐름 설계, 최종 산출물 완성 프로젝트 수행\r" +
      "토론: 의료기기 품질관리 현장의 QMS 문서 자동화 적용 방안에 대한 그룹 토론을 통해 실무 적용 능력 배양\r" +
      "Q&A: 실시간 질문을 통해 이해도 점검 및 피드백 제공",
    "{{edu_testhow}}":
      "가. 평가시점 : 교과목 수업 종료시\r" +
      "나. 평가내용 \r" +
      "• ChatGPT를 활용한 프롬프트 기반 QMS 문서 생성 능력\r" +
      "• Office for Claude를 활용한 문서 템플릿 설계 및 AI 자동화 구현 능력\r" +
      "• 문서 작성–검증 자동 흐름 설계 능력\r" +
      "다. 평가방법\r" +
      "• 결과평가 : 최종 산출물(문서 템플릿, AI 자동화 구현물, 자동 흐름 설계서) 제출 및 구두발표",
    "{{edu_book}}": "자체교재",
    "{{edu_needreason}}": "의료기기 품질관리(QA) 담당자들의 경우 ISO 13485 기반 QMS 반복문서(SOP, CAPA, 내부감사 문서) 작성에 많은 시간을 소요하며, 문서 품질의 일관성 유지에 어려움을 겪는 경우가 많음. 또한 관련 직무의 수요조사 결과 AI를 활용한 QMS 문서 자동화 교육의 필요성이 제기됨. 본 과정은 의료기기 품질관리 현장에서 필요한 QMS 문서 자동화 역량을 배양하여 생성형 AI 기반 문서 자동 생성·검증 체계를 구축하며, 반복문서 작성 시간을 획기적으로 단축하여 업무의 프로세스와 효율을 높일 수 있다",
    "{{edu_curri}}": "ISO 13485 기반 QMS 반복문서(SOP, CAPA, 내부감사)의 구조를 이해하고, ISO 요구사항과 문서 항목 간 매핑 체계를 설계한다. ChatGPT·Claude를 활용한 프롬프트 기반 QMS 문서 자동 생성 기법을 습득하고, SOP 자동 작성 템플릿 설계, CAPA 보고서 AI 구조화 및 자동 초안 생성, 내부감사 체크리스트 자동 생성을 실습한다. n8n 기반 문서 작성–검증 자동 흐름을 설계하여 QMS 문서 자동화 체계를 완성한다.",
    "{{edu_edutime}}": "18시간 (100%)",
    "{{time_day_1}}": "6",
    "{{time_day_2}}": "6",
    "{{time_day_3}}": "6",
    "{{time_day_4}}": "0",
    "{{time_day_5}}": "0",
    "{{topic_day_1}}": "QMS 문서의 유형(SOP, CAPA, 내부감사 등)과 구조를 분석하고, 각 문서 유형별 작성 요건과 실무에서의 문서 작성 흐름을 이해한다. ISO 13485 요구사항의 핵심 조항을 분석·해설하고, ISO 요구사항과 문서 항목 간 매핑 체계를 직접 설계하는 실습을 진행한다. 매핑 결과를 검토하고 실제 문서에 적용하는 토론을 통해 QMS 문서 자동화의 기반을 다진다.",
    "{{topic_day_2}}": "ChatGPT를 활용한 프롬프트 설계의 원리와 기법을 학습하고, 기존 QMS 문서(SOP, CAPA 등)를 프롬프트 설계를 통해 생성하는 실습을 진행한다. 생성된 문서의 품질을 검토하고 프롬프트를 최적화하는 심화 실습 후, Office for Claude를 활용하여 SOP·CAPA 문서 템플릿을 직접 설계하는 실습을 수행하여 프롬프트 기반 문서 생성과 템플릿화 능력을 함양한다.",
    "{{topic_day_3}}": "Office for Claude를 활용하여 문서 AI 자동화 체계를 설계하고 문서 자동 생성·검증 기능을 구현하는 실습을 진행한다. 문서 작성부터 검증까지의 전체 프로세스를 통합한 자동 흐름을 설계하고, 3일간의 학습 내용을 종합하여 문서 템플릿, AI 자동화 구현물, 자동 흐름 설계서를 최종 산출물로 완성한다. 팀별 발표와 피드백을 통해 현업 적용 전략을 수립한다.",
    "{{topic_day_4}}": "0",
    "{{topic_day_5}}": "0",
    "{{edu_future-Basic-1}}": "Lv.1 - 의료·바이오 AI 리터러시 입문",
    "{{edu_future-Basic-2}}": "Lv.2 - 의료·바이오 데이터리터러시와 데이터시각화",
    "{{edu_future-Basic-3}}": "Lv.2 - AI 워크플로우 설계 기초",
    "{{edu_future-Advance-4}}": "Lv.3 - ISO 13485 기반 QMS 반복문서 AI 자동화 구현 (본 과정)",
    "{{edu_future-Advance-5}}": "Lv.3 - 의료기기 인허가(RA)를 위한 AI 활용",
    "{{edu_future-Advance-6}}": "Lv.4 - 의료기기 R&D를 위한 AI 활용",
    "{{edu_future-Advance-7}}": "Lv.5 - 의료기기 데이터 파이프라인 구축 및 운영",
    "{{edu_future-Expert-1}}": ""
  };

  // 토큰을 하나씩 검색 → 삭제 → InsertText로 다줄 텍스트 삽입
  for (var key in map) {
    while (true) {
      // 토큰 찾기
      HAction.GetDefault("RepeatFind", HParameterSet.HFindReplace.HSet);
      HParameterSet.HFindReplace.FindString = key;
      HParameterSet.HFindReplace.Direction = 1;       // forward
      HParameterSet.HFindReplace.MatchCase = 0;
      HParameterSet.HFindReplace.WholeWordOnly = 0;
      HParameterSet.HFindReplace.IgnoreMessage = 1;   // 메시지 숨김

      if (!HAction.Execute("RepeatFind", HParameterSet.HFindReplace.HSet)) break;

      // 토큰 삭제
      HAction.Run("Delete");

      // 텍스트 삽입 (여러 줄은 \r 로 구분)
      HAction.GetDefault("InsertText", HParameterSet.HInsertText.HSet);
      HParameterSet.HInsertText.Text = map[key];
      HAction.Execute("InsertText", HParameterSet.HInsertText.HSet);
    }
  }

  return true;
}
```
