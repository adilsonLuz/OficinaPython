import time

def media_simples(num1, num2):
    media =  ( num1 + num2 ) / 2

    print("-----------------------------------------")
    print("numeros:", num1, " e " , num2)
    print("media dos numeros:", media)
    print("-----------------------------------------")

def media_ponderada(num1, num2):
    mediap = (num1 * 0.4 + num2 * 0.6)
    print("-----------------------------------------")
    print("numeros:", num1, " e " , num2)
    print("media ponderada dos numeros:", mediap)
    print("-----------------------------------------")


# Programa principal
condicao = True
numero1 = int(input("Informe um número : "))
numero2 = int(input("Informe um outro número : "))
while condicao:
    print("\n\n\n-----------------------------------------")
    print("0 - Sair")
    print("1 - Média simples")
    print("2 - Média Ponderada")
    print("-----------------------------------------")

    opcao = int(input("Informe uma opção: "))
    if opcao == 1:
        media_simples(numero1, numero2)
        media_simples(4 + 5,8)
    elif opcao == 2:
        media_ponderada(numero1, numero2)
    elif opcao ==0:
        condicao = False
    else:
        print("Opção inválida")

    time.sleep(5)

print("\n Fim")
