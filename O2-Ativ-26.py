# Python
import random

#-----------------------------------------------------------------------
def cria_lista_rand(qtde):
    lista_num = []
    for cont in range(0, qtde):
        num = random.randrange(1, 101)
        lista_num.append(num)

    return lista_num

#----------------------------------------------------------------
def cria_lista_par(lista):
    lista_par = []
    qtde = len(lista)
    for cont in range(0, qtde):
        if (lista[cont] % 2 == 0):
            lista_par.append(lista[cont])

    return lista_par

#----------------------------------------------------------------
def cria_lista_impar(lista):
    lista_impar = []
    qtde = len(lista)
    for cont in range(0, qtde):
        if (lista[cont] % 2 == 1):
            lista_impar.append(lista[cont])

    return lista_impar

#----------------------------------------------------------------
#Principal
#----------------------------------------------------------------

lista1 = cria_lista_rand(10)
print("-"*70)
print("\n lista gerada: ", lista1)
print("\n lista com numeros pares: ", cria_lista_par(lista1))
print("\n lista com numeros ímpares: ", cria_lista_impar(lista1))
print("-"*70)


lista1 = cria_lista_rand(6)
print("\n\n")
print("-"*70)
print("\n lista gerada: ", lista1)
print("\n lista com numeros pares: ", cria_lista_par(lista1))
print("\n lista com numeros ímpares: ", cria_lista_impar(lista1))
print("-"*70)

print("\nFim")

