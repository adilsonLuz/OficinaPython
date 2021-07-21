#----------------------------------------------------------------
# opção 1
#----------------------------------------------------------------
def opcao1(arquivo):
    print("\n Opção 1 \n")
    try:
        with open(arquivo, 'r') as arq:
            cont = 1
            for linha in arq:
                print(linha)


            arq.close()

    except IOError:
        print("Erro ao ler arquivo.")


# ----------------------------------------------------------------
# opção 2
# ----------------------------------------------------------------
def opcao2(arquivo):
    print("\n Opção 2 \n")
    try:
        with open(arquivo, 'r') as arq:
            cont = 1
            for linha in arq:
                print(linha)

            arq.close()

    except IOError:
        print("Erro ao ler arquivo.")


#----------------------------------------------------------------
# Programa Principal
#----------------------------------------------------------------
opcao = 0
continua = True
while continua == True:
    print("\n\n\n\n", "=" * 60)

    print("\n[ Opções ] ")
    print("0. Para terminar ")
    print("1. Opção 1")
    print("2. Opção 2")

    opcao = input("\nEscolha a opção:")

    if (opcao != "0"):
        nome_arq = input("\n\n Informe o nome do arquivo para tratamento :")

    if ( opcao == "1"):
        opcao1(nome_arq)
    elif ( opcao == "2"):
        opcao2(nome_arq)
    elif ( opcao == "0"):
        continua = False
    else:
        print("Opção inválida:")

    print("\n","=" * 60)



print("\n\n Fim")
