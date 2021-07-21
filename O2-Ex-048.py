arquivo = open('arquivo31.txt', 'w')

lista = [ "Item 1 \n", "item 2 \n", "item 3 \n", "item 4 \n"]
print(lista)

lista2 = [ "limão ", "laranja ", "abacate ", "abacaxi "]
print(lista2)

print("\n\n Escrevendo conteúdo das listas no arquivo..... ")
arquivo.writelines("\nlista=\n")
arquivo.writelines(lista)
arquivo.writelines("\n\n A.lista2=\n")
arquivo.writelines(lista2)

arquivo.writelines("\n\n B.lista2=\n")
for fruta in lista2:
    arquivo.writelines(fruta)

arquivo.writelines("\n\n C.lista2=\n")
for fruta in lista2:
    arquivo.writelines(fruta + "\n")

arquivo.writelines("\n\n ------------------------------------ \n")
arquivo.writelines("linha A")
arquivo.writelines("linha B\n Linha C\n Linha D\n")
arquivo.write("1111111 \n 22222222222 \n 33333333333333 \n")
arquivo.writelines("zzzzzzzzzzzzzzzzzzzzzz")
arquivo.writelines("eeeeeeeeeeeeeeeeeeeeeen")

# para gravar conteúdo de uma lista, o método write não pode ser utilizado
#arquivo.write(lista)


arquivo.close()




print("\n\n Fim")