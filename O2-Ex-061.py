import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
print(excel_df)
print("\n-------------  Vetor Lógico --> Departamento TI ------------------------")

print(excel_df["Departamento"]=="TI")
print("-------------------------------------------------\n\n\n")

dep_TI = excel_df["Departamento"]=="TI"

print("\n-------------  Só Departamento TI ------------------------")

print(excel_df[ dep_TI ])
print("-------------------------------------------------\n\n\n")

print("\n\n Fim")