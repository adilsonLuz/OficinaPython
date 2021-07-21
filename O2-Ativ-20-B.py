import time

def qtde_vogal(texto_str, vogal):
    qtde = 0
    for letra in texto_str:
        if ( letra == vogal):
            qtde += 1
    return qtde


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
    resposta = ""

    if opcao == "f":
        condicao = False
    elif opcao in "a#e#i#o#u":
        opc_valida = True
    else:
        print("Opção inválida")
        opc_valida = False

    if condicao and opc_valida:
        resposta = qtde_vogal(str, opcao)
        if str != "":
            print("A string", str, " tem ", resposta, " ", opcao)
            time.sleep(5)

print("\n Fim")
