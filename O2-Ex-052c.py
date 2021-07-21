import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls", sheet_name='Func')
print("2-Plan-A.xls - Aba Func")
print(excel_df)
print("-------------------------------------------------\n\n\n")


excel_df2 = pd.read_excel("02-Plan-A.xls", sheet_name='Depart')
print("2-Plan-A.xls - Aba Depart")
print(excel_df2)
print("-------------------------------------------------\n")

print("\n\n Fim")