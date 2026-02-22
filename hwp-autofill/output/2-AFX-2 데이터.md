# 2-AFX-2 데이터 - HWP 자동입력 매크로

## 사용법
1. 한글(HWP/HWPX) 문서를 엽니다
2. 도구 > 스크립트 매크로 에서 아래 코드를 붙여넣고 실행합니다

## 매크로 코드

```javascript
function OnScriptMacro_자동입력매크로() {
  // 치환 맵: 값 중 줄바꿈은 \r 로 표기 (한글에서 문단 구분)
  var map = {
    "{{edu_title}}": "의료·바이오 데이터리터러시와 데이터시각화 (6h)",
    "{{edu_cate01}}": "20.정보통신",
    "{{edu_cate02}}": "01.정보기술",
    "{{edu_cate03}}": "07.인공지능 ",
    "{{edu_cate04}}": "07.생성형AI엔지니어링",
    "{{edu_cate05}}": "2001070701_25v1",
    "{{edu_ncslevel}}": "7",
    "{{edu_time}}": "6시간( 1일)",
    "{{edu_target}}": "의료기기 개발·제조 기업 임직원 중 데이터 분석과 AI 활용에 관심이 있는 전 직군 (품질, RA, R&D, 생산, 영업, 경영지원 등)",
    "{{edu_job}}": "데이터 분석이 필요한 전 직무",
    "{{edu_limit}}": "20명",
    "{{edu_feature}}": "의료기기 산업 종사자를 대상으로 데이터리터러시의 기본 개념부터 AI를 활용한 데이터 수집·전처리·시각화·리포트 제작까지 다루는 AI 전환(AX) 데이터 활용 과정으로, 의료기기 분야 실제 데이터 사례와 실습 중심의 교육을 통해 데이터 기반 의사결정 역량을 강화하는 신기술·융복합 훈련과정",
    "{{edu_summary}}": "의료·바이오 분야의 데이터리터러시 개념을 이해하고, ChatGPT·Claude·Gemini를 활용한 데이터 수집 방법을 학습한다. Excel과 Excel for Claude를 활용하여 비정형 의료기기 데이터를 정형화하는 전처리 기법을 익히고, ChatGPT와 Tableau를 활용한 데이터시각화 기초를 배운다. 최종적으로 의료기기 분야 데이터 분석 리포트를 직접 제작하는 실습을 수행한다.",
    "{{edu_ncsreason}}": "본 훈련과정은 의료기기 산업 현장의 데이터 기반 AI 전환(AX) 수요에 맞춰 데이터리터러시 및 시각화 역량 강화를 목적으로 설계된 과정으로, 기존 NCS 분류체계에 정확히 부합하는 능력단위가 부재하여 산업 현장 맞춤형 커리큘럼으로 자체 구성함",
    "{{edu_goal}}": "의료기기 산업 종사자가 데이터리터러시의 개념을 이해하고, 생성형 AI(ChatGPT, Claude, Gemini)와 Tableau 등 도구를 활용하여 의료기기 데이터의 수집·전처리·시각화·리포트 제작까지 전 과정을 수행할 수 있는 데이터 활용 역량을 습득하는 것을 목표로 함",
    "{{edu_guidegoal}}": "의료기기 분야의 데이터 특성과 활용 사례를 명확히 이해하고, AI 도구를 활용한 데이터 수집·전처리·시각화 실습을 통해 데이터 기반 의사결정 능력을 키워 의료기기 업무 현장에 바로 적용할 수 있는 실무 문제 해결 능력을 갖추어 업무 효율성을 높입니다.",
    "{{edu_guidegoaldetail}}":
      "* 의료·바이오 분야 데이터리터러시의 개념과 중요성 이해\r" +
      "* 생성형 AI(ChatGPT, Claude, Gemini)를 활용한 데이터 수집 기법 습득\r" +
      "* Excel과 Excel for Claude를 활용한 비정형 데이터 전처리 능력 배양\r" +
      "* ChatGPT와 Tableau를 활용한 데이터시각화 기초 역량 강화\r" +
      "* 의료기기 분야 데이터 분석 리포트 제작 실습을 통한 종합 역량 함양",
    "{{edu_guidegoaldetail-1}}":
      "[데이터리터러시와 AI 기반 데이터 수집]\r" +
      "- 의료·바이오 데이터리터러시의 개념과 의료기기 데이터 특성 이해\r" +
      "- AI(ChatGPT/Claude/Gemini)를 활용한 데이터 수집 방법론",
    "{{edu_guidegoaldetail-2}}":
      "[데이터 전처리 및 시각화]\r" +
      "- Excel과 Excel for Claude를 활용한 비정형 데이터 정형화 전처리\r" +
      "- ChatGPT와 Tableau를 활용한 데이터시각화 기초",
    "{{edu_guidegoaldetail-3}}":
      "[데이터 분석 리포트 제작]\r" +
      "- ChatGPT와 Tableau를 활용한 의료기기 데이터 분석 리포트 제작\r" +
      "- 데이터 기반 의사결정 및 리포트 발표 실습",
    "{{edu_learnhow}}":
      "강의: 슬라이드 및 의료기기 데이터 분석 사례 자료를 활용하여 데이터리터러시의 개념과 활용 방법을 시각적으로 설명\r" +
      "실습: ChatGPT·Claude·Gemini를 활용한 데이터 수집, Excel·Excel for Claude를 활용한 전처리, Tableau를 활용한 시각화 및 리포트 제작 실습\r" +
      "토론: 의료기기 업무 현장의 실제 데이터 활용 사례를 기반으로 그룹 토론을 통해 실무 적용 능력 배양\r" +
      "Q&A: 실시간 질문을 통해 이해도 점검 및 피드백 제공",
    "{{edu_testhow}}":
      "가. 평가시점 : 교과목 수업 종료시\r" +
      "나. 평가내용 \r" +
      "• AI 도구(ChatGPT, Claude, Gemini)를 활용한 데이터 수집 능력\r" +
      "• Excel 및 AI를 활용한 데이터 전처리 능력\r" +
      "• Tableau를 활용한 데이터시각화 및 리포트 제작 능력\r" +
      "다. 평가방법\r" +
      "• 결과평가 : 데이터 분석 리포트 제출 및 구두발표",
    "{{edu_book}}": "자체교재",
    "{{edu_needreason}}": "의료기기 산업 종사자들의 경우 업무에서 다양한 데이터를 다루지만 체계적인 데이터 분석·시각화 역량이 부족하여 데이터 기반 의사결정에 어려움을 겪는 경우가 많음. 또한 관련 직무의 수요조사 결과 AI를 활용한 데이터 분석 및 시각화 교육의 필요성이 제기됨. 본 과정은 의료기기 산업 현장에서 필요한 데이터리터러시를 배양하여 AI 도구를 활용한 데이터 수집·전처리·시각화·리포트 제작 역량을 높이며, 데이터 기반 의사결정을 통해 업무의 프로세스와 효율을 높일 수 있다",
    "{{edu_curri}}": "의료·바이오 분야의 데이터리터러시 개념과 중요성을 이해하고, ChatGPT·Claude·Gemini를 활용한 데이터 수집 기법을 학습한다. Excel과 Excel for Claude를 활용하여 비정형 의료기기 데이터를 정형화하는 전처리 기법을 익히고, ChatGPT와 Tableau를 활용한 데이터시각화 기초 역량을 배양한다. 최종적으로 의료기기 분야 데이터 분석 리포트를 직접 제작하는 실습을 통해 데이터 기반 업무 수행 능력을 강화한다.",
    "{{edu_edutime}}": "6시간 (100%)",
    "{{time_day_1}}": "6",
    "{{time_day_2}}": "0",
    "{{time_day_3}}": "0",
    "{{time_day_4}}": "0",
    "{{time_day_5}}": "0",
    "{{topic_day_1}}": "의료·바이오 분야 데이터리터러시의 개념과 의료기기 데이터의 특성을 이해한 후, ChatGPT·Claude·Gemini를 활용하여 의료기기 관련 데이터를 직접 수집하는 실습을 진행한다. Excel과 Excel for Claude를 활용하여 비정형 의료기기 데이터를 정형화하는 전처리 기법을 실습하고, ChatGPT와 Tableau를 활용한 데이터시각화 기초를 배운다. 최종적으로 의료기기 분야 데이터를 활용한 분석 리포트를 직접 제작하고 발표하여 데이터 기반 의사결정 역량을 함양한다.",
    "{{topic_day_2}}": "0",
    "{{topic_day_3}}": "0",
    "{{topic_day_4}}": "0",
    "{{topic_day_5}}": "0",
    "{{edu_future-Basic-1}}": "Lv.1 - 의료·바이오 AI 리터러시 입문",
    "{{edu_future-Basic-2}}": "Lv.2 - 의료·바이오 데이터리터러시와 데이터시각화 (본 과정)",
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
