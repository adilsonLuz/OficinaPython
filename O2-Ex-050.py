import pandas as pd

df = pd.read_csv("planilha1.csv")
print("planilha1.csv")
print("\n-------------   Head - 3 ------------------------")
print(df.head(3))

print("-------------------------------------------------\n")

print("\n-------------   Tail - 2------------------------")
print(df.tail(2))
print("-------------------------------------------------\n")


print("\n\n Fim")