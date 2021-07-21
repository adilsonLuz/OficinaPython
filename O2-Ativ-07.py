var_str = input("informe uma string : ")
compr = len(var_str)
if compr % 2 == 0:
    meio = int(compr / 2)
    par = True
    print('Par')
else:
    meio = int(compr / 2) + 1
    par = False
    print('Impar')

print("Comprimento = ", compr, "   meio = ", meio)

nova_str = ""
parte1 = ""
parte2 = ""

# parte 1
for cont in range(0, meio):
    letra = var_str[cont]
    parte1 += letra

print("A) ", parte1)

# parte 2
for cont in range(meio, compr):
    letra = var_str[cont]
    parte2 += letra

print("B) ", parte2)

# final - mescla da parte 1 e da parte 2
if par:

    for cont in range(0, meio):
        letra1 = parte1[cont]
        letra2 = parte2[cont]
        nova_str += letra1 + letra2
else:
    for cont in range(0, meio-1):
        letra1 = parte1[cont]
        letra2 = parte2[cont]
        nova_str += letra1 + letra2

    nova_str +=  parte1[meio-1]

print(" string informada = ", var_str)
print(" string gerada com intercalacao= ", nova_str)


print("Fim")
