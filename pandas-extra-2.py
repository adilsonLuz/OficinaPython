import pandas as pd

excel_data_df = pd.read_excel("02-Plan-A.xls")
print("\n-----------------  [ planilha inicial  ]  --------------------------\n")
print(excel_data_df)


excel_data_df["Salário"] = excel_data_df["Salário"] * 1.20


print("\n\n\n---------------  [ Lista dos novos salarios  ]   -----------------------------")
print(excel_data_df[['Nome','Salário']])




print("\n\n Fim")