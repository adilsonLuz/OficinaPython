def altera(par_tupla):
    v_nova_tupla = ()

    qtde = len(par_tupla)

    for cont in range(qtde-1,-1,-1):
        v_nova_tupla = v_nova_tupla + par_tupla[cont:cont+1]

    return v_nova_tupla

#--------------------------------------------------------------
# Programa principal
#--------------------------------------------------------------
v_tupla1 = ("123", "abc", "def", "45" , "7890", "ghi")
v_tupla_alt = altera(v_tupla1)

print("\n\n\n===================================================================================")
print("tupla inicial = ",v_tupla1)
print("nova tupla (invertida) : ", v_tupla_alt)
print("===================================================================================")
print("\nFim")

