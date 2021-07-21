def conta_vogal(arquivo):

    dic_letras = { "a":0, "e":0, "i":0, "o":0, "u":0}

    #arq = open(arquivo, 'r')
    try:
        with open(arquivo, 'r') as arq:
            for linha in arq:
                # print(linha)
                # print("letras")
                for letra in linha:
                    # print(letra)
                    if ('a' == letra) or ('A' == letra):
                        dic_letras['a'] = dic_letras['a'] + 1
                    elif ('e' == letra) or ('E' == letra):
                        dic_letras['e'] = dic_letras['e'] + 1
                    elif ('i' == letra) or ('I' == letra):
                        dic_letras['i'] = dic_letras['i'] + 1
                    elif ('o' == letra) or ('O' == letra):
                        dic_letras['o'] = dic_letras['o'] + 1
                    elif ('u' == letra) or ('U' == letra):
                        dic_letras['u'] = dic_letras['u'] + 1
            arq.close()


    except IOError:

        print("Erro ao ler arquivo.")

    return dic_letras

#----------------------------------------------------------------
# Programa Principal
#----------------------------------------------------------------
nome_arq = input("Informe o nome do arquivo:")
dic_contagem = conta_vogal(nome_arq)
print("Contagem:")
print(dic_contagem)

print("\n\n Fim")