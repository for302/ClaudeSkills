# Company Analysis Framework

This document provides guidelines for analyzing companies and extracting relevant information from web searches.

## Analysis Categories

### 1. Business Areas and Main Products/Services
**사업 분야 및 주요 제품/서비스**

**What to look for:**
- Core business domains and industry sectors
- Main product lines or service offerings
- Key technologies or platforms used
- Business model (B2B, B2C, B2G, etc.)

**Information sources:**
- Company homepage "About" or "Products" sections
- Company introduction pages
- Product catalogs
- Press releases about new products/services

**Output format:**
Concise 2-3 sentence summary focusing on the most important products/services and business areas.

Example: "AI 기반 데이터 분석 플랫폼 개발 전문 기업. 주요 제품으로 실시간 빅데이터 분석 솔루션과 예측 분석 엔진을 제공하며, 금융 및 제조 산업 대상 B2B 사업 운영."

---

### 2. Main Customers and Market Status
**주요 고객 및 시장 현황**

**What to look for:**
- Target customer segments (industries, company sizes)
- Major clients or partnerships (if publicly disclosed)
- Market positioning (leader, challenger, niche player)
- Customer base size or market share (if available)

**Information sources:**
- Case studies or client testimonials
- Partnership announcements
- News about major contracts
- Investor relations materials

**Output format:**
2-3 sentences describing target customers and market position.

Example: "주요 고객은 국내 대기업 및 공공기관으로, 삼성전자, LG전자 등과 장기 공급 계약 체결. 국내 B2B 데이터 분석 시장에서 점유율 15%로 3위 업체."

---

### 3. Domestic Market Status
**관련 사업분야 시장 현황(국내)**

**What to look for:**
- Overall domestic market size and growth rate
- Key trends in the industry
- Competitive landscape in Korea
- Regulatory environment or government policies

**Information sources:**
- Industry reports and market research
- News articles about the industry
- Government statistics or publications
- Industry association reports

**Output format:**
2-3 sentences about the domestic market size, trends, and competitive environment.

Example: "국내 데이터 분석 시장은 2024년 기준 3.5조원 규모로 연평균 12% 성장 중. AI 기술 발전과 디지털 전환 가속화로 수요 급증. 주요 경쟁사로 SK C&C, 삼성SDS 등 대기업 계열사와 다수 스타트업 존재."

---

### 4. Global Market Status
**관련 사업분야 시장 현황(글로벌)**

**What to look for:**
- Global market size and growth projections
- International trends and innovations
- Major global competitors
- Regional market differences

**Information sources:**
- International market research reports
- Global industry news
- Analyst reports (Gartner, IDC, etc.)
- Trade publications

**Output format:**
2-3 sentences about global market trends and major players.

Example: "글로벌 데이터 분석 시장은 2024년 2,800억 달러 규모로 연평균 15% 성장 전망. Tableau, Power BI, Qlik 등 글로벌 선도 기업들이 시장 주도. 클라우드 기반 분석과 AI 통합이 주요 트렌드."

---

### 5. Technology Capability
**기술 역량 (Technology Capability)**

**What to look for:**
- Core technologies and technical expertise
- Patents or intellectual property
- R&D investments or innovation initiatives
- Technical certifications or standards compliance
- Technology partnerships or collaborations

**Information sources:**
- Company technology pages
- Patent databases
- R&D announcements
- Technical white papers or case studies
- Technology partnerships

**Output format:**
2-3 sentences highlighting key technical capabilities and innovations.

Example: "머신러닝 및 딥러닝 알고리즘 자체 개발 역량 보유. 실시간 대용량 데이터 처리 관련 특허 5건 등록. AWS, Google Cloud와 기술 파트너십 체결하여 클라우드 네이티브 솔루션 제공."

---

### 6. Awards and Recognition
**수상실적**

**What to look for:**
- Industry awards and recognitions
- Government certifications or designations
- Innovation prizes
- Quality or excellence awards
- Dates and awarding organizations

**Information sources:**
- Company news or press releases
- Awards sections on company website
- Industry publications
- Government databases (e.g., Innobiz, Venture certification)

**Output format:**
Bullet-point list or comma-separated list of major awards with years.

Example: "2024 AI 혁신대상 수상, 2023 벤처기업 인증, 2022 중소벤처기업부 기술혁신형 중소기업(Inno-Biz) 선정, 2021 Good Software 인증"

---

### 7. News and Updates Summary
**뉴스 및 소식에 대한 전체적은 요약 내용**

**What to look for:**
- Recent news articles (past 6-12 months)
- Major announcements or milestones
- Product launches or updates
- Funding rounds or financial news
- Strategic initiatives or expansions
- Any controversies or challenges

**Information sources:**
- Company press releases
- News websites and business publications
- Industry media
- Company blog or social media

**Output format:**
Comprehensive 3-5 sentence summary of recent developments and current status.

Example: "2024년 상반기 시리즈 B 투자 유치로 총 150억원 조달 성공. 5월 신제품 'DataViz Pro 3.0' 출시하며 시장 반응 긍정적. 7월 베트남 법인 설립으로 동남아 시장 진출 시작. 최근 금융권 대상 AI 윤리 및 보안 강화 업데이트 발표. 올해 매출 200% 성장 목표."

---

## General Guidelines

### Search Strategy

1. **Start with official sources:**
   - Company website (especially About, Products, News sections)
   - Official social media or blog
   - Press releases

2. **Use reliable secondary sources:**
   - Major news outlets and business publications
   - Industry-specific media
   - Market research reports
   - Government databases

3. **Verify information:**
   - Cross-check facts across multiple sources
   - Prefer recent information (within 1-2 years)
   - Note the date of information when possible

### When Information is Not Available

- Leave the field blank (as per user preference)
- Do not fabricate or guess information
- Move on to next company

### Language and Tone

- Use Korean language for all outputs
- Be concise and factual
- Avoid marketing language or subjective opinions
- Focus on verifiable facts and figures

### Formatting

- Keep each field's content within 300-500 characters
- Use clear, professional language
- Include specific numbers, dates, and names where available
- Avoid redundancy across different fields
