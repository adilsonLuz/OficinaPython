import pandas as pd

excel_data_df = pd.read_excel("02-Plan-A.xls")
print("Primeiras 4 linhas da planilha")
print(excel_data_df.head(4))

print(excel_data_df.tail(3))

print("\n\n Todas as  linhas da planilha")
print(excel_data_df)


print("\n\n Fim")