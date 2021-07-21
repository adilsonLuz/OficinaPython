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
def cria_lista_par_impar(lista, par):
    lista_par_impar = []
    qtde = len(lista)
    if par:
        resto = 0
    else:
        resto = 1

    for cont in range(0, qtde):
        if (lista[cont] % 2 == resto):
            lista_par_impar.append(lista[cont])

    return lista_par_impar


#----------------------------------------------------------------
#Principal
#----------------------------------------------------------------

lista1 = cria_lista_rand(9)
print("-"*70)
print("\n lista gerada: ", lista1)
print("\n lista com numeros pares: ", cria_lista_par_impar(lista1, True))
print("\n lista com numeros ímpares: ", cria_lista_par_impar(lista1, False))
print("-"*70)


lista1 = cria_lista_rand(5)
print("\n\n")
print("-"*70)
print("\n lista gerada: ", lista1)
print("\n lista com numeros pares: ", cria_lista_par_impar(lista1, True))
print("\n lista com numeros ímpares: ", cria_lista_par_impar(lista1, False))
print("-"*70)

print("\nFim")

