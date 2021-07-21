import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
print(excel_df)
print("\n-------------  query salario > 5000 , apenas 3 linhas------------------------")

print(excel_df.query('Salário > 5000 ').head(3))
print("-------------------------------------------------\n\n\n")

print("\n-------------  query salario > 6000 ou < 5000 ------------------------")

print(excel_df.query('Salário > 6000  | Salário < 5000 ' ))
print("-------------------------------------------------\n\n\n")

print("\n-------------  query Codigo_Funcional > 200 , 7 linhas------------------------")
print(excel_df.query('Codigo_Funcional > 200 ').head(7))
print("-------------------------------------------------\n\n\n")


print("-------------------------------------------------\n")


print("\n\n Fim")