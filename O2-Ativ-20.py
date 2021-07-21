import time

def qtde_vogal(texto_str, vogal):
    qtde = 0
    for letra in texto_str:
        if ( letra == vogal):
            qtde += 1

    print("-----------------------------------------")
    print("String:", texto_str)
    print("Qtde da vogal ", vogal, " na string: ", qtde)
    print("-----------------------------------------")



# Programa principal
condicao = True
str = input("Informe um texto : ")

while condicao:
    print("\n\n\n-----------------------------------------")
    print("0 - Sair")
    print("a - Qtde de vogal a")
    print("e - Qtde de vogal e")
    print("i - Qtde de vogal i")
    print("o - Qtde de vogal o")
    print("u - Qtde de vogal u")
    print("f - para finalizar ")
    print("-----------------------------------------")

    opcao = input("Informe uma opção: ")
    if opcao == "a":
        qtde_vogal(str, "a")
    elif opcao =="e":
        qtde_vogal(str, "e")
    elif opcao == "i":
        qtde_vogal(str, "i")
    elif opcao == "o":
        qtde_vogal(str, "o")
    elif opcao == "u":
        qtde_vogal(str, "u")
    elif opcao == "f":
        condicao = False
    else:
        print("Opção inválida")

    time.sleep(5)

print("\n Fim")
