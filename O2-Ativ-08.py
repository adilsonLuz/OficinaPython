
v_tupla1 = ("123", "abc", "def", "45" , "7890", "ghi")

qtde = len(v_tupla1)

print("tupla inicial = ",v_tupla1)

for cont in range(qtde-1,-1,-1):
    v_str_aux = v_tupla1[cont]
    #print(v_str_aux)
    qtde2 = len(v_str_aux)
    str_inv = ""
    for cont2 in range(qtde2-1,-1,-1):
        str_inv = str_inv + v_str_aux[cont2]
    print(str_inv)


print("\nFim")

