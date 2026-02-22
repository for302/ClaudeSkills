---
name: paper-analyzer
description: Academic paper analysis tool that reads PDF research papers and generates structured analysis with Obsidian YAML metadata in Markdown format. Specializes in education, educational psychology, HCI, AI literacy, instructional design, and HRD research. Automatically creates APA7 citations and bilingual (Korean-English) metadata. Use when analyzing academic papers, building Obsidian research vault, or creating literature reviews.
---

# Paper Analyzer

Automated tool for analyzing academic research papers and generating comprehensive, structured analysis documents in Markdown format with **Obsidian YAML metadata blocks** for research knowledge management.

## Purpose

This skill automates the process of academic paper analysis by:
- Reading PDF research papers using Claude's PDF reading capability
- Generating **APA7 format citations** automatically
- Creating **Obsidian YAML metadata blocks** with bilingual (Korean-English) tags
- Extracting and analyzing key components (research questions, methodology, findings, implications)
- Identifying theoretical frameworks, design contributions, and limitations
- Producing **structured 9-section analysis documents** in Markdown format
- Enabling seamless integration with Obsidian research vault workflows

## When to Use This Skill

Activate this skill when:
- Analyzing academic papers for Obsidian research vault
- Creating structured summaries with YAML metadata
- Building a searchable knowledge base of academic literature
- Conducting systematic literature reviews
- Preparing for research presentations or paper discussions
- Studying papers in education, educational psychology, HCI, AI literacy, instructional design, or HRD
- Organizing research papers with consistent metadata structure

## Output Structure

The skill generates analysis in three parts:

### Part 1: APA7 Citation
- Full citation in APA 7th edition format
- Authors, year, title, publication venue, DOI
- Ready to use in reference lists

### Part 2: Obsidian YAML Metadata Block
- **제목(Title)**: Paper title in Korean and English
- **Citation**: APA7 in-text citation format with parentheses (e.g., "(Wilmoth et al., 2014)")
- **Reference List**: APA7 full reference format (complete bibliographic entry)
- **저자(Authors)**: All authors with affiliations
- **연도(Year)**: Publication year
- **학회(Conference)**: Publication venue
- **DOI**: Digital object identifier
- **키워드(Keywords)**: Main topics and themes (bilingual)
- **관련이론(Related Theories)**: Theoretical frameworks used
- **연구목적(Purpose)**: Core research motivation
- **연구질문(Research Questions)**: RQ1, RQ2, RQ3, etc.
- **연구방법(Methodology)**: Research design, participants, procedure, analysis
- **주요결과(Main Findings)**: Key findings from the study
- **디자인기여(Design Contributions)**: Contributions to design/theory
- **디자인한계(Design Limitations)**: Acknowledged limitations
- **향후연구(Future Work)**: Suggested future directions
- **연구의의(Significance)**: Academic and practical significance
- **카테고리(Category Tags)**: Classification tags
- **연구상태(Obsidian Status)**: Research status (active-research, archived, etc.)
- **읽기우선순위(Reading Priority)**: Priority level (high, medium, low)
- **작성일(Created)**: Document creation date
- **업데이트(Update)**: Last update date

### Part 3: 9-Section Structured Analysis

**1. 연구 목적 및 배경 (Purpose & Background)**
- Core research problem
- Limitations of existing research
- Proposed solution direction

**2. 연구 질문 (Research Questions)**
- RQ1, RQ2, RQ3, etc. explicitly listed
- Hypotheses if applicable

**3. 연구 방법 (Methodology)**
- Research type (experimental, qualitative, mixed-methods, etc.)
- Participants and sampling
- Procedure step-by-step
- Data analysis methods

**4. 연구 도구 및 시스템 (System or Model)**
- Experimental tools, systems, platforms
- Design frameworks or models
- Technical infrastructure
- System architecture

**5. 주요 결과 (Findings)**
- Key results for each research question
- Statistical significance and effect sizes
- Supporting data and evidence

**6. 논의 및 시사점 (Discussion & Implications)**
- Theoretical contributions
- Practical implications for practitioners
- Field-specific applications (education, HCI, AI literacy, etc.)

**7. 디자인 한계 (Design Limitations)**
- Research design limitations
- Sample or data diversity constraints
- Generalizability boundaries
- Duration or scope limitations

