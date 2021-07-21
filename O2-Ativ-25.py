import random


#-----------------------------------------------------------------------
def cria_tupla(qtde):

    if qtde==0:
        return ()

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

    for cont in range(1, qtde+1):
        sorteio = random.randrange(len(par_tupla))
        v_nova_tupla = v_nova_tupla[:] + par_tupla[sorteio:sorteio + 1]

        par_tupla = par_tupla[:sorteio] + par_tupla[sorteio + 1:]

    return v_nova_tupla

#-----------------------------------------------------------------------
# Principal
# #-----------------------------------------------------------------------

v_qtde = 1

while (v_qtde != 0 ):
    print("\n\n\n\n---------------------- [ Inicio ] -----------------------------------\n")
    v_qtde = int(input("Informe a quantidade de itens na tupla:"))
    v_tupla1 = cria_tupla(v_qtde)
    v_tupla_alt = altera(v_tupla1)

    print("\n\n")
    print("tupla inicial = ",v_tupla1)
    print("nova tupla (ordem aleatória) : ", v_tupla_alt)
    print("----------------------------------------------------------------------------------")

print("\nFim")

