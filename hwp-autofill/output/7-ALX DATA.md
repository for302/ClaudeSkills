# 7-ALX DATA - HWP 자동입력 매크로

## 사용법
1. 한글(HWP/HWPX) 문서를 엽니다
2. 도구 > 스크립트 매크로 에서 아래 코드를 붙여넣고 실행합니다

## 매크로 코드

```javascript
function OnScriptMacro_자동입력매크로() {
  // 치환 맵: 값 중 줄바꿈은 \r 로 표기 (한글에서 문단 구분)
  var map = {
    "{{edu_title}}": "의료기기 통합 데이터 기반 KPI 대시보드 및 AI 자동 리포팅 구축 (18h)",
    "{{edu_cate01}}": "20.정보통신",
    "{{edu_cate02}}": "01.정보기술",
    "{{edu_cate03}}": "07.인공지능 ",
    "{{edu_cate04}}": "07.생성형AI엔지니어링",
    "{{edu_cate05}}": "2001070707_25v1",
    "{{edu_ncslevel}}": "5",
    "{{edu_time}}": "18시간( 3일)",
    "{{edu_target}}": "의료기기 개발·제조 기업의 데이터 분석·활용 담당자 및 KPI 대시보드 구축에 관심이 있는 임직원 (품질, R&D, 생산, 경영지원 등)",
    "{{edu_job}}": "의료기기 품질관리, 연구개발(R&D), 생산관리, 경영지원, 데이터 분석 등",
    "{{edu_limit}}": "20명",
    "{{edu_feature}}": "의료기기 산업 종사자를 대상으로 품질·임상·공정 데이터의 구조를 이해하고, 코드작성 없이 AI(ChatGPT, Claude Code)를 활용하여 Python/Pandas 기반 데이터 정제부터 바이브코딩 KPI 자동 계산, Claude Code·Streamlit 기반 KPI 대시보드 구현, GPT 기반 KPI 자동 해석, 통합 AI 워크플로 구축까지 다루는 AI 전환(AX) 최고급 과정으로, 의료기기 규제(ISO 13485, MFDS, FDA) 기준을 반영한 데이터 기반 의사결정 역량을 강화하는 신기술·융복합 훈련과정",
    "{{edu_summary}}": "의료기기 품질·임상·공정 데이터 구조를 이해하고 직무별 데이터 흐름을 분석한다. ISO 13485·MFDS·FDA 기준을 반영한 통합 KPI 체계를 설계하고, 코드작성 없이 ChatGPT·Claude Code를 활용하여 Python/Pandas 기반 데이터 정제·구조화를 실습한다. 바이브코딩으로 KPI 자동 계산 코드를 생성하고, Claude Code·Streamlit 기반 KPI 대시보드를 설계·구현하며 부서 통합 데이터 시각화와 인터랙티브 기능을 구현한다. ChatGPT·Claude Code 기반 KPI 자동 해석 코멘트 생성과 분석 자동화를 실습하고, 최종적으로 데이터 수집부터 AI 코멘트·자동 리포트까지 통합 AI 워크플로를 구축한다.",
    "{{edu_ncsreason}}": "본 훈련과정은 의료기기 산업 현장의 데이터 기반 의사결정 및 AI 자동 리포팅 전환(AX) 수요에 맞춰 KPI 대시보드 및 AI 워크플로 구축 역량 강화를 목적으로 설계된 과정으로, 기존 NCS 분류체계에 정확히 부합하는 능력단위가 부재하여 산업 현장 맞춤형 커리큘럼으로 자체 구성함",
    "{{edu_goal}}": "의료기기 산업 종사자가 품질·임상·공정 데이터의 구조를 이해하고, 코드작성 없이 ChatGPT·Claude Code를 활용한 바이브코딩으로 Python/Pandas 기반 데이터 정제 및 KPI 자동 계산 코드를 생성하고, Claude Code·Streamlit 기반 KPI 대시보드를 구축하며, 규제 기준(ISO 13485, MFDS, FDA)을 반영한 데이터 수집부터 AI 자동 리포트까지 통합 워크플로를 직접 구축할 수 있는 데이터 파이프라인 구축 역량을 습득하는 것을 목표로 함",
    "{{edu_guidegoal}}": "의료기기 데이터 구조와 KPI 체계의 설계 방법론을 명확히 이해하고, 코드작성 없이 ChatGPT·Claude Code를 활용한 실습을 통해 데이터 정제·KPI 계산·대시보드 구현·AI 자동 해석 능력을 키워, 의료기기 업무 현장에서 데이터 기반 의사결정 시간을 획기적으로 단축하고 리포팅 품질을 향상시킬 수 있는 실무 문제 해결 능력을 갖추어 업무 효율성을 높입니다.",
    "{{edu_guidegoaldetail}}":
      "* 의료기기 품질·임상·공정 데이터 구조 이해 및 직무별 데이터 흐름 분석\r" +
      "* ISO 13485·MFDS·FDA 기준 반영 통합 KPI 체계 설계 및 의사결정 구조 수립\r" +
      "* 코드작성 없이 AI를 활용하여 Python/Pandas 기반 데이터 정제·구조화 및 바이브코딩 KPI 자동 계산 실습\r" +
      "* Streamlit 기반 KPI 대시보드 설계·구현 및 인터랙티브 시각화 실습\r" +
      "* GPT 기반 KPI 자동 해석 코멘트 생성 및 분석 자동화 실습\r" +
      "* 데이터 수집→정제→KPI→시각화→AI 코멘트→자동 리포트 통합 워크플로 구축 역량 함양",
    "{{edu_guidegoaldetail-1}}":
      "[데이터 구조·KPI 설계 및 AI 활용 데이터 정제·KPI 자동 계산]\r" +
      "- 의료기기 품질·임상·공정 데이터 구조 이해 및 KPI 체계 설계\r" +
      "- 코드작성 없이 ChatGPT·Claude Code로 Python/Pandas 데이터 정제 및 바이브코딩 KPI 자동 계산",
    "{{edu_guidegoaldetail-2}}":
      "[Claude Code·Streamlit 대시보드 및 GPT 기반 자동 해석]\r" +
      "- Claude Code·Streamlit 기반 KPI 대시보드 설계·구현 및 인터랙티브 시각화\r" +
      "- ChatGPT·Claude Code 기반 KPI 자동 해석 코멘트 생성 및 분석 자동화",
    "{{edu_guidegoaldetail-3}}":
      "[통합 AI 워크플로 구축 및 최종 산출물]\r" +
      "- 데이터 수집→정제→KPI→시각화→AI 코멘트→자동 리포트 통합 워크플로 구축 (Claude Code, Python, Streamlit, ChatGPT API, Claude API)\r" +
      "- 최종 산출물: KPI 대시보드 앱, AI 자동 리포트, 통합 워크플로",
    "{{edu_learnhow}}":
      "강의: 슬라이드 및 의료기기 데이터 분석·KPI 대시보드 사례 자료를 활용하여 데이터 구조·KPI 체계·AI 자동화 방법론을 시각적으로 설명\r" +
      "실습: 코드작성 없이 ChatGPT·Claude Code를 활용한 Python/Pandas 데이터 정제, 바이브코딩 KPI 자동 계산 코드 생성, Claude Code·Streamlit 대시보드 구현, GPT 기반 자동 해석, 통합 AI 워크플로 구축 실습, 최종 산출물 완성 프로젝트 수행\r" +
      "토론: 의료기기 업무 현장의 데이터 기반 의사결정 및 AI 리포팅 활용 방안에 대한 그룹 토론을 통해 실무 적용 능력 배양\r" +
      "Q&A: 실시간 질문을 통해 이해도 점검 및 피드백 제공",
    "{{edu_testhow}}":
      "가. 평가시점 : 교과목 수업 종료시\r" +
      "나. 평가내용 \r" +
      "• ChatGPT·Claude Code를 활용한 Python/Pandas 데이터 정제 및 바이브코딩 KPI 자동 계산 능력\r" +
      "• Claude Code·Streamlit 기반 KPI 대시보드 설계·구현 능력\r" +
      "• GPT 기반 KPI 자동 해석 및 통합 AI 워크플로 구축 능력\r" +
      "다. 평가방법\r" +
      "• 결과평가 : 최종 산출물(KPI 대시보드 앱, AI 자동 리포트 시스템, 통합 워크플로) 제출 및 구두발표",
    "{{edu_book}}": "자체교재",
    "{{edu_needreason}}": "의료기기 산업 종사자들의 경우 품질·임상·공정 등 부서별 데이터가 분산되어 있어 통합적인 데이터 기반 의사결정에 어려움을 겪으며, KPI 리포팅에 과도한 시간을 소요하는 경우가 많음. 또한 관련 직무의 수요조사 결과 AI를 활용한 데이터 파이프라인 및 자동 리포팅 교육의 필요성이 제기됨. 본 과정은 의료기기 산업 현장에서 필요한 통합 데이터 기반 KPI 대시보드 및 AI 자동 리포팅 구축 역량을 배양하여 데이터 수집부터 AI 코멘트·자동 리포트까지 통합 워크플로를 구축하며, 데이터 기반 의사결정 시간을 획기적으로 단축하여 업무의 프로세스와 효율을 높일 수 있다",
    "{{edu_curri}}": "의료기기 품질·임상·공정 데이터 구조를 이해하고 직무별 데이터 흐름을 분석한 후, ISO 13485·MFDS·FDA 기준을 반영한 통합 KPI 체계를 설계한다. 코드작성 없이 ChatGPT·Claude Code를 활용하여 Python/Pandas 기반 데이터 정제·구조화를 실습하고, 바이브코딩으로 KPI 자동 계산 코드를 생성한다. Streamlit 기반 KPI 대시보드를 설계·구현하고 인터랙티브 시각화 기능을 구현하며, GPT 기반 KPI 자동 해석 코멘트 생성을 실습하여 데이터 수집부터 AI 자동 리포트까지 통합 워크플로를 구축한다.",
    "{{edu_edutime}}": "18시간 (100%)",
    "{{time_day_1}}": "6",
    "{{time_day_2}}": "6",
    "{{time_day_3}}": "6",
    "{{time_day_4}}": "0",
    "{{time_day_5}}": "0",
    "{{topic_day_1}}": "의료기기 품질·임상·공정 데이터의 구조를 이해하고 직무별 데이터 흐름을 분석한 후, ISO 13485·MFDS·FDA 기준을 반영한 통합 KPI 체계를 설계하고 규제 기반 의사결정 구조를 수립한다. 코드작성 없이 ChatGPT·Claude Code를 활용하여 Python/Pandas 기반 데이터 정제·구조화를 실습하고, 바이브코딩을 통해 KPI 자동 계산 코드를 생성·검증하는 실습을 진행한다.",
    "{{topic_day_2}}": "ChatGPT를 활용하여 Claude Code·Streamlit 기반 KPI 대시보드를 설계하고 실제 앱을 구현하는 실습을 진행한다. Claude Code·Streamlit·Pandas로 부서 통합 데이터 시각화와 필터·드릴다운·동적 차트 등 인터랙티브 기능을 구현한 후, ChatGPT·Claude Code를 활용하여 GPT 기반 KPI 자동 해석 코멘트 생성과 분석 자동화를 실습하여 대시보드에 AI 해석 기능을 통합한다.",
    "{{topic_day_3}}": "데이터 수집부터 정제→KPI 계산→시각화→AI 코멘트→자동 리포트까지 연결되는 통합 AI 워크플로를 설계하고, ChatGPT API·Claude API를 연동하여 Claude Code·Python·Streamlit 기반 통합 시스템을 구축하는 실습을 진행한다. 3일간의 학습 내용을 종합하여 KPI 대시보드 앱, AI 자동 리포트 시스템, 통합 워크플로를 최종 산출물로 완성하고 팀별 발표를 통해 결과를 공유한다.",
    "{{topic_day_4}}": "0",
    "{{topic_day_5}}": "0",
    "{{edu_future-Basic-1}}": "Lv.1 - 의료·바이오 AI 리터러시 입문",
    "{{edu_future-Basic-2}}": "Lv.2 - 의료·바이오 데이터리터러시와 데이터시각화",
    "{{edu_future-Basic-3}}": "Lv.2 - AI 워크플로우 설계 기초",
    "{{edu_future-Advance-4}}": "Lv.3 - ISO 13485 기반 QMS 반복문서 AI 자동화 구현",
    "{{edu_future-Advance-5}}": "Lv.3 - 규제·인허가 AI 자동화 실무",
    "{{edu_future-Advance-6}}": "Lv.4 - 의료기기 설계관리(Design Controls) AI 자동화 실습",
    "{{edu_future-Advance-7}}": "Lv.5 - 의료기기 통합 데이터 기반 KPI 대시보드 및 AI 자동 리포팅 구축 (본 과정)",
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
