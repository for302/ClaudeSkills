# Paper Analysis Guidelines

This document provides detailed guidance on how to analyze academic papers effectively, with special focus on **education, educational psychology, HCI, AI literacy, instructional design, and HRD research**.

The analysis output includes:
1. **APA7 Citation** - Ready-to-use citation
2. **Obsidian YAML Metadata** - Structured, searchable frontmatter
3. **9-Section Analysis** - Comprehensive paper breakdown

---

## 📋 Obsidian YAML Metadata Guide

### Purpose of YAML Metadata

The YAML metadata block (frontmatter) enables:
- **Searchability**: Query papers by any metadata field
- **Organization**: Filter by category, priority, status
- **Linking**: Connect related papers automatically
- **Tracking**: Monitor reading progress and research timeline
- **Bilingual support**: Korean-English tags for Korean researchers

### YAML Structure Requirements

**Critical Rules**:
1. **Exact field names**: Use the exact Korean(English) format as shown in template
2. **Indentation**: Use 2 spaces for nested items (never tabs)
3. **List format**: Use `- ` for list items
4. **Multi-line text**: Use `>` for paragraph-style content
5. **Dates**: Use YYYY-MM-DD format
6. **No empty fields**: Keep all fields even if content is TBD

### Required YAML Fields

```yaml
---
제목(Title): [Korean / English]
저자(Authors): [Names - Affiliations]
소속(Affiliation): [Institution]
연도(Year): YYYY
학회(Conference): [Venue name]
DOI: [https://doi.org/...]

키워드(Keywords):
  - [Keyword1 (English1)]
  - [Keyword2 (English2)]

관련이론(Related Theories):
  - [Theory name]

연구목적(Purpose): >
  [Multi-line purpose description]

연구질문(Research Questions):
  - [RQ1: ...]
  - [RQ2: ...]

연구방법(Methodology):
  연구유형(Type): [Type]
  참여자(Participants): [Description]
  절차(Procedure):
    - [Step 1]
  분석(Analysis):
    - [Method]

주요결과(Main Findings):
  - [Finding 1]

디자인기여(Design Contributions):
  - [Contribution]

디자인한계(Design Limitations):
  - [Limitation]

향후연구(Future Work):
  - [Direction]

연구의의(Significance): >
  [Multi-line significance]

카테고리(Category Tags):
  - [ ] 교육학 (Education)
  - [x] HCI
  - [ ] AI 리터러시 (AI Literacy)

연구상태(Obsidian Status): "active-research"
읽기우선순위(Reading Priority): "high"
작성일(Created): 2025-01-15
업데이트(Update): 2025-01-15
---
```

### YAML Field Descriptions

**제목(Title)**: Bilingual title (Korean / English)

**키워드(Keywords)**: 3-5 main topics in bilingual format
- Use consistent terminology across papers
- Include both domain (e.g., HCI) and method (e.g., qualitative)

**관련이론(Related Theories)**: Theoretical frameworks used
- Examples: Self-Determination Theory, TPACK, Activity Theory

**연구목적(Purpose)**: 2-3 sentence summary using `>`
- Why this research was conducted
- What problem it addresses

**연구질문(Research Questions)**: List format
- Copy exact RQ wording from paper
- Use RQ1, RQ2, RQ3 format

**연구방법(Methodology)**: Nested structure
- **연구유형(Type)**: Experimental, Qualitative, Mixed, Case Study, etc.
- **참여자(Participants)**: n, demographics, sampling
- **절차(Procedure)**: Step-by-step list
- **분석(Analysis)**: Statistical/qualitative methods

**디자인기여(Design Contributions)**: What's new
- Theoretical contributions
- Methodological innovations
- Design guidelines or frameworks

**디자인한계(Design Limitations)**: Acknowledged weaknesses
- Sample limitations
- Generalizability constraints
- Technical limitations

**카테고리(Category Tags)**: Checkboxes for classification
- Check `[x]` for applicable categories
- Leave unchecked `[ ]` for non-applicable

**연구상태(Obsidian Status)**: Research workflow status
- `"active-research"`: Currently reading/analyzing
- `"archived"`: Completed, for reference
- `"to-read"`: In queue

**읽기우선순위(Reading Priority)**: Priority level
- `"high"`: Must read immediately
- `"medium"`: Read soon
- `"low"`: Nice to read eventually

### Obsidian Integration Tips

**Dataview Queries**:
```dataview
TABLE 저자(Authors), 연도(Year), 읽기우선순위(Reading Priority)
FROM "Papers"
WHERE 카테고리(Category Tags) contains "HCI"
SORT 연도(Year) DESC
```

