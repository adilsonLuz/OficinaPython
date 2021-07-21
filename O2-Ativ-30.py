dic_palavras = { "Linha":0, "teste2":0}
print(dic_palavras)

arquivo = open('teste.txt', 'r')
for linha in arquivo:
    print("\n",linha)
    frase = linha.split()
    print("Split")
    print(frase)
    for palavra in frase:
        if palavra in dic_palavras:
            print("Dicionario tem ", palavra)
            dic_palavras[palavra] = dic_palavras[palavra] + 1



arquivo.close()
print("\n\n Resultado da analise")
print(dic_palavras)
print("\n\n Fim")
