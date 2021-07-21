def palavras_arquivo(arquivo):

    dic_palavras = { }

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
                    else:
                        dic_palavras[palavra] = 1

            arq.close()
        return dic_palavras

    except IOError:
        print("Erro ao ler arquivo.")

#----------------------------------------------------------------
# Programa Principal
#----------------------------------------------------------------
nome_arq = input("Informe o nome do arquivo:")

palavras = palavras_arquivo(nome_arq)

print("\n\n Resultado da análise do arquivo: " , nome_arq)
print(palavras)


