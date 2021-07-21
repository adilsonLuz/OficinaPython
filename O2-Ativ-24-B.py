
#-----------------------------------------------------------------------
def cria_tupla(qtde):
    nomes = ()

    for cont in range(1, qtde + 1):
        entrada = input(str(cont) + "- Informe um nome:")

        tupla_entrada = (entrada,)
        nomes = nomes + tupla_entrada

    return nomes

#-----------------------------------------------------------------------
def altera(par_tupla):
    v_nova_tupla = ()

    qtde = len(par_tupla)

    for cont in range(qtde-1,-1,-1):
        v_nova_tupla = v_nova_tupla + par_tupla[cont:cont+1]

    return v_nova_tupla

#--------------------------------------------------------------
# Programa principal
#--------------------------------------------------------------
v_tupla1 = cria_tupla(5)
v_tupla_alt = altera(v_tupla1)

print("\n\n\n===================================================================================")
print("tupla inicial = ",v_tupla1)
print("nova tupla (invertida) : ", v_tupla_alt)
print("===================================================================================")
print("\nFim")

