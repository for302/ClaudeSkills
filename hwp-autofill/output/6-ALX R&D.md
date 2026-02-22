# 6-ALX R&D - HWP 자동입력 매크로

## 사용법
1. 한글(HWP/HWPX) 문서를 엽니다
2. 도구 > 스크립트 매크로 에서 아래 코드를 붙여넣고 실행합니다

## 매크로 코드

```javascript
function OnScriptMacro_자동입력매크로() {
  // 치환 맵: 값 중 줄바꿈은 \r 로 표기 (한글에서 문단 구분)
  var map = {
    "{{edu_title}}": "의료기기 연구개발 설계 관리 AX 실습 과정 (18h)",
    "{{edu_cate01}}": "20.정보통신",
    "{{edu_cate02}}": "01.정보기술",
    "{{edu_cate03}}": "07.인공지능 ",
    "{{edu_cate04}}": "07.생성형AI엔지니어링",
    "{{edu_cate05}}": "2001070707_25v1",
    "{{edu_ncslevel}}": "5",
    "{{edu_time}}": "18시간( 3일)",
    "{{edu_target}}": "의료기기 개발·제조 기업의 연구개발(R&D) 담당자 및 설계관리(Design Controls) 관련 임직원",
    "{{edu_job}}": "의료기기 연구개발(R&D), 설계관리, 소프트웨어 개발, 위험관리, V&V 등",
    "{{edu_limit}}": "20명",
    "{{edu_feature}}": "의료기기 R&D 담당자를 대상으로 IEC 62304·ISO 14971 기반 설계관리 전주기를 이해하고, 생성형 AI(ChatGPT, Claude, Claude Cowork, Claude Code)와 자동화 도구(Excel, n8n, Google AI Studio)를 활용하여 URS 구조화·SRS 자동 생성·TC 자동 변환·ECO 변경 영향 자동 식별·Traceability 자동 생성까지 설계관리 전 과정의 AI 자동화를 실습하고, 설계 입력부터 변경관리까지 연결된 AI 워크플로를 통합 설계하는 AI 전환(AX) 심화 과정으로, 실제 R&D 업무 시나리오 기반 실습 중심의 신기술·융복합 훈련과정",
    "{{edu_summary}}": "생성형 AI 협업 환경에서의 설계관리 전주기(IEC 62304·ISO 14971)를 이해한 후, Claude·ChatGPT·Claude Cowork를 활용하여 자연어 요구사항을 구조화된 URS로 자동 변환하고 SRS 초안을 자동 생성하며 문서 일관성·논리를 검증한다. ChatGPT·Excel·Google AI Studio를 활용하여 요구사항을 테스트 케이스로 자동 변환하고 표준 문서로 출력하며, Claude Code·n8n을 활용하여 설계 변경 시 영향 항목을 자동 식별하고 알림 체계를 설계한다. Traceability 매트릭스를 AI로 자동 생성하여 누락을 탐지하고, 최종적으로 설계 입력부터 변경관리까지 연결된 AI 기반 설계관리 워크플로를 통합 설계한다.",
    "{{edu_ncsreason}}": "본 훈련과정은 의료기기 R&D 현장의 설계관리(Design Controls) AI 전환(AX) 수요에 맞춰 설계관리 프로세스 전반의 AI 자동화 역량 강화를 목적으로 설계된 과정으로, 기존 NCS 분류체계에 정확히 부합하는 능력단위가 부재하여 산업 현장 맞춤형 커리큘럼으로 자체 구성함",
    "{{edu_goal}}": "의료기기 R&D 담당자가 생성형 AI 협업 환경(ChatGPT, Claude, Claude Cowork, Claude Code)을 활용하여 설계관리 전주기(URS 구조화→SRS 자동 생성→TC 자동 변환→ECO 변경 영향 자동 식별→Traceability 자동 생성)를 AI로 수행하고, n8n·Google AI Studio 기반으로 설계 입력부터 변경관리까지 연결된 통합 워크플로를 직접 설계·구축할 수 있는 설계관리 AX 실무 역량을 습득하는 것을 목표로 함",
    "{{edu_guidegoal}}": "의료기기 설계관리 전주기의 구조를 이해하고, ChatGPT·Claude·Claude Cowork·Claude Code를 활용한 실습을 통해 URS 구조화·SRS 생성·TC 변환·ECO 영향 식별·Traceability 구축 능력을 키워, R&D 업무 현장에서 설계관리 문서화와 검증 시간을 획기적으로 단축하고 AI 기반 통합 워크플로 설계 능력을 갖추어 업무 효율성을 높입니다.",
    "{{edu_guidegoaldetail}}":
      "* 생성형 AI 협업 환경에서의 설계관리 전주기(IEC 62304·ISO 14971) 구조 이해\r" +
      "* Claude·ChatGPT·Claude Cowork를 활용한 URS 구조화 및 자동 도출 실습\r" +
      "* ChatGPT·Claude를 활용한 SRS 초안 자동 생성 및 문서 일관성·논리 검증 실습\r" +
      "* ChatGPT·Excel·Google AI Studio를 활용한 TC 자동 변환 및 표준 문서 출력 실습\r" +
      "* Claude Code·ChatGPT·n8n을 활용한 ECO 변경 영향 자동 식별 및 알림 설계 실습\r" +
      "* Traceability 매트릭스 AI 자동 생성·누락 탐지 및 AI 기반 설계관리 워크플로 통합 설계 역량 함양",
    "{{edu_guidegoaldetail-1}}":
      "[설계관리 전주기 이해 및 AI 기반 URS 구조화·SRS 자동 생성]\r" +
      "- 생성형 AI 협업 환경에서의 설계관리 전주기(IEC 62304·ISO 14971) 구조 이해\r" +
      "- Claude·ChatGPT·Claude Cowork로 URS 자동 구조화 및 SRS 초안 자동 생성·검증 실습",
    "{{edu_guidegoaldetail-2}}":
      "[TC 자동 변환·ECO 변경 영향 자동 식별 실습]\r" +
      "- ChatGPT·Excel·Google AI Studio를 활용한 TC 자동 변환 및 표준 문서 출력 실습\r" +
      "- Claude Code·ChatGPT·Claude Cowork·n8n을 활용한 ECO 변경 영향 자동 식별 및 알림 설계",
    "{{edu_guidegoaldetail-3}}":
      "[Traceability 자동 생성 및 AI 워크플로 통합 설계]\r" +
      "- Claude Code·ChatGPT·Excel·Google AI Studio로 Traceability 매트릭스 자동 생성 및 누락 탐지\r" +
      "- 설계 입력~변경관리 연결 AI 기반 설계관리 워크플로 통합 설계 (ChatGPT, Claude Code, Claude Cowork, n8n)",
    "{{edu_learnhow}}":
      "강의: 슬라이드 및 의료기기 설계관리 사례 자료를 활용하여 IEC 62304·ISO 14971 기반 설계관리 전주기와 AI 협업 환경을 시각적으로 설명\r" +
      "실습: Claude·ChatGPT·Claude Cowork로 URS 구조화 및 SRS 자동 생성, ChatGPT·Excel·Google AI Studio로 TC 자동 변환, Claude Code·n8n으로 ECO 변경 영향 자동 식별 및 알림 설계, Traceability 매트릭스 AI 자동 생성, 설계관리 AI 워크플로 통합 설계 실습, 최종 산출물 완성 프로젝트 수행\r" +
      "토론: 의료기기 R&D 현장의 설계관리 AI 전환 적용 방안에 대한 그룹 토론을 통해 실무 적용 능력 배양\r" +
      "Q&A: 실시간 질문을 통해 이해도 점검 및 피드백 제공",
    "{{edu_testhow}}":
      "가. 평가시점 : 교과목 수업 종료시\r" +
      "나. 평가내용 \r" +
      "• Claude·ChatGPT·Claude Cowork를 활용한 URS 구조화 및 SRS 자동 생성 능력\r" +
      "• ChatGPT·Excel·Google AI Studio를 활용한 TC 자동 변환 및 ECO 변경 영향 자동 식별 능력\r" +
      "• Traceability 매트릭스 AI 자동 생성 및 AI 기반 설계관리 워크플로 통합 설계 능력\r" +
      "다. 평가방법\r" +
      "• 결과평가 : 최종 산출물(설계관리 전주기 AI 자동화 결과물 및 통합 워크플로 설계서) 제출 및 구두발표",
    "{{edu_book}}": "자체교재",
    "{{edu_needreason}}": "의료기기 R&D 담당자들의 경우 설계관리(Design Controls) 전주기에서 요구사항 구조화, SRS 문서 작성, 테스트 케이스 변환, Traceability 매트릭스 관리 등 복잡하고 반복적인 문서화 업무에 많은 시간을 소요하며, 설계 변경 시 영향 범위 파악에 어려움을 겪는 경우가 많음. 또한 관련 직무의 수요조사 결과 AI를 활용한 설계관리 자동화 교육의 필요성이 제기됨. 본 과정은 의료기기 R&D 현장에서 필요한 설계관리 전주기 AI 자동화 역량을 배양하여 설계 입력부터 변경관리까지 연결된 AI 워크플로를 구축하며, 설계관리 문서화와 검증 시간을 획기적으로 단축하여 업무의 프로세스와 효율을 높일 수 있다",
    "{{edu_curri}}": "생성형 AI 협업 환경에서의 설계관리 전주기(IEC 62304·ISO 14971)를 이해하고, Claude·ChatGPT·Claude Cowork를 활용하여 자연어 요구사항(URS)을 구조화하고 SRS 초안을 자동 생성하며 문서 일관성·논리를 검증한다. ChatGPT·Excel·Google AI Studio를 활용하여 요구사항을 테스트 케이스로 자동 변환하고, Claude Code·n8n을 활용하여 설계 변경 시 영향 항목을 자동 식별한다. Traceability 매트릭스를 AI로 자동 생성하여 누락을 탐지하고, 최종적으로 설계 입력부터 변경관리까지 연결된 AI 기반 설계관리 워크플로를 통합 설계한다.",
    "{{edu_edutime}}": "18시간 (100%)",
    "{{time_day_1}}": "6",
    "{{time_day_2}}": "6",
    "{{time_day_3}}": "6",
    "{{time_day_4}}": "0",
    "{{time_day_5}}": "0",
    "{{topic_day_1}}": "IEC 62304·ISO 14971 기반 설계관리 전주기의 구조와 URS–SRS–TC–ECO–Traceability 간 관계를 이해하고, ChatGPT·Claude·Claude Cowork·Claude Code의 도구별 역할을 파악한다. 오후에는 Claude·ChatGPT로 자연어 요구사항을 구조화된 URS로 자동 변환하고 Claude Cowork으로 협업 검토하며, ChatGPT·Claude를 활용하여 SRS 초안을 자동 생성하고 문서 일관성·논리를 검증하는 실습을 진행한다.",
    "{{topic_day_2}}": "ChatGPT로 SRS 기반 검증 가능한 TC를 자동 생성하고 Excel·Google AI Studio 연계로 표준 문서로 출력하는 실습을 진행한다. Claude Code로 설계 변경 시 영향 항목을 자동 식별하고, Claude Cowork·n8n으로 변경 알림 워크플로를 구축하는 실습을 수행한다. 실제 의료기기 설계 변경 시나리오에 AI를 적용하여 ECO 변경 영향 분석을 실습하고, TC 자동화와 ECO 식별 결과를 종합 검토한다.",
    "{{topic_day_3}}": "Claude Code·ChatGPT로 요구–설계–검증–위험 간 Traceability 매트릭스를 AI로 자동 생성하고 Excel·Google AI Studio로 누락을 탐지하는 실습을 진행한다. ChatGPT·Claude Code·Claude Cowork·n8n을 연결하여 설계 입력부터 변경관리까지 통합된 AI 워크플로를 설계하고, 3일간의 산출물을 통합하여 팀별 발표와 피드백을 통해 현업 AX 적용 전략을 수립한다.",
    "{{topic_day_4}}": "0",
    "{{topic_day_5}}": "0",
    "{{edu_future-Basic-1}}": "Lv.1 - 의료·바이오 AI 리터러시 입문",
    "{{edu_future-Basic-2}}": "Lv.2 - 의료·바이오 데이터리터러시와 데이터시각화",
    "{{edu_future-Basic-3}}": "Lv.2 - AI 워크플로우 설계 기초",
    "{{edu_future-Advance-4}}": "Lv.3 - ISO 13485 기반 QMS 반복문서 AI 자동화 구현",
    "{{edu_future-Advance-5}}": "Lv.3 - 규제·인허가 AI 자동화 실무",
    "{{edu_future-Advance-6}}": "Lv.4 - 의료기기 설계관리(Design Controls) AI 자동화 실습 (본 과정)",
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
