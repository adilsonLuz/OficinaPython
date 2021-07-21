import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
print(excel_df)
print("\n-------------  loc 2 a 5  ------------------------")
print(excel_df.loc[2:5,['Nome']])
print("-------------------------------------------------\n\n\n")
print("\n-------------  loc 3, 5 e 7 ------------------------")
print(excel_df.loc[[3,5,7],['Nome', 'Departamento']])
print("-------------------------------------------------\n")


print("\n\n Fim")