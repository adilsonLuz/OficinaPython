import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
print(excel_df)


dep_TI = excel_df["Departamento"]=="TI"
sal_maiores = excel_df["Salário"] >= 5000

print("\n-------------  Só Departamento TI ------------------------")

print(excel_df[ dep_TI ])
print("-------------------------------------------------\n\n\n")

print("\n-------------  Só salario > 5000 ------------------------")

print( excel_df[ sal_maiores ] )
print("-------------------------------------------------\n\n\n")

print("\n-------------   Departamento TI com salario >= 5000------------------------")

print(excel_df[ dep_TI & sal_maiores ])
print("-------------------------------------------------\n\n\n")

print("\n\n Fim")