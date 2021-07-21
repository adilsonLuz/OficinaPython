

print("\n\n Escrevendo conteúdo da lista no arquivo..... ")

#arquivo = open('arquivo31.txt', 'w')
#arquivo.write("\nzzzzzzzzzzzzzzzzzzzzzz")
#arquivo.write("\neeeeeeeeeeeeeeeeeeeeeen")
#arquivo.close()

#-------------------------------------------------------------------
# Adicionar conteúdo ao final
#-------------------------------------------------------------------
arquivo = open('arquivo31.txt', 'a')
arquivo.write("\n\n  Texto adicionado (Novo ) \n\n ")

arquivo.write("\n1111111111 [ novo ] 1111111")
arquivo.write("\n222222222222222222")

arquivo.write("\n\nxxxxxxxxx")
arquivo.write("\nyyyyyyy")
arquivo.close()

print("\n\n Fim")