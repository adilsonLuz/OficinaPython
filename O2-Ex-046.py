arquivo = open('arquivo-xxxx.txt', 'r')

print("\n\n Outra forma \n\n")

continua = True
while continua:
    linha = arquivo.readline()
    print(linha)
    if (linha==""):
        continua = False

arquivo.close()


print("\n\n Fim")