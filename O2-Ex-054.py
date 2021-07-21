import pandas as pd

excel_df = pd.read_excel("02-Plan-A.xls")
print("2-Plan-A.xls")
#print(excel_df)
#print("\n-------------  Com indice default  ------------------------")
#print(excel_df)
print("-------------------------------------------------\n\n\n")
print("\n-------------  Com indice pelo Nome  ------------------------")
#excel_df.set_index('Departamento', inplace=False)
#print(excel_df)
print(excel_df)

excel_df.set_index('Nome', inplace=False)
print(excel_df)

print("-------------------------------------------------\n")


print("\n\n Fim")