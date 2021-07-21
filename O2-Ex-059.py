import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
print(excel_df)
print("\n-------------  sort - salario ------------------------")

print(excel_df.sort_values('Salário').head(7))
print("-------------------------------------------------\n\n\n")


print("\n-------------  sort - Nome ------------------------")

print(excel_df.sort_values('Nome'))
print("-------------------------------------------------\n\n\n")


print("\n-------------  sort - Departamento + Nome ------------------------")

df_aux = excel_df.sort_values(['Departamento','Nome'])

print(df_aux.head(8))



print("-------------------------------------------------\n")


print("\n\n Fim")