**8. 향후 연구 (Future Work)**
- Proposed system/theory improvements
- Follow-up research directions
- Expansion possibilities

**9. 연구의의 (Significance)**
- Academic contribution summary
- Practical application perspectives
- Impact on educational practice or field advancement

## Workflow

### Step 1: Load the Paper

Read the PDF paper using Claude's Read tool:

```
Read the paper at: path/to/paper.pdf
```

Claude can read PDF files directly and will extract both text and visual content (figures, tables, equations).

### Step 2: Load Analysis Guidelines

Before analyzing, read the analysis guidelines to understand what to look for:

```python
# Read the analysis guidelines for reference
with open('references/guidelines.md', 'r', encoding='utf-8') as f:
    guidelines = f.read()
```

The guidelines provide:
- What information to extract for each section
- How to evaluate research quality
- Standards for educational research analysis
- Tips for critical reading

### Step 3: Analyze the Paper

Systematically work through each section of the paper:

1. **Initial Read**: Get overall sense of the paper
   - What is the main contribution?
   - What methodology was used?
   - What were the key findings?

2. **Deep Analysis**: Extract detailed information
   - Identify theoretical frameworks and constructs
   - Map out the research design
   - Extract specific results and statistics
   - Note limitations and future directions

3. **Critical Evaluation**: Assess quality and contribution
   - Is the methodology sound?
   - Are conclusions supported by data?
   - What are the practical implications?
   - How does this fit with existing literature?

4. **Synthesis**: Connect ideas
   - How does this relate to other papers?
   - What questions does it raise?
   - How could this inform practice?

### Step 4: Generate Markdown Document with YAML Metadata

**CRITICAL**: The YAML frontmatter MUST be at the absolute top of the file (first line). Nothing can come before it.

**YAML SYNTAX RULES** (Obsidian compatibility):
- **CRITICAL: ALL field names (keys) with parentheses MUST be wrapped in double quotes**
- **ALL values with colons (:), commas (,), brackets, or special characters MUST be wrapped in double quotes**
- **ALL list items (lines starting with `-`) MUST have values in double quotes**
- Example CORRECT: `"제목(Title)": "HPT 모델: 현장의 주요 모델 개관 / HPT Models: An Overview"`
- Example WRONG: `제목(Title): "HPT 모델: 현장의 주요 모델 개관"` ← This will cause "Invalid properties" error in Obsidian
- URLs, DOIs, RQ statements, parentheses content - ALL need quotes
- Nested field names also need quotes: `"연구유형(Type)": "이론적 검토"`
- Category checkboxes: `"[x] 커뮤니케이션 이론 (Communication Theory)"`
- Multi-line values using `>` do NOT need quotes (already safe)

Use the analysis template to structure your findings in three parts:

**Part 1: YAML Metadata Block** (파일 맨 위!)
```yaml
---
"제목(Title)": "Korean title / English title"
"Citation": "(FirstAuthor et al., 2025)"
"Reference List": "FirstAuthor, A., SecondAuthor, B., & ThirdAuthor, C. (2025). Full paper title. Conference/Journal Name, Volume(Issue), pages. https://doi.org/..."
"저자(Authors)": "Author list"
"소속(Affiliation)": "Institution"
"연도(Year)": 2025
"학회(Conference)": "CHI 2025"
"DOI": "https://doi.org/..."

"키워드(Keywords)":
  - "AI 리터러시 (AI Literacy)"
  - "교육용 로봇 (Educational Robots)"

"연구질문(Research Questions)":
  - "RQ1: What is the research question?"
  - "RQ2: Another research question?"

[... all metadata fields ...]

"연구상태(Obsidian Status)": "active-research"
"읽기우선순위(Reading Priority)": "high"
"작성일(Created)": "{{today}}"
"업데이트(Update)": "{{today}}"
---
```

**Part 2: APA7 Citation** (YAML 이후)
```
# [APA7 Citation]

Ho, H., Kargeti, N., Liu, Z., & Mutlu, B. (2025). SET-PAiREd: Designing for Parental Involvement...

---
```

**Part 3: 9-Section Analysis**
```
## 1. 연구 목적 및 배경 (Purpose & Background)
...
```

The template provides:
- YAML metadata block with all required fields at the TOP
- Bilingual (Korean-English) structure
- Standardized 9-section organization
- Obsidian-compatible formatting
- `{{today}}` placeholder for auto date population

