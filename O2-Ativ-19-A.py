import time

def soma():
    print("\nSoma\n")
    num1=int(input("Informe um número : "))
    num2=int(input("Informe um outro número : "))
    print("Soma dos números:", num1 + num2)


def multiplica():
    print("\nMultiplicação\n")

    num1 = int(input("Informe um número : "))
    num2 = int(input("Informe um outro número : "))
    print("Multiplicação dos números:", num1 * num2)

def medias():
    print("\n\n\n------------ [ Médias ]  -----------------------------\n")
    print("11 - Média Aritmética")
    print("12 - Média Ponderada")
    print("------------------------------------------------------------")

    opcao = int(input("Informe a opção da média: "))
    if opcao == 11:
        media_simples()
    elif opcao == 12:
        media_ponderada()

    print("Fim da função geral das médias")


def media_simples():
    print("\n\n -----------------------------------------")
    print("  [ Média Simples ] \n")
    num1 = int(input("Informe um número : "))
    num2 = int(input("Informe um outro número : "))
    media =  ( num1 + num2 ) / 2


    print("numeros:", num1, " e " , num2)
    print("media dos numeros:", media)
    print("-----------------------------------------")

def media_ponderada():
    print("\n\n -----------------------------------------")
    print("  [ Média ponderada ] \n")
    numero1 = int(input("Informe um número : "))
    numero2 = int(input("Informe um outro número : "))
    mediap = (numero1 * 0.4 + numero2 * 0.6)
    print("-----------------------------------------")
    print("numeros:", numero1, " e " , numero2)
    print("media ponderada dos numeros:", mediap)
    print("-----------------------------------------")


# Programa principal
condicao = True

while condicao:
    print("\n\n\n-----------------------------------------")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Multiplicação")
    print("3 - Médias ")
    print("-----------------------------------------------")

    opcao = int(input("Informe uma opção: "))
    if opcao == 1:
        soma()
    elif opcao == 2:
        multiplica()
    elif opcao == 3:
        medias()
    elif opcao ==0:
        condicao = False
    else:
        print("Opção inválida")

    print("Voltando para  programa principal")
    time.sleep(5)

print("\n Fim")
