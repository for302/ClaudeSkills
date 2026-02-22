import pandas as pd
import json

# 결과 파일 읽기
df = pd.read_excel('기업분석_정확한버전.xlsx', engine='openpyxl')

print("=" * 80)
print("기업 분석 결과 검증 (정확한 기업명 버전)")
print("=" * 80)
print(f"\n총 분석 기업 수: {len(df)}\n")

# JSON으로 기업명 출력
result = {
    '총_기업수': len(df),
    '기업목록': []
}

for idx, row in df.iterrows():
    result['기업목록'].append({
        '순번': idx+1,
        '기업명': row['기업명'],
        '홈페이지': row['홈페이지주소']
    })

print(json.dumps(result, ensure_ascii=False, indent=2))

print("\n" + "=" * 80)
print("분석 항목별 데이터 현황")
print("=" * 80)

analysis_columns = ['사업분야및주요제품서비스', '주요고객및시장현황', '국내시장현황',
                   '글로벌시장현황', '기술역량', '수상실적', '뉴스요약']

for col in analysis_columns:
    filled = df[col].notna().sum()
    empty = df[col].isna().sum() + (df[col] == '').sum()
    avg_length = df[df[col].notna()][col].str.len().mean() if filled > 0 else 0
    print(f"\n{col}:")
    print(f"  - 정보 있음: {filled}개 기업")
    print(f"  - 정보 없음: {empty}개 기업")
    print(f"  - 평균 글자 수: {avg_length:.0f}자")

print("\n" + "=" * 80)
print("완료!")
print("=" * 80)
print("파일: 기업분석_정확한버전.xlsx")
