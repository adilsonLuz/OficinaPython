lista =  [ 1,2,3 ,4, 5, 6 , 7 , 8, 9, 10]
lista2 = [ 11, 12, 13 ]
lista3 = [ 100, 120 ]
print("\n Lista (1) original=", lista)
print("\n Lista (2) a ser incluída=", lista2)

lista.extend(lista2)

print("\n lista (1) com acrescimo da lista (2) ")
print(lista)

#outra forma de juntar listas
print("\nLista 3", lista3)
lista = lista + lista3
print("Lista 3 adicionada na lista 1", lista)



