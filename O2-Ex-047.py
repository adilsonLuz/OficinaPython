nome_arq = input("Informe o nome do arquivo: ")
arquivo = open(nome_arq , 'w')

print("\n\n Escrevendo no arquivo..... ")

arquivo.write("Linha A 1  aaaa\n")
arquivo.write("Linha B 1 \n")
arquivo.write("Linha C 1 \n")


arquivo.close()


print("\n\n Fim")