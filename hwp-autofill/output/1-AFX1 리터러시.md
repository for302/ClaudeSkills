# 1-AFX1 리터러시 - HWP 자동입력 매크로

## 사용법
1. 한글(HWP/HWPX) 문서를 엽니다
2. 도구 > 스크립트 매크로 에서 아래 코드를 붙여넣고 실행합니다

## 매크로 코드

```javascript
function OnScriptMacro_자동입력매크로() {
  // 치환 맵: 값 중 줄바꿈은 \r 로 표기 (한글에서 문단 구분)
  var map = {
    "{{edu_title}}": "의료·바이오 AI 리터러시 입문 (4h)",
    "{{edu_cate01}}": "#N/A",
    "{{edu_cate02}}": "#N/A",
    "{{edu_cate03}}": "#N/A",
    "{{edu_cate04}}": "#N/A",
    "{{edu_cate05}}": "#N/A",
    "{{edu_ncslevel}}": "#N/A",
    "{{edu_time}}": "16시간( 1일)",
    "{{edu_target}}": "의료기기 개발·제조 기업 임직원 중 AI 활용에 관심이 있는 전 직군 (품질, RA, R&D, 생산, 영업, 경영지원 등)",
    "{{edu_job}}": "전직무",
    "{{edu_limit}}": "20명",
    "{{edu_feature}}": "의료기기 산업 종사자를 대상으로 생성형 AI의 기본 개념부터 실무 활용까지 다루는 AI 전환(AX) 입문 과정으로, 의료기기 분야 특화 사례와 실습 중심의 교육을 통해 디지털 전환 역량을 강화하는 신기술·융복합 훈련과정",
    "{{edu_summary}}": "의료·바이오 분야의 AI 적용 현황과 한계를 이해하고, ChatGPT·Claude·Gemini 등 주요 생성형 AI 도구의 원리와 활용법을 학습한다. 프롬프트 엔지니어링 기법을 익혀 AI를 고급 활용하고, GPTs·Gems를 통해 나만의 챗봇을 제작하며, AI 기반 문서작성과 NotebookLM을 활용한 리서치·기획 역량을 배양한다. 또한 AI 윤리와 보안에 대한 인식을 갖춘다.",
    "{{edu_ncsreason}}": "본 훈련과정은 의료기기 산업 현장의 AI 전환(AX) 수요에 맞춰 생성형 AI 활용 역량 강화를 목적으로 설계된 과정으로, 기존 NCS 분류체계에 정확히 부합하는 능력단위가 부재하여 산업 현장 맞춤형 커리큘럼으로 자체 구성함",
    "{{edu_goal}}": "의료기기 산업 종사자가 생성형 AI의 개념과 원리를 이해하고, 프롬프트 엔지니어링과 주요 AI 도구(ChatGPT, Claude, Gemini, NotebookLM 등)를 활용하여 문서작성, 리서치, 기획 등 실무 업무에 AI를 효과적으로 적용할 수 있는 기초 역량을 습득하는 것을 목표로 함",
    "{{edu_guidegoal}}": "의료기기 분야의 AI 적용 사례와 생성형 AI 도구의 기본 원리를 명확히 이해하고, 실습을 통해 프롬프트 엔지니어링 능력을 키워 최신 AI 기술을 의료기기 업무 현장에 바로 적용할 수 있는 실무 문제 해결 능력을 갖추어 업무 효율성을 높입니다.",
    "{{edu_guidegoaldetail}}":
      "* 의료·바이오 분야 AI 적용 사례와 한계점 분석\r" +
      "* 생성형 AI(ChatGPT, Claude, Gemini)의 원리와 활용 방법 이해\r" +
      "* 프롬프트 엔지니어링 기법을 통한 AI 고급 활용 능력 배양\r" +
      "* GPTs, Gems를 활용한 맞춤형 챗봇 제작 실습\r" +
      "* AI 기반 문서작성 및 NotebookLM을 활용한 리서치·기획 역량 강화\r" +
      "* AI 윤리 및 보안 이슈에 대한 인식 제고",
    "{{edu_guidegoaldetail-1}}":
      "[의료·바이오 AI 개론 및 생성형 AI 활용]\r" +
      "- 의료기기 분야 AI 적용 사례와 한계점 분석\r" +
      "- 생성형 AI(ChatGPT, Claude, Gemini)의 원리 이해 및 실습",
    "{{edu_guidegoaldetail-2}}":
      "[프롬프트 엔지니어링과 AI 고급 활용]\r" +
      "- 프롬프트 엔지니어링 기법을 통한 생성형 AI 고급 활용\r" +
      "- 나만의 챗봇 만들기 (GPTs, Gems) 실습",
    "{{edu_guidegoaldetail-3}}":
      "[AI 기반 문서작성 및 윤리·보안]\r" +
      "- AI를 활용한 문서작업 및 NotebookLM 활용 리서치·기획\r" +
      "- AI 윤리, 보안의 이해 및 의료기기 업무 적용 시 주의사항",
    "{{edu_learnhow}}":
      "강의: 슬라이드 및 의료기기 산업 사례 영상 자료를 활용하여 시각적 이해를 돕고, 실제 의료기기 AI 적용 사례 중심으로 설명\r" +
      "실습: ChatGPT, Claude, Gemini 등 생성형 AI 도구를 직접 활용한 프롬프트 작성 및 문서작성 실습\r" +
      "토론: 의료기기 업무 현장에서의 AI 활용 방안에 대한 그룹 토론을 통해 실무 적용 능력 배양\r" +
      "Q&A: 실시간 질문을 통해 이해도 점검 및 피드백 제공",
    "{{edu_testhow}}":
      "가. 평가시점 : 교과목 수업 종료시\r" +
      "나. 평가내용 \r" +
      "• 생성형 AI 도구(ChatGPT, Claude, Gemini)의 기본 활용 능력\r" +
      "• 프롬프트 엔지니어링을 통한 업무 적용 능력\r" +
      "• AI 윤리 및 보안에 대한 이해도\r" +
      "다. 평가방법\r" +
      "• 결과평가 : 실습 결과물 제출 및 구두발표",
    "{{edu_book}}": "자체교재",
    "{{edu_needreason}}": "의료기기 산업 종사자들의 경우 AI 기술의 급속한 발전에도 불구하고 실무 적용에 어려움을 겪는 경우가 많음. 또한 관련 직무의 수요조사 결과 생성형 AI 활용 교육의 필요성이 제기됨. 본 과정은 의료기기 산업 현장에서 필요한 AI 리터러시를 배양하여 직무 관련 디지털 전환 역량을 높이며, 생성형 AI 도구를 활용한 문서작성·리서치·기획 등을 통해 업무의 프로세스와 효율을 높일 수 있다",
    "{{edu_curri}}": "의료·바이오 분야의 AI 적용 사례와 한계를 이해하고, ChatGPT·Claude·Gemini 등 생성형 AI의 구조와 활용법을 학습하며, 프롬프트 엔지니어링 기법을 통한 고급 활용 능력을 배양한다. GPTs·Gems를 활용한 맞춤형 챗봇 제작과 AI 기반 문서작성, NotebookLM을 활용한 리서치·기획 역량을 실습하며, AI 윤리·보안 및 의료기기 업무 적용 시 주의사항을 학습하여 민감정보를 안전하게 처리하는 역량을 강화한다.",
    "{{edu_edutime}}": "16시간 (100%)",
    "{{time_day_1}}": "4",
    "{{time_day_2}}": "0",
    "{{time_day_3}}": "0",
    "{{time_day_4}}": "0",
    "{{time_day_5}}": "0",
    "{{topic_day_1}}": "의료·바이오 분야의 AI 적용 현황과 한계를 파악한 후, ChatGPT·Claude·Gemini 등 주요 생성형 AI 도구의 원리를 이해하고 직접 실습한다. 프롬프트 엔지니어링 기법을 익혀 AI를 고급 활용하는 방법을 배우고, GPTs·Gems를 활용하여 의료기기 업무에 특화된 나만의 챗봇을 제작하는 실습을 진행한다. 마지막으로 AI 활용 시 반드시 고려해야 할 윤리적 이슈와 보안 가이드라인을 학습하여 안전한 AI 활용 역량을 갖춘다.",
    "{{topic_day_2}}": "0",
    "{{topic_day_3}}": "0",
    "{{topic_day_4}}": "0",
    "{{topic_day_5}}": "0",
    "{{edu_future-Basic-1}}": "Lv.1 - 의료·바이오 AI 리터러시 입문 (본 과정)",
    "{{edu_future-Basic-2}}": "Lv.2 - 의료기기 데이터 분석 및 AI 활용 기초",
    "{{edu_future-Basic-3}}": "Lv.2 - 의료기기 업무 자동화를 위한 AI 워크플로우",
    "{{edu_future-Advance-4}}": "Lv.3 - 의료기기 품질관리(QA)를 위한 AI 활용",
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
