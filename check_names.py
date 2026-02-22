import sys
sys.path.insert(0, 'company-analyzer/scripts')

from excel_helper import get_companies_to_analyze
import json

# 개선된 함수로 엑셀 읽기
companies = get_companies_to_analyze('기업분석.xlsx')

# JSON으로 출력 (인코딩 문제 회피)
result = {
    'total': len(companies),
    'companies': []
}

for i, company in enumerate(companies, 1):
    result['companies'].append({
        'index': i,
        'name': company['기업명'],
        'homepage': company['홈페이지주소'],
        'ceo': company['대표자명']
    })

# JSON 출력
print(json.dumps(result, ensure_ascii=False, indent=2))
