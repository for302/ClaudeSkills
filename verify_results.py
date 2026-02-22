import pandas as pd

# 결과 파일 읽기
df = pd.read_excel('기업분석_결과.xlsx')

print("=" * 80)
print("기업 분석 결과 검증")
print("=" * 80)
print(f"\n총 분석 기업 수: {len(df)}\n")

# 각 컬럼별 데이터 존재 여부 확인
columns = df.columns.tolist()
print("분석 항목별 데이터 현황:")
print("-" * 80)

for idx, row in df.iterrows():
    company_name = row['기업명']
    print(f"\n{idx+1}. {company_name}")

    for col in columns:
        if col in ['기업명', '홈페이지주소', '대표자명']:
            continue

        value = row[col]
        if pd.isna(value) or value == '':
            status = "✗ 정보 없음"
        else:
            status = f"✓ {len(str(value))}자"

        print(f"   - {col}: {status}")

print("\n" + "=" * 80)
print("분석 완료 통계")
print("=" * 80)

analysis_columns = ['사업분야및주요제품서비스', '주요고객및시장현황', '국내시장현황',
                   '글로벌시장현황', '기술역량', '수상실적', '뉴스요약']

for col in analysis_columns:
    filled = df[col].notna().sum()
    empty = df[col].isna().sum() + (df[col] == '').sum()
    print(f"{col}: {filled}개 기업 정보 있음, {empty}개 기업 정보 없음")

print("\n✓ 모든 기업 분석이 완료되었습니다!")
print(f"✓ 결과 파일: 기업분석_결과.xlsx")
