def conta_palavra(arquivo, lista_palav):
    dic_palavras = {}
    for palavra in lista_palav:
        dic_palavras[palavra] = 0

    #print(dic_palavras)

    try:
        with open(arquivo, 'r') as arq:

            for linha in arq:
                #print("\n",linha)
                frase = linha.split()
                #print("Split")
                #print(frase)
                for palavra in frase:
                    if palavra in dic_palavras:
                        #print("Dicionario tem ", palavra)
                        dic_palavras[palavra] = dic_palavras[palavra] + 1

            arq.close()

    except IOError:
        print("Erro ao ler arquivo.")

    return dic_palavras

#-----------------------------------------------------------
# Leitura de uma lista de palavra
#------------------------------------------------------------
def monta_lista():
    lista_palavra = []
    leitura = True
    while leitura:
        palavra = input("\nInforme uma palavra para busca: ")
        if palavra == "":
            leitura = False
        else:
            lista_palavra.append(palavra)
    return lista_palavra

#----------------------------------------------------------------
# Programa Principal
#----------------------------------------------------------------
nome_arq = input("Informe o nome do arquivo:")
lista_pal = monta_lista()
dic_contagem = conta_palavra(nome_arq, lista_pal)

print("Contagem das palavras:")
print(dic_contagem)
print("\n\n Fim")
