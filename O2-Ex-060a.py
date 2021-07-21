import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
print(excel_df)
print("\n-------------  A) Filtro  ------------------------")

print(excel_df.filter(like = "Nome").head(7))
print("-------------------------------------------------\n\n\n")

print("\n-------------  B) Filtro  ------------------------")

print(excel_df.filter( like = "me").head(7))
print("-------------------------------------------------\n\n\n")

print("\n\n-------------------------------------------------\n")


print("\n\n Fim")