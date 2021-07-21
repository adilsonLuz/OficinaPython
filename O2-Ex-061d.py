import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
print(excel_df)


dep_TI = excel_df["Departamento"]=="TI"
dep_Vendas = excel_df["Departamento"]=="Vendas"

print("\n-------------   Departamento TI ou de Vendas ------------------------")

print(excel_df[ dep_TI | dep_Vendas ])
print("-------------------------------------------------\n\n\n")

print("\n\n Fim")