### Step 5: Review and Refine

After generating the initial analysis:
- Check that all sections are complete
- Verify citations and references
- Ensure conclusions are supported by the paper
- Add personal notes and reflections
- Format code, equations, and tables properly

## Important Guidelines

### Reading Academic Papers Effectively

- **Start with Abstract**: Get the big picture first
- **Read Strategically**: Don't read linearly - jump to relevant sections
- **Focus on Methods and Results**: These are the core of empirical papers
- **Question Assumptions**: Think critically about claims and interpretations
- **Note Connections**: Link to other papers and your own research

### Information Extraction

- **Be Accurate**: Quote directly when capturing specific claims or results
- **Be Precise**: Include statistical details (p-values, effect sizes, n)
- **Be Complete**: Capture all relevant methodological details
- **Be Objective**: Distinguish between author claims and your interpretation

### Critical Analysis

- **Evaluate Methodology**: Is the design appropriate for the research question?
- **Assess Evidence**: Do the results support the conclusions?
- **Consider Limitations**: What are the boundaries of these findings?
- **Think Practically**: How could this be applied in real settings?

### Markdown Formatting

- Use proper heading hierarchy (##, ###, ####)
- Format tables for readability
- Use code blocks for statistical notation or models
- Include links to related papers or resources
- Use lists for clarity and scannability
- Bold key terms and concepts
- Use blockquotes for important definitions or quotes

### Domain-Specific Considerations

For **Education Research**:
- Note pedagogical approaches and learning theories
- Identify student populations and contexts
- Consider scalability and transferability
- Look for learning outcomes and assessments

For **Educational Psychology**:
- Focus on psychological constructs and measures
- Note experimental manipulations
- Consider cognitive and motivational factors
- Examine individual differences

For **HCI (Human-Computer Interaction)**:
- Identify interaction design patterns and frameworks
- Note user study methodologies (usability testing, interviews, observations)
- Consider user experience metrics and evaluation criteria
- Examine system design contributions and novel interaction techniques
- Look for design implications and guidelines

For **AI Literacy & Educational Technology**:
- Focus on AI system design for learning contexts
- Note how AI capabilities are explained to learners
- Consider transparency, explainability, and trust factors
- Examine integration of AI tools in educational settings
- Look for pedagogical strategies for teaching with/about AI

For **Instructional Design**:
- Identify design models and frameworks
- Note technology platforms and tools
- Consider usability and effectiveness
- Look at learner experience data

For **HRD (Human Resource Development)**:
- Focus on workplace learning contexts
- Note organizational factors
- Consider ROI and business impact
- Examine training transfer and application

## Bundled Resources

### Templates

- **analysis_template.md**: Structured template for analysis output
  - Pre-formatted sections for all analysis components
  - Markdown syntax examples
  - Placeholder text to guide analysis
  - Flexible structure that can be adapted

### References

- **guidelines.md**: Detailed guidelines for paper analysis
  - What to look for in each section
  - Quality evaluation criteria
  - Critical reading strategies
  - Domain-specific considerations
  - Example analyses

## Example Usage

```
User: "이 논문을 분석해서 Obsidian용 마크다운으로 정리해줘" [uploads PDF]

Claude:
1. Read the PDF paper
2. Load analysis guidelines and template from references/
3. Create Obsidian YAML metadata block (파일 맨 위!):
   - Extract title, authors, affiliation, year, venue, DOI
   - Generate Citation: APA7 in-text format with parentheses (e.g., "(Wilmoth et al., 2014)")
   - Generate Reference List: Full APA7 reference entry
   - Identify keywords (bilingual Korean-English)
   - Extract research questions
   - Summarize methodology, findings, contributions
   - Note limitations and future work
   - Add Obsidian metadata (status, priority)
   - Use {{today}} for dates
4. Generate APA7 citation section (YAML 이후)
5. Systematically analyze paper in 9 sections:
   - Purpose & Background
   - Research Questions
   - Methodology
   - System or Model
   - Findings
   - Discussion & Implications
   - Design Limitations
   - Future Work
   - Significance
6. Save as (Citation).md format (e.g., (Wilmoth et al., 2014).md)
```

Example output structure:
```
---
"제목(Title)": "..."
"Citation": "(Wilmoth et al., 2014)"
"Reference List": "Wilmoth, F. S., Prigmore, C., & Bray, M. (2014). HPT models: An overview of the major models in the field. Performance Improvement, 53(9), 31–42. https://doi.org/10.1002/pfi.21440"
"저자(Authors)": "..."
...
---

# APA7 Citation

Wilmoth, F. S., Prigmore, C., & Bray, M. (2014). ...

---

## 1. 연구 목적 및 배경
...
```

Example output filename: `(Wilmoth et al., 2014).md`

## Filename Convention

**CRITICAL**: Follow this exact naming format for all generated analysis files:

**Format**: `(Citation).md`

**Rules**:
1. Wrap the entire citation in parentheses `( )`
2. Use the **exact Citation field value** from YAML metadata (which already includes parentheses)
3. **DO NOT** add any other text (no "_analysis", no suffixes)
4. Follow APA7 in-text citation format

**Citation Field Format**:
- YAML Citation field: `"(Wilmoth et al., 2014)"` ← Includes parentheses
- Filename: `(Wilmoth et al., 2014).md` ← Same as Citation field + .md

**Examples**:
- ✅ Citation: `"(Wilmoth et al., 2014)"` → Filename: `(Wilmoth et al., 2014).md`
- ✅ Citation: `"(Huang et al., 2004)"` → Filename: `(Huang et al., 2004).md`
- ✅ Citation: `"(Koehler, 2016)"` → Filename: `(Koehler, 2016).md`
- ✅ Citation: `"(Smith & Jones, 2020)"` → Filename: `(Smith & Jones, 2020).md`
- ❌ `Wilmoth2014_analysis.md` (WRONG - no parentheses)
- ❌ `(Wilmoth et al., 2014)_analysis.md` (WRONG - no suffix)
- ❌ `Wilmoth et al., 2014.md` (WRONG - missing parentheses)

## Output Format

The final output is a well-structured Markdown file with:

**1. YAML Metadata Block** (Obsidian frontmatter - 파일 맨 위!)
- **MUST be at line 1** of the file
- All metadata fields in Korean-English bilingual format
- Compatible with Obsidian queries and filters
- Searchable and linkable across vault
- `{{today}}` placeholder for dates

**2. APA7 Citation** (after YAML block)
- Complete citation ready for reference lists
- Follows APA 7th edition format

**3. 9-Section Analysis** (main body)
- Clear heading hierarchy
- Bilingual section titles
- Properly formatted lists and tables
- Code blocks for statistical notation
- Blockquotes for key definitions
- Links to related papers or concepts

Example filename: `(Wilmoth et al., 2014).md` (based on Citation field, wrapped in parentheses)

**File Structure**:
```
Line 1:  ---
Line 2:  "제목(Title)": "..."
Line 3:  "Citation": "(Wilmoth et al., 2014)"
Line 4:  "Reference List": "Full APA7 reference..."
...
Line N:  ---
Line N+1: (blank)
Line N+2: # APA7 Citation
...
```

## Advanced Features

### Multiple Paper Analysis

When analyzing multiple related papers:
- Create a summary document linking analyses
- Note common themes and contradictions
- Build a concept map of the literature
- Identify research gaps

### Integration with Literature Review

The analysis documents can be:
- Compiled into a comprehensive literature review
- Organized by theme or research question
- Used to build an annotated bibliography
- Synthesized into a research proposal

### Customization

The template can be adapted for:
- Different research paradigms (quantitative, qualitative, mixed)
- Different paper types (theoretical, empirical, review)
- Different output needs (personal notes, presentation slides, blog posts)
- Different citation styles (APA, MLA, Chicago)

## Notes

- This skill leverages Claude's native PDF reading capability
- **Obsidian-first design**: YAML metadata is fully compatible with Obsidian dataview queries
- **Bilingual support**: All metadata in Korean-English format for Korean researchers
- Analysis quality depends on paper quality and completeness
- Processing time varies with paper length and complexity
- Works best with well-structured academic papers
- Can handle papers with figures, tables, and equations
- Optimized for education, educational psychology, HCI, AI literacy, instructional design, and HRD research
- **APA7 citation format** for academic writing and reference management
- Output documents are plain text Markdown (easily version controlled with Git)
- Template structure follows academic conventions while being Obsidian-optimized
- Dates auto-populate with current date for tracking purposes
