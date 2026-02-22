# 3-AFX-3 워크플로우 - HWP 자동입력 매크로

## 사용법
1. 한글(HWP/HWPX) 문서를 엽니다
2. 도구 > 스크립트 매크로 에서 아래 코드를 붙여넣고 실행합니다

## 매크로 코드

```javascript
function OnScriptMacro_자동입력매크로() {
  // 치환 맵: 값 중 줄바꿈은 \r 로 표기 (한글에서 문단 구분)
  var map = {
    "{{edu_title}}": "AI 워크플로우 설계 기초 (8h)",
    "{{edu_cate01}}": "20.정보통신",
    "{{edu_cate02}}": "01.정보기술",
    "{{edu_cate03}}": "07.인공지능 ",
    "{{edu_cate04}}": "07.생성형AI엔지니어링",
    "{{edu_cate05}}": "2001070707_25v1",
    "{{edu_ncslevel}}": "5",
    "{{edu_time}}": "31시간( 1일)",
    "{{edu_target}}": "의료기기 개발·제조 기업 임직원 중 AI를 활용한 업무 자동화와 워크플로우 설계에 관심이 있는 전 직군 (품질, RA, R&D, 생산, 영업, 경영지원 등)",
    "{{edu_job}}": "AI 워크플로우와 자동화가 필요한 모든 직무",
    "{{edu_limit}}": "20명",
    "{{edu_feature}}": "의료기기 산업 종사자를 대상으로 AI 워크플로우 도구(Opal, n8n, Google AI Studio)의 개념부터 실제 업무 자동화 워크플로우 설계·구축까지 다루는 AI 전환(AX) 워크플로우 과정으로, 의료기기 분야 반복 업무의 자동화 사례와 실습 중심의 교육을 통해 업무 프로세스 혁신 역량을 강화하는 신기술·융복합 훈련과정",
    "{{edu_summary}}": "AI 워크플로우 도구(Opal, n8n, Google AI Studio)의 개념과 특성을 이해하고, 의료기기 업무에 적합한 워크플로우를 설계하는 방법을 학습한다. Opal을 활용한 Google 서비스 기반 워크플로우, n8n을 활용한 업무자동화 워크플로우, Google AI Studio를 활용한 멀티모달 AI 워크플로우 앱 개발을 실습하고, 최종적으로 의료기기 업무에 특화된 통합 AI 워크플로우를 구축하는 프로젝트를 수행한다.",
    "{{edu_ncsreason}}": "본 훈련과정은 의료기기 산업 현장의 AI 기반 업무 자동화 전환(AX) 수요에 맞춰 AI 워크플로우 설계 및 구축 역량 강화를 목적으로 설계된 과정으로, 기존 NCS 분류체계에 정확히 부합하는 능력단위가 부재하여 산업 현장 맞춤형 커리큘럼으로 자체 구성함",
    "{{edu_goal}}": "의료기기 산업 종사자가 AI 워크플로우 도구(Opal, n8n, Google AI Studio)의 원리와 활용법을 이해하고, 의료기기 업무의 반복 프로세스를 AI로 자동화하는 워크플로우를 직접 설계·구축할 수 있는 업무 자동화 역량을 습득하는 것을 목표로 함",
    "{{edu_guidegoal}}": "AI 워크플로우 도구의 기본 원리와 설계 방법론을 명확히 이해하고, 실습을 통해 Opal·n8n·Google AI Studio 활용 능력을 키워 의료기기 업무 현장의 반복 프로세스를 AI로 자동화할 수 있는 실무 문제 해결 능력을 갖추어 업무 효율성을 높입니다.",
    "{{edu_guidegoaldetail}}":
      "* AI 워크플로우 도구(Opal, n8n, Google AI Studio)의 개념과 특성 비교 이해\r" +
      "* 의료기기 업무 프로세스 분석 및 AI 워크플로우 설계 방법론 습득\r" +
      "* Opal을 활용한 Google 서비스 기반 업무 자동화 워크플로우 이해\r" +
      "* n8n을 활용한 AI 업무자동화 워크플로우 설계 및 구현 실습\r" +
      "* Google AI Studio를 활용한 멀티모달 AI 워크플로우 앱 개발 실습\r" +
      "* 의료기기 업무에 특화된 통합 AI 워크플로우 구축 및 발표",
    "{{edu_guidegoaldetail-1}}":
      "[AI 워크플로우 도구 이해와 설계]\r" +
      "- AI 워크플로우 도구(Opal, n8n, Google AI Studio)의 개념과 특성 비교\r" +
      "- 의료기기 업무 프로세스 분석 및 워크플로우 설계 방법론",
    "{{edu_guidegoaldetail-2}}":
      "[도구별 워크플로우 실습]\r" +
      "- Opal을 활용한 Google 서비스 기반 업무 자동화 워크플로우 이해\r" +
      "- n8n을 활용한 AI 업무자동화 워크플로우 설계 및 구현",
    "{{edu_guidegoaldetail-3}}":
      "[멀티모달 AI 앱 및 통합 워크플로우 구축]\r" +
      "- Google AI Studio를 활용한 멀티모달 AI 워크플로우 앱 개발\r" +
      "- 의료기기 업무에 특화된 통합 AI 워크플로우 구축 및 발표",
    "{{edu_learnhow}}":
      "강의: 슬라이드 및 의료기기 업무 자동화 사례 영상 자료를 활용하여 AI 워크플로우 도구의 개념과 설계 방법을 시각적으로 설명\r" +
      "실습: Opal·n8n·Google AI Studio를 직접 활용한 워크플로우 설계 및 구축 실습, 의료기기 업무 시나리오 기반 통합 프로젝트 수행\r" +
      "토론: 의료기기 업무 현장의 반복 프로세스 개선 방안에 대한 그룹 토론을 통해 실무 적용 능력 배양\r" +
      "Q&A: 실시간 질문을 통해 이해도 점검 및 피드백 제공",
    "{{edu_testhow}}":
      "가. 평가시점 : 교과목 수업 종료시\r" +
      "나. 평가내용 \r" +
      "• AI 워크플로우 도구(n8n, Google AI Studio)의 기본 활용 능력\r" +
      "• 의료기기 업무 프로세스에 맞는 워크플로우 설계 능력\r" +
      "• 통합 AI 워크플로우 구축 및 발표 능력\r" +
      "다. 평가방법\r" +
      "• 결과평가 : 통합 워크플로우 구축 결과물 제출 및 구두발표",
    "{{edu_book}}": "자체교재",
    "{{edu_needreason}}": "의료기기 산업 현장에서 반복적인 업무 프로세스가 많으나 자동화 도구 활용 역량이 부족하여 업무 효율화에 한계를 겪는 경우가 많음. 또한 관련 직무의 수요조사 결과 AI 기반 업무 자동화 워크플로우 설계 교육의 필요성이 제기됨. 본 과정은 의료기기 산업 현장에서 필요한 AI 워크플로우 설계 역량을 배양하여 Opal·n8n·Google AI Studio를 활용한 업무 자동화 체계를 구축하며, 반복 업무의 자동화를 통해 업무의 프로세스와 효율을 높일 수 있다",
    "{{edu_curri}}": "AI 워크플로우 도구(Opal, n8n, Google AI Studio)의 개념과 특성을 비교·이해하고, 의료기기 업무 프로세스를 분석하여 자동화 대상을 도출한다. Opal을 활용한 Google 서비스 기반 워크플로우, n8n을 활용한 AI 업무자동화 워크플로우, Google AI Studio를 활용한 멀티모달 AI 워크플로우 앱 개발을 단계별로 실습하며, 최종적으로 의료기기 업무에 특화된 통합 AI 워크플로우를 구축하여 업무 자동화 역량을 강화한다.",
    "{{edu_edutime}}": "8시간 (100%)",
    "{{time_day_1}}": "8",
    "{{time_day_2}}": "0",
    "{{time_day_3}}": "0",
    "{{time_day_4}}": "0",
    "{{time_day_5}}": "0",
    "{{topic_day_1}}": "AI 워크플로우 도구(Opal, n8n, Google AI Studio)의 개념과 특성을 비교·이해한 후, 의료기기 업무 프로세스를 분석하여 AI 워크플로우를 설계하는 방법론을 학습한다. Opal을 활용한 Google 서비스 기반 업무 자동화, n8n을 활용한 AI 업무자동화 워크플로우 설계, Google AI Studio를 활용한 멀티모달 AI 앱 개발을 단계별로 실습한다. 최종적으로 의료기기 업무에 특화된 통합 AI 워크플로우를 직접 구축하는 프로젝트를 수행하고 결과를 발표하여 업무 프로세스 혁신 역량을 함양한다.",
    "{{topic_day_2}}": "0",
    "{{topic_day_3}}": "0",
    "{{topic_day_4}}": "0",
    "{{topic_day_5}}": "0",
    "{{edu_future-Basic-1}}": "Lv.1 - 의료·바이오 AI 리터러시 입문",
    "{{edu_future-Basic-2}}": "Lv.2 - 의료·바이오 데이터리터러시와 데이터시각화",
    "{{edu_future-Basic-3}}": "Lv.2 - AI 워크플로우 설계 기초 (본 과정)",
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
