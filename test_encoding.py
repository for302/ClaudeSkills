import sys
sys.path.insert(0, 'company-analyzer/scripts')

from excel_helper import get_companies_to_analyze

# 개선된 함수로 엑셀 읽기
companies = get_companies_to_analyze('기업분석.xlsx')

print("=" * 80)
print("정확한 기업명 확인 (UTF-8 인코딩)")
print("=" * 80)
print(f"\n총 {len(companies)}개 기업\n")

for i, company in enumerate(companies, 1):
    print(f"{i}. {company['기업명']}")
    if company['홈페이지주소']:
        print(f"   홈페이지: {company['홈페이지주소']}")
    if company['대표자명']:
        print(f"   대표자: {company['대표자명']}")
    print()