**Internal Linking**:
- Link to authors: `[[Author Name]]`
- Link to theories: `[[Self-Determination Theory]]`
- Link to related papers: `[[Ho2025_SET-PAiREd_analysis]]`

**Tags**:
- YAML tags are searchable in Obsidian
- Use consistent bilingual format
- Create tag hierarchy: `#research/education/AI-literacy`

---

## 📖 APA7 Citation Guide

### Citation Format

**Journal Article**:
```
Author, A. A., Author, B. B., & Author, C. C. (Year). Title of article.
  Journal Name, volume(issue), page-page. https://doi.org/xxxxx
```

**Conference Paper**:
```
Author, A. A., & Author, B. B. (Year). Title of paper. In Proceedings
  of the Conference Name (pp. page-page). Publisher. https://doi.org/xxxxx
```

**Multiple Authors**:
- 1-20 authors: List all names
- 21+ authors: List first 19, then "...", then last author

**Italics**:
- Journal/Conference name: *italic*
- Volume number: *italic*
- Everything else: regular

### Example Citations

**CHI Paper**:
```
Ho, H., Kargeti, N., Liu, Z., & Mutlu, B. (2025). SET-PAiREd:
  Designing for Parental Involvement in Learning with an
  AI-Assisted Educational Robot. In Proceedings of the CHI
  Conference on Human Factors in Computing Systems (CHI '25),
  Yokohama, Japan. https://doi.org/10.1145/3706598.3713330
```

**Journal Article**:
```
Zimmerman, B. J., & Schunk, D. H. (2011). Self-regulated learning
  and performance: An introduction and an overview. In B. J.
  Zimmerman & D. H. Schunk (Eds.), Handbook of self-regulation
  of learning and performance (pp. 1-12). Routledge.
```

---

## 📖 Reading Strategy

### The Three-Pass Approach

**First Pass (5-10 minutes)**: Get the big picture
- Read title, abstract, and conclusion
- Skim section headings and subheadings
- Look at figures and tables
- Note the research question and main findings
- Decision: Is this paper relevant? Should you continue?

**Second Pass (1 hour)**: Understand the content
- Read introduction and related work carefully
- Read methodology in detail
- Study results and discussion
- Note key points, but ignore technical details
- Try to grasp the main contributions

**Third Pass (4-5 hours)**: Master the paper
- Read every section carefully
- Understand every figure, table, and equation
- Note assumptions, missing details, and potential issues
- Think about how you would replicate the study
- Compare with related work
- Identify strengths and weaknesses

For most papers, the **second pass** is sufficient for analysis purposes.

---

## 🎯 What to Look for in Each Section

### Abstract
**Extract**:
- Core research question
- Method used (in one sentence)
- Key finding (in one sentence)
- Significance or implication

**Evaluate**:
- Is it clear and concise?
- Does it accurately represent the paper?

### Introduction
**Extract**:
- Problem statement or motivation
- Research gap being addressed
- Research questions or hypotheses
- Overview of approach
- Main contributions claimed

**Evaluate**:
- Is the problem well-motivated?
- Is the research gap clearly identified?
- Are the contributions significant?

### Literature Review / Related Work
**Extract**:
- Key prior studies cited
- Theoretical frameworks used
- Current state of knowledge
- How this work differs or extends prior work

**Evaluate**:
- Is the review comprehensive?
- Are important papers missing?
- Is the positioning convincing?

### Theoretical Framework
**Extract**:
- Theories, models, or frameworks guiding the research
- Key constructs and their definitions
- Relationships between constructs
- Conceptual model or framework diagram

**Evaluate**:
- Is the framework appropriate for the research question?
- Are constructs clearly defined?
- Are relationships logical?

### Methodology
**Extract**:
- Research design and rationale
- Participants (n, demographics, sampling)
- Setting and context
- Data collection instruments
- Reliability and validity of instruments
- Procedure (step-by-step)
- Data analysis methods
- Ethical considerations

**Evaluate**:
- Is the design appropriate for the research question?
- Is the sample adequate and representative?
- Are instruments validated and reliable?
- Is the procedure clearly described and replicable?
- Are potential biases addressed?
- Are ethical issues handled properly?

**Red Flags**:
- Small sample size without justification
- Convenience sampling with claims of generalizability
- Instruments without reported reliability/validity
- Confounding variables not controlled
- Missing details that prevent replication

