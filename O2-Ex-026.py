lista = [ "b", "d", "c", "a", "z", "f", "x"]
print("\n lista  ")
print(lista)

lista.sort()
print("\n lista ordenada ")
print(lista)

lista.reverse()
print("\n lista com ordem inversa ")
print(lista)

lista2 = [ "b", "d", "c", "1", "2", "a", "z", "f", "x"]
print("\n\n\n lista  2")
print(lista2)
lista2.sort()
print("\n Lista 2 ordenada \n", lista2)


lista3 = [ "b", 32, "d", "c", "1", "2", 29, "a", "z", "f", "x"]
#lista3.sort()   --> dá erro se houver tipos diferentes
