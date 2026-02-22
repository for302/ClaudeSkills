import pandas as pd

df = pd.read_excel('기업분석.xlsx')
print("=== 엑셀 파일 내용 ===\n")
print(f"총 기업 수: {len(df)}\n")
print(f"컬럼: {df.columns.tolist()}\n")
print("기업 목록:")
print(df.to_string(index=False))
