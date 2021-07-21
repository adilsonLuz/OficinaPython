import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls", sheet_name='Func')
print("2-Plan-A.xls - Aba Func")
print("-------------- [ nome - 3 primeiros ] -----------------------------------")
print(excel_df['Nome'].head(3))
print("-------------------------------------------------")

print("\n\n -------------- [ nome, salário - 5 primeiros ] -----------------------------------")
print(excel_df[['Nome','Salário']].head(5))
print("-------------------------------------------------\n\n\n")


excel_df2 = pd.read_excel("02-Plan-A.xls", sheet_name='Depart')
print("2-Plan-A.xls - Aba Depart")
print(excel_df2['Departamento'].head(2))
print("-------------------------------------------------\n")
#Outra forma, apenas quando se usar uma coluna
print("Outra forma de selecionar uma coluna")
print(excel_df2.Departamento.head(3))
print("-------------------------------------------------\n")

print("\n\n Fim")