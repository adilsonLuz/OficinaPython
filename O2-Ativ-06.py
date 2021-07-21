var_str = input("informe uma string : ")
pos_final = len(var_str)
parte1 = ""
parte2 = ""

# extrai a primeira parte
for cont in range(0, pos_final, 2):
    parte1 += var_str[cont]

print(" string informada = ", var_str)
print(" parte 1 ", parte1)

# extrai a segunda parte
for cont in range(1, pos_final, 2):
    parte2 += var_str[cont]

print(" parte 2 ", parte2)

nova = parte1 + parte2
print(" String modificada final: ", nova)

print("Fim")
