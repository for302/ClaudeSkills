---
name: company-analyzer
description: Automated company research and analysis tool that reads company information from Excel, performs web searches to gather business intelligence, and writes structured analysis results back to Excel. Use when analyzing multiple companies from a spreadsheet, performing competitive intelligence, or conducting market research on Korean companies.
---

# Company Analyzer

Automated tool for analyzing companies listed in Excel spreadsheets by gathering information from web sources and generating structured business intelligence reports.

## Purpose

This skill automates the process of company research and analysis by:
- Reading company lists from Excel files (company name, homepage, CEO name)
- Performing web searches to gather business information
- Analyzing companies across multiple dimensions (business areas, market status, technology, etc.)
- Writing structured analysis results back to Excel in separate columns

## When to Use This Skill

Activate this skill when:
- Analyzing multiple companies from an Excel spreadsheet
- Performing competitive intelligence research
- Conducting market research on Korean companies
- Creating company databases with detailed business information
- Preparing for business development or partnership evaluations

## Analysis Categories

The skill gathers information across seven key categories:

1. **사업분야및주요제품서비스** - Business areas and main products/services
2. **주요고객및시장현황** - Main customers and market status
3. **국내시장현황** - Domestic market status (Korea)
4. **글로벌시장현황** - Global market status
5. **기술역량** - Technology capability
6. **수상실적** - Awards and recognition
7. **뉴스요약** - News and updates summary

## Workflow

### Step 1: Load and Validate Excel File

Read the Excel file containing company information:

```python
from scripts.excel_helper import read_companies, get_companies_to_analyze

# Get list of companies to analyze
companies = get_companies_to_analyze('companies.xlsx')
```

Expected Excel columns:
- **기업명** (required): Company name
- **홈페이지주소** (optional): Homepage URL
- **대표자명** (optional): CEO name

**Important**: The excel_helper uses `openpyxl` engine with `dtype=str` to ensure Korean company names are read correctly with proper UTF-8 encoding. This prevents issues like "기원테크" being misread as "키원테크".

### Step 2: Load Analysis Framework

Before analyzing companies, read the analysis framework to understand what information to gather for each category:

```python
# Read the analysis framework for reference
with open('references/analysis_framework.md', 'r', encoding='utf-8') as f:
    framework = f.read()
```

The framework provides detailed guidelines for each analysis category including:
- What information to look for
- Recommended information sources
- Output format specifications
- Example outputs

### Step 3: Analyze Each Company

For each company in the list:

1. **Construct search queries** using company name, homepage, and CEO name
2. **Perform web searches** using the WebSearch tool
3. **Extract relevant information** according to the analysis framework
4. **Structure the findings** into the seven analysis categories
5. **Store results** in a structured format

Search strategy:
- **Use the exact company name from Excel** - Do not modify or simplify the company name
- Start with the company homepage if provided
- Use company name + specific keywords (e.g., "기업명 + 제품", "기업명 + 수상")
- Cross-reference multiple sources for accuracy
- Prioritize recent information (within 1-2 years)

Example search queries:
```
"{company_name} 사업분야 제품"
"{company_name} 주요 고객"
"{company_name} 시장 점유율"
"{company_name} 기술 특허"
"{company_name} 수상"
"{company_name} 뉴스"
```

For each analysis category, follow the guidelines in `references/analysis_framework.md`:
- Extract information as specified in the framework
- Format output as 2-3 concise sentences (or bullet points for awards)
- Leave blank if information is not available (do not guess or fabricate)
- Use Korean language for all outputs

### Step 4: Write Results to Excel

After analyzing all companies, write the results back to Excel:

```python
import pandas as pd
from scripts.excel_helper import write_analysis_results

# Prepare results DataFrame
results = pd.DataFrame({
    '기업명': [...],
    '홈페이지주소': [...],
    '대표자명': [...],
    '사업분야및주요제품서비스': [...],
    '주요고객및시장현황': [...],
    '국내시장현황': [...],
    '글로벌시장현황': [...],
    '기술역량': [...],
    '수상실적': [...],
    '뉴스요약': [...]
})

# Write to Excel
write_analysis_results('companies.xlsx', results)
```

The helper function will:
- Add analysis columns to the Excel file
- Format headers with bold text
- Enable text wrapping for analysis columns
- Auto-adjust column widths
- Preserve original company information

### Step 5: Verify and Report

After writing results:
- Count how many companies were successfully analyzed
- Identify any companies with missing information
- Report summary statistics to the user

## Important Guidelines

### Use Original Company Names

- **Critical**: Always use the exact company name as it appears in the Excel file
- Do not modify, simplify, or transliterate company names
- Example: If Excel shows "(주)기원테크", search for "(주)기원테크" NOT "(주)키원테크"
- Accurate company names ensure correct search results and prevent analyzing wrong companies
- The excel_helper.py is configured with UTF-8 encoding to preserve original Korean characters

### Information Quality

- **Accuracy**: Cross-check facts across multiple sources
- **Recency**: Prefer information from the past 1-2 years
- **Relevance**: Focus on information directly related to the analysis category
- **Verification**: Use official sources (company website, press releases) when possible

### Handling Missing Information

- Leave cells blank when information cannot be found
- Do not fabricate or guess information
- Do not use placeholder text like "정보 없음" (as per user preference)

### Output Formatting

- Use Korean language for all analysis outputs
- Keep each field's content concise (300-500 characters)
- Use professional, factual tone
- Include specific numbers, dates, and names when available
- Format awards as comma-separated list with years

### Performance Optimization

- Batch web searches when possible
- Reuse information found in one search for multiple categories
- Start with homepage search to gather multiple data points efficiently

## Bundled Resources

### Scripts

- **excel_helper.py**: Utility functions for reading and writing Excel files
  - `read_companies()`: Read company list from Excel
  - `get_companies_to_analyze()`: Get companies needing analysis
  - `write_analysis_results()`: Write results to Excel with formatting

### References

- **analysis_framework.md**: Detailed guidelines for each analysis category
  - What information to look for
  - Recommended sources
  - Output format specifications
  - Examples for each category

## Example Usage

```
User: "이 엑셀 파일에 있는 기업들을 분석해서 정보를 추가해줘"

Claude:
1. Load companies from Excel using excel_helper.py
2. Read analysis framework from references/
3. For each company:
   - Search for business areas and products
   - Find customer and market information
   - Gather domestic and global market data
   - Research technology capabilities
   - Look up awards and recognition
   - Summarize recent news
4. Write all results back to Excel with proper formatting
5. Report completion with statistics
```

## Notes

- This skill requires pandas and openpyxl packages
- Web searches are performed using Claude's WebSearch tool
- Analysis quality depends on available public information
- Processing time scales with number of companies
- Recommend analyzing in batches for large company lists (>20 companies)
