import pandas as pd

excel_data_df = pd.read_excel("02-Plan-A.xls")
print("\n-----------------  [ planilçha inicial  ]  --------------------------\n")
print(excel_data_df)
print("\n\n\n-----------------  [ Nomes  ]  --------------------------\n")
lista_nomes = excel_data_df["Nome"]
for nome in lista_nomes:
    print(nome)
print("\n---------------------------------------------")

print("\n-----------------  [ Salários  ]  --------------------------\n")
#excel_data_df[['Nome','Salário']
salarios = excel_data_df["Salário"]
print(salarios)
print("\n---------------------------------------------")


print("\n-----------------  [ Novos Salários  ]  --------------------------\n")
salarios_novos = salarios * 1.20
print(salarios_novos)
print("\n---------------------------------------------")

print("\n\n\n---------------  [ planilha original ]      -----------------------------")
print(excel_data_df[['Nome','Salário']])


print("\n\n Fim")