### Results
**Extract**:
- Descriptive statistics (means, SDs, frequencies)
- Inferential statistics (t-tests, ANOVA, correlations, regressions)
- Effect sizes (Cohen's d, eta-squared, R²)
- Statistical significance (p-values)
- Qualitative themes or patterns
- Supporting quotes or examples

**Evaluate**:
- Do results directly answer research questions?
- Are statistics reported completely?
- Are effect sizes meaningful (not just statistically significant)?
- Are tables and figures clear and accurate?
- Are qualitative findings well-supported with evidence?

**Red Flags**:
- P-hacking (reporting only significant results)
- Missing effect sizes
- Unclear or inconsistent statistics
- Cherry-picked quotes without systematic analysis
- Results that don't match the claims

### Discussion / Conclusion
**Extract**:
- Interpretation of findings
- Theoretical implications
- Practical implications
- Limitations acknowledged
- Future research suggestions

**Evaluate**:
- Are interpretations supported by the data?
- Are limitations honestly acknowledged?
- Are practical implications realistic?
- Do conclusions go beyond the data?

**Red Flags**:
- Overgeneralization beyond sample
- Ignoring contradictory findings
- Causal claims from correlational data
- Dismissing major limitations

---

## ⚖️ Evaluating Research Quality

### Validity

**Internal Validity**: Can we trust the causal claims?
- Were confounding variables controlled?
- Was randomization used (if applicable)?
- Were there alternative explanations?
- Did attrition bias results?

**External Validity**: Can we generalize the findings?
- Is the sample representative?
- Is the setting typical or artificial?
- Would results transfer to other contexts?

**Construct Validity**: Do measures capture what they claim?
- Are constructs clearly defined?
- Are measures validated?
- Is there convergent/discriminant validity?

**Statistical Conclusion Validity**: Are statistics used correctly?
- Is sample size adequate (power analysis)?
- Are assumptions of tests met?
- Are effect sizes reported?
- Are corrections made for multiple comparisons?

### Reliability

**Are results consistent and replicable?**
- Cronbach's alpha > 0.70 for scales?
- Inter-rater reliability for qualitative coding?
- Test-retest reliability for repeated measures?
- Clear enough description to replicate?

### Credibility (Qualitative Research)

- **Trustworthiness**: Multiple data sources, member checking, prolonged engagement
- **Transferability**: Thick description of context
- **Dependability**: Clear audit trail
- **Confirmability**: Reflexivity, acknowledgment of researcher bias

---

## 🎓 Domain-Specific Considerations

### Education Research

**Key Questions**:
- What is the learning context (K-12, higher ed, informal)?
- What pedagogical approach is being studied?
- What are the learning outcomes measured?
- How is learning assessed?
- What is the duration of the intervention?
- Are effects sustained over time?

**Common Methods**:
- Quasi-experimental designs (classrooms as units)
- Pre/post assessments
- Control vs. treatment groups
- Mixed methods (learning outcomes + student perceptions)
- Design-based research

**Quality Indicators**:
- Alignment between learning objectives, instruction, and assessment
- Use of validated achievement tests
- Control for teacher effects
- Ecological validity (real classroom settings)
- Long-term retention tested

### Educational Psychology

**Key Questions**:
- What psychological constructs are being measured?
- What is the unit of analysis (individual, group)?
- Are mediating or moderating variables examined?
- What is the theoretical basis for predictions?

**Common Methods**:
- Correlational studies
- Experimental manipulations
- Structural equation modeling (SEM)
- Latent growth modeling
- Survey research

**Quality Indicators**:
- Validated psychological scales
- Appropriate statistical models for research questions
- Consideration of individual differences
- Theory-driven hypotheses
- Large enough sample for complex models

### HCI (Human-Computer Interaction)

**Key Questions**:
- What interaction design problem is being addressed?
- What user population is studied?
- What evaluation methods are used?
- Are design implications clearly articulated?
- How generalizable are the findings to other systems/contexts?

**Common Methods**:
- User studies (lab-based, field studies, diary studies)
- Usability testing (think-aloud, task performance)
- Interviews and observations
- Surveys and questionnaires
- Design workshops and participatory design
- A/B testing and controlled experiments
- Wizard-of-Oz studies (for AI/robot systems)

**Quality Indicators**:
- Clear description of system/prototype
- Appropriate participant recruitment (representative of target users)
- Triangulation of methods (mixed qualitative-quantitative)
- Ecological validity (realistic usage contexts)
- Design implications grounded in findings
- Novelty of interaction technique or design contribution
- Comparison with baseline or existing systems

**HCI-Specific Analysis Tips**:
- **System Description**: Document the interface, features, and technical implementation
- **Interaction Techniques**: Note novel input methods, displays, or interaction paradigms
- **User Experience**: Capture subjective measures (satisfaction, perceived usability, trust)
- **Design Guidelines**: Extract actionable design recommendations
- **Contextual Factors**: Consider setting, task, and social context

### AI Literacy & Educational Technology

**Key Questions**:
- How is AI introduced or integrated in the learning environment?
- What AI literacy competencies are targeted?
- How is AI explainability or transparency addressed?
- What are learners' perceptions and understanding of AI?
- How does AI augment or transform pedagogical practices?

**Common Methods**:
- Educational interventions with AI tools
- Pre/post assessments of AI literacy
- Qualitative interviews about AI understanding
- Design-based research with AI-enhanced learning systems
- Analysis of learner-AI interactions (log data, conversation analysis)
- Surveys on attitudes toward AI

**Quality Indicators**:
- Clear definition of AI literacy constructs
- Validated or well-justified assessment instruments
- Consideration of diverse learner populations
- Ethical considerations (privacy, bias, equity)
- Transparency in how AI works and how it's explained to learners
- Evidence of learning outcomes or conceptual change
- Discussion of pedagogical strategies for teaching with/about AI

**AI Literacy-Specific Analysis Tips**:
- **AI System Design**: How is the AI system designed for learning contexts?
- **Explainability**: How are AI decisions or behaviors made understandable?
- **Trust & Agency**: How do learners develop trust in or agency over AI?
- **Equity & Access**: Who benefits? Who might be excluded?
- **Pedagogical Integration**: How do educators use AI tools in teaching?
- **Competency Development**: What AI-related knowledge/skills are developed?

**Common AI Literacy Frameworks**:
- Long & Magerko's AI Literacy Framework (2020)
- AI4K12 Five Big Ideas in AI
- TPACK-AI (Technological Pedagogical Content Knowledge for AI)

### Instructional Design

**Key Questions**:
- What design model or framework is used (ADDIE, SAM, backward design)?
- What technologies or media are employed?
- How is usability evaluated?
- What is the evidence of effectiveness?
- Is the design transferable to other contexts?

**Common Methods**:
- Design-based research
- Usability testing
- Iterative design and evaluation
- Case studies
- Learning analytics

**Quality Indicators**:
- Clear articulation of design decisions
- Alignment with learning theories
- Evidence of iterative improvement
- Usability data (completion rates, time on task, errors)
- Learning effectiveness data
- Considerations of scalability

### HRD (Human Resource Development)

**Key Questions**:
- What is the organizational context?
- What training or development intervention is studied?
- How is transfer to the workplace measured?
- What are the organizational outcomes?
- Is ROI considered?

**Common Methods**:
- Kirkpatrick's four levels of evaluation
- Pre/post training assessments
- Surveys of trainees and supervisors
- Performance metrics
- Cost-benefit analysis

**Quality Indicators**:
- Evaluation beyond reaction (Level 1)
- Measurement of behavior change (Level 3)
- Organizational impact (Level 4)
- Consideration of transfer climate
- Longitudinal follow-up
- Practical significance for organizations

---

## 🧠 Critical Thinking Questions

As you analyze, continually ask:

**About the Research Question**:
- Is this an important question?
- Has it been answered before?
- Is it answerable with the chosen method?

**About the Method**:
- Is this the right approach for this question?
- What are the trade-offs of this design?
- What alternative approaches could work?
- What are the major limitations?

**About the Results**:
- Do the results make sense?
- Are there alternative explanations?
- How big are the effects practically?
- Do figures match tables match text?

**About the Conclusions**:
- Do conclusions follow from results?
- Are claims overstated?
- What are the boundaries of these findings?
- How would I apply this in practice?

**About the Contribution**:
- What is genuinely new here?
- How does this change my understanding?
- What are the implications for theory?
- What are the implications for practice?

---

## ✍️ Writing Your Analysis

### General Principles

**Be Objective**: Distinguish between what the authors claim and your own interpretation.
- Authors claim: "The authors argue that..."
- Your interpretation: "This suggests that..." or "I interpret this to mean..."

**Be Specific**: Include details, numbers, and examples.
- Weak: "The sample was small."
- Strong: "The sample consisted of 23 undergraduate students from a single university."

**Be Balanced**: Note both strengths and weaknesses.
- Don't just criticize
- Don't just praise
- Evaluate fairly

**Be Clear**: Write for your future self or a colleague.
- Use plain language
- Define technical terms
- Organize logically

### Structuring Your Analysis

**Follow the Template**: Use the provided analysis template as a starting point.

**Adapt as Needed**: Not all papers fit the same structure.
- Theoretical papers may not have a methods section
- Review papers synthesize across studies
- Some papers have non-standard organizations

**Add Your Voice**: The "Personal Notes" section is where you think critically.
- What do you really think about this paper?
- How does it connect to your interests?
- What questions does it raise?

### Markdown Best Practices

**Use Headings Clearly**:
```markdown
## Main Section
### Subsection
#### Detail Level
```

**Format Tables**:
```markdown
| Heading 1 | Heading 2 |
|-----------|-----------|
| Data 1    | Data 2    |
```

**Use Lists**:
```markdown
- Bullet point
- Another point
  - Nested point

1. Numbered item
2. Another item
```

**Emphasize Key Points**:
```markdown
**Bold for emphasis**
*Italic for terms*
`Code format for statistics`
> Blockquote for definitions
```

**Link Related Content**:
```markdown
[Link text](url)
[Related paper](./other_paper_analysis.md)
```

---

## 🚀 Advanced Analysis Techniques

### Synthesis Across Papers

When analyzing multiple related papers:
1. **Create a comparison table**: Compare methods, findings, populations across papers
2. **Identify themes**: What common findings emerge?
3. **Note contradictions**: Where do papers disagree?
4. **Map the landscape**: Create a concept map of how papers relate
5. **Identify gaps**: What hasn't been studied?

### Building a Literature Matrix

Create a spreadsheet with columns:
- Author/Year
- Research Question
- Method
- Sample
- Key Findings
- Limitations
- Your Rating

This helps you:
- See patterns across studies
- Identify methodological trends
- Support systematic reviews
- Organize your thinking

### Concept Mapping

Visually represent:
- Theoretical relationships
- How studies build on each other
- Connections between constructs
- Your own developing understanding

Tools: Obsidian, Roam Research, ConceptDraw, or even paper and pencil

---

## 📚 Example Analysis Excerpts

### Example: Methodology Analysis

**Good**:
> The study employed a randomized controlled trial with 120 undergraduate students (M_age = 20.3, SD = 1.5) enrolled in an introductory psychology course. Students were randomly assigned to either a spaced practice condition (n=60) or a massed practice condition (n=60). The dependent variable was test performance measured one week after the learning phase using a 40-item multiple-choice test (Cronbach's α = .85). The design effectively controls for individual differences through randomization, though the sample is limited to one course at one university, limiting generalizability.

**Why it's good**: Specific details, includes statistics, notes both strengths and limitations.

**Poor**:
> The researchers used an experiment with college students to test spaced vs. massed practice. Students took a test afterward.

**Why it's poor**: Vague, missing key details, no evaluation.

### Example: Critical Analysis

**Good**:
> While the authors conclude that their intervention "significantly improved learning," the effect size was modest (d = 0.32) and the follow-up period was only one week. It remains unclear whether these gains persist over time or transfer to novel problems. Additionally, the intervention required substantial instructor training (20 hours), raising questions about practical scalability. The study makes a theoretical contribution by demonstrating the mediating role of self-efficacy, but practitioners should interpret the practical implications cautiously given these limitations.

**Why it's good**: Distinguishes statistical from practical significance, considers real-world implementation, balances theoretical and practical value.

---

## 🎯 Summary Checklist

Before finalizing your analysis, check:

- [ ] All key sections of the paper are covered
- [ ] Specific details included (numbers, names, methods)
- [ ] Both strengths and weaknesses noted
- [ ] Your own critical thinking included
- [ ] Connections to other work noted
- [ ] Practical implications considered
- [ ] Markdown formatting is clean and consistent
- [ ] Citations are accurate
- [ ] You could use this analysis 6 months from now

---

## 💡 Final Tips

1. **Start simple**: Your first few analyses will take time. It gets faster with practice.

2. **Develop your style**: Adapt the template to your needs over time.

3. **Make it useful**: Focus on what YOU need to remember and use.

4. **Be honest**: Note what you don't understand. It's okay to have questions.

5. **Connect ideas**: The real value comes from linking papers together.

6. **Think practically**: How does this apply to real problems?

7. **Enjoy the process**: Reading research should be intellectually stimulating!

---

**Remember**: The goal is not to perfectly summarize every detail, but to **understand the paper deeply** and **capture insights for future use**. Your analysis is a thinking tool, not just a record.
