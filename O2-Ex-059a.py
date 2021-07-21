import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
print(excel_df)
print("\n------------- A) sort - salario ------------------------")

print(excel_df.sort_values('Salário', ascending=True).head(11))
print("-------------------------------------------------\n\n\n")


print("\n------------- B) sort - salario ------------------------")
print(excel_df.sort_values('Salário', ascending=False).head(11))
print("-------------------------------------------------\n\n\n")




print("-------------------------------------------------\n")


print("\n\n Fim")