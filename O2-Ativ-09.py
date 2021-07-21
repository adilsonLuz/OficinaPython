

v_tupla1 = ("123", "abc", "def", "45" , "7890", "ghi")
v_nova_tupla = ()

qtde = len(v_tupla1)

print("tupla inicial = ",v_tupla1)

for cont in range(qtde-1,-1,-1):
    print("Extração =", v_tupla1[cont:cont+1])
    v_nova_tupla = v_nova_tupla[:] + v_tupla1[cont:cont+1]
    print("nova tupla (parcial) : ", v_nova_tupla)
    print("------------------------------------------------------------------------------------")

print("\n\n\n===================================================================================")
print("tupla inicial = ",v_tupla1)
print("nova tupla : ", v_nova_tupla)
print("===================================================================================")
print("\nFim")

