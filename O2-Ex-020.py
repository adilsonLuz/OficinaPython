lista =  [ "a","teste","c" ]

print("\n lista ")
print(lista)

for item in lista:
    print(item)

print("Posição 1 alterada com conteúdo 'b' ")
lista[1]= "b"
print("Adicionado item com conteúdo 'h' ")
lista.append("h")
print("Adicionado item com conteúdo 'l' ")
lista.append("l")
print("\n lista  - alterada")
print(lista)
