lista =  [ 1,2,3 ,4, 5, 6 , 7 , 8, 9, 10, 11,12,13 ,14, 15, 16 , 17 , 18, 19, 20]
print("\n lista ")
print(lista)

print("\n sublista [0:4:2]  ")
print(lista[0:4:2])

lista[0:4:2] = [ 'X', 'Y']
print("\n lista com alteração da sublista [0:4:2] por [ 'X', 'Y'] ")
print(lista)
