import random

v_tupla1 = ("aa", "bb", "cc", "dd" , "ee", "ff")

v_copia_inicial = v_tupla1
v_nova_tupla = ()

qtde = len(v_tupla1)

print("tupla inicial = ",v_tupla1)

for cont in range(1, qtde+1):
    sorteio = random.randrange(len(v_tupla1))
    v_nova_tupla = v_nova_tupla[:] + v_tupla1[sorteio:sorteio+1]

    v_tupla1 = v_tupla1[:sorteio] + v_tupla1[sorteio + 1:]
    print("tupla original ajustada = ", v_tupla1)
    print("nova tupla (parcial) : ", v_nova_tupla)
    print("------------------------------------------------------------------------------------")

print("\n\n\n===================================================================================")
print("tupla inicial = ",v_copia_inicial)
print("nova tupla = ", v_nova_tupla)
print("===================================================================================")
print("\nFim")

