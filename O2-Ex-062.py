import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
print(excel_df)

print("\n\n-------------  Group By - Size ------------------------")
print(excel_df.groupby(by='Salário').size())
print("\n\n",excel_df.groupby(['Salário']).size())

print("\n\n-------------  Group By - Mean ------------------------")
print(excel_df.groupby(by='Departamento').mean())






print("\n\n Fim")