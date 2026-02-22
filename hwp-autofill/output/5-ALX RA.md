# 5-ALX RA - HWP 자동입력 매크로

## 사용법
1. 한글(HWP/HWPX) 문서를 엽니다
2. 도구 > 스크립트 매크로 에서 아래 코드를 붙여넣고 실행합니다

## 매크로 코드

```javascript
function OnScriptMacro_자동입력매크로() {
  // 치환 맵: 값 중 줄바꿈은 \r 로 표기 (한글에서 문단 구분)
  var map = {
    "{{edu_title}}": "규제·인허가 AI 자동화 실무 (18h)",
    "{{edu_cate01}}": "20.정보통신",
    "{{edu_cate02}}": "01.정보기술",
    "{{edu_cate03}}": "07.인공지능 ",
    "{{edu_cate04}}": "07.생성형AI엔지니어링",
    "{{edu_cate05}}": "2001070707_25v1",
    "{{edu_ncslevel}}": "5",
    "{{edu_time}}": "18시간( 3일)",
    "{{edu_target}}": "의료기기 개발·제조 기업의 인허가(RA) 담당자 및 규제대응 관련 임직원",
    "{{edu_job}}": "의료기기 인허가(RA), 규제대응, 기술문서(TD) 작성, 품질관리(QA) 등",
    "{{edu_limit}}": "20명",
    "{{edu_feature}}": "의료기기 인허가(RA) 담당자를 대상으로 생성형 AI(ChatGPT, Claude)를 활용하여 규정 문서 분석, 규제 요구사항 체크리스트 자동 생성, 기술문서(TD) 초안 자동 작성, 기존 문서와 최신 규정 간 Gap 분석, Deficiency 대응 문장 자동 생성, 규정 변경 영향 분석 자동화, RA 업무 AI 워크플로 설계까지 다루는 AI 전환(AX) 심화 과정으로, 실제 RA 업무 시나리오 기반 실습 중심의 교육을 통해 인허가 업무 혁신 역량을 강화하는 신기술·융복합 훈련과정",
    "{{edu_summary}}": "생성형 AI(ChatGPT)로 규정 문서의 핵심을 빠르게 파악하는 방법을 학습하고, ChatGPT·Claude Cowork·Excel for Claude를 활용하여 규제 요구사항을 구조화하고 체크리스트를 자동 생성한다. 기술문서(TD) 초안 자동 작성 및 템플릿화를 실습하고, Excel for Claude를 활용하여 기존 문서와 최신 규정 간 Gap을 자동 도출한다. ChatGPT를 활용한 Deficiency 대응 문장 자동 생성, Claude Cowork·Excel for Claude·n8n을 활용한 규정 변경 영향 분석 자동화를 실습하며, 최종적으로 RA 업무 전반의 AI 워크플로를 설계하고 템플릿을 구축한다.",
    "{{edu_ncsreason}}": "본 훈련과정은 의료기기 인허가(RA) 현장의 규제 문서 자동화 AI 전환(AX) 수요에 맞춰 RA 업무 전반의 AI 활용 역량 강화를 목적으로 설계된 과정으로, 기존 NCS 분류체계에 정확히 부합하는 능력단위가 부재하여 산업 현장 맞춤형 커리큘럼으로 자체 구성함",
    "{{edu_goal}}": "의료기기 인허가(RA) 담당자가 생성형 AI(ChatGPT, Claude)와 자동화 도구(Excel for Claude, Claude Cowork, n8n)를 활용하여 규정 문서 분석, 규제 체크리스트 자동 생성, 기술문서(TD) 초안 작성, Gap 분석, Deficiency 대응, 규정 변경 영향 분석, RA 업무 워크플로 설계까지 인허가 업무 전 과정에 AI를 효과적으로 적용할 수 있는 실무 역량을 습득하는 것을 목표로 함",
    "{{edu_guidegoal}}": "의료기기 규제·인허가 업무의 AI 활용 자동화 방법론을 명확히 이해하고, 실습을 통해 생성형 AI 기반 규제 문서 분석·작성·검증 능력을 키워 RA 업무 현장에서 반복적인 규제 대응 업무 시간을 획기적으로 단축하고 문서 정확성을 향상시킬 수 있는 실무 문제 해결 능력을 갖추어 업무 효율성을 높입니다.",
    "{{edu_guidegoaldetail}}":
      "* 생성형 AI(ChatGPT)를 활용한 규정 문서 핵심 파악 및 분석 능력 배양\r" +
      "* AI 기반 규제 요구사항 구조화 및 체크리스트 자동 생성 기법 습득\r" +
      "* 기술문서(TD) 초안 자동 작성 및 템플릿화 실습\r" +
      "* 기존 문서와 최신 규정 간 Gap 자동 도출 능력 강화\r" +
      "* Deficiency 대응 문장 자동 생성 및 규정 변경 영향 분석 자동화 실습\r" +
      "* RA 업무 AI 워크플로 설계 및 템플릿 구축 역량 함양",
    "{{edu_guidegoaldetail-1}}":
      "[규정 문서 AI 분석과 규제 체크리스트 자동화]\r" +
      "- 생성형 AI(ChatGPT)를 활용한 규정 문서 핵심 파악 및 분석\r" +
      "- AI 기반 규제 요구사항 구조화 및 체크리스트 자동 생성",
    "{{edu_guidegoaldetail-2}}":
      "[TD 자동 작성 및 Gap·Deficiency 대응]\r" +
      "- 기술문서(TD) 초안 자동 작성 및 템플릿화 실습\r" +
      "- 기존 문서–최신 규정 Gap 자동 도출 및 Deficiency 대응 문장 생성",
    "{{edu_guidegoaldetail-3}}":
      "[규정 변경 영향 분석 및 RA 워크플로 구축]\r" +
      "- 규정 변경 영향 분석 자동화 (Claude Cowork, Excel for Claude, n8n)\r" +
      "- RA 업무 AI 워크플로 설계 및 템플릿 구축",
    "{{edu_learnhow}}":
      "강의: 슬라이드 및 의료기기 인허가 규제 사례 자료를 활용하여 RA 업무 AI 자동화 방법론을 시각적으로 설명\r" +
      "실습: ChatGPT·Claude·Excel for Claude·Claude Cowork를 활용한 규정 분석·TD 초안 작성·Gap 도출·Deficiency 대응·규정 변경 영향 분석 실습, n8n 기반 RA 워크플로 설계 실습, 최종 템플릿 구축 프로젝트 수행\r" +
      "토론: 의료기기 인허가 현장의 규제 대응 AI 활용 방안에 대한 그룹 토론을 통해 실무 적용 능력 배양\r" +
      "Q&A: 실시간 질문을 통해 이해도 점검 및 피드백 제공",
    "{{edu_testhow}}":
      "가. 평가시점 : 교과목 수업 종료시\r" +
      "나. 평가내용 \r" +
      "• 생성형 AI(ChatGPT, Claude)를 활용한 규제 문서 분석 및 자동 작성 능력\r" +
      "• 기술문서(TD) 초안 자동 작성 및 Gap 분석 능력\r" +
      "• RA 업무 AI 워크플로 설계 및 템플릿 구축 능력\r" +
      "다. 평가방법\r" +
      "• 결과평가 : 최종 산출물(RA 워크플로 설계서, TD 템플릿, 규제 체크리스트) 제출 및 구두발표",
    "{{edu_book}}": "자체교재",
    "{{edu_needreason}}": "의료기기 인허가(RA) 담당자들의 경우 규정 문서 분석, 기술문서(TD) 작성, 규제 변경 대응 등 반복적이고 정밀한 문서 업무에 많은 시간을 소요하며, 최신 규정과의 Gap 분석에 어려움을 겪는 경우가 많음. 또한 관련 직무의 수요조사 결과 AI를 활용한 규제 문서 자동화 교육의 필요성이 제기됨. 본 과정은 의료기기 인허가 현장에서 필요한 규제 문서 분석·작성·검증 자동화 역량을 배양하여 RA 업무 전반의 AI 워크플로를 구축하며, 규제 대응 업무 시간을 획기적으로 단축하여 업무의 프로세스와 효율을 높일 수 있다",
    "{{edu_curri}}": "생성형 AI(ChatGPT)를 활용하여 규정 문서의 핵심을 빠르게 파악하고, ChatGPT·Claude Cowork·Excel for Claude를 활용하여 규제 요구사항을 구조화하고 체크리스트를 자동 생성한다. 기술문서(TD) 초안 자동 작성 및 템플릿화, 기존 문서와 최신 규정 간 Gap 자동 도출, Deficiency 대응 문장 자동 생성을 실습하며, Claude Cowork·n8n을 활용한 규정 변경 영향 분석 자동화를 구현한다. 최종적으로 RA 업무 전반의 AI 워크플로를 설계하고 템플릿을 구축하여 인허가 업무 자동화 역량을 강화한다.",
    "{{edu_edutime}}": "18시간 (100%)",
    "{{time_day_1}}": "6",
    "{{time_day_2}}": "6",
    "{{time_day_3}}": "6",
    "{{time_day_4}}": "0",
    "{{time_day_5}}": "0",
    "{{topic_day_1}}": "ChatGPT를 활용하여 의료기기 규정 문서의 핵심을 빠르게 파악하는 방법을 학습하고, 주요 규제 요구사항을 추출·요약하는 실습을 진행한다. ChatGPT와 Claude Cowork를 활용하여 규제 요구사항을 구조화하고, Excel for Claude를 활용하여 체크리스트를 자동 생성하는 실습을 수행한다. 오후에는 기술문서(TD) 초안 자동 작성과 템플릿화의 기초를 실습하여 규제 문서 AI 자동화의 토대를 다진다.",
    "{{topic_day_2}}": "Excel for Claude를 활용하여 기존 문서와 최신 규정 간 Gap을 자동으로 도출하는 방법을 학습하고, 실제 의료기기 규정 변경 사례를 적용한 Gap 분석 실습을 진행한다. ChatGPT를 활용한 Deficiency 대응 문장 자동 생성을 기초부터 실제 심사 지적 사례까지 심화 실습하며, Claude Cowork·Excel for Claude·n8n을 활용한 규정 변경 영향 분석 자동화의 설계와 기초 연계 실습을 수행한다.",
    "{{topic_day_3}}": "ChatGPT·Claude Cowork·n8n을 활용하여 RA 업무 전반의 AI 워크플로를 설계하고, n8n 기반 업무 자동화 파이프라인을 구축하는 실습을 진행한다. 3일간의 학습 내용을 종합하여 TD 템플릿, 규제 체크리스트, RA 워크플로 설계서를 최종 산출물로 완성하고 팀별 발표를 통해 결과를 공유한다. 종합 피드백과 함께 현업에서의 RA AI 자동화 적용 전략을 수립한다.",
    "{{topic_day_4}}": "0",
    "{{topic_day_5}}": "0",
    "{{edu_future-Basic-1}}": "Lv.1 - 의료·바이오 AI 리터러시 입문",
    "{{edu_future-Basic-2}}": "Lv.2 - 의료·바이오 데이터리터러시와 데이터시각화",
    "{{edu_future-Basic-3}}": "Lv.2 - AI 워크플로우 설계 기초",
    "{{edu_future-Advance-4}}": "Lv.3 - ISO 13485 기반 QMS 반복문서 AI 자동화 구현",
    "{{edu_future-Advance-5}}": "Lv.3 - 규제·인허가 AI 자동화 실무 (본 과정)",
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
