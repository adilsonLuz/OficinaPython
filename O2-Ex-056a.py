import pandas as pd

df = pd.read_csv("planilha1.csv")
print("02-Plan-A.csv")
print(df)
print("\n-------------  loc 2 a 5  ------------------------")
print(df.loc[2:5])
print("-------------------------------------------------\n\n\n")
print("\n-------------  loc 3 a 6 ------------------------")
print(df.loc[3:6])
print("-------------------------------------------------\n")
print("-------------------------------------------------\n")


print("\n\n Fim")