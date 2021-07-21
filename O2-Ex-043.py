
def programa1():
    print("Rodando o Programa 1")

def programa2():
    print("-----------------------------------------")
    print("Rodando o Programa 2\n")
    programa3()
    programa4()
    print("\nTerminando o Programa 2")
    print("-----------------------------------------")

def programa3():
    print("Rodando o Programa 3")

def programa4():
    print("Rodando o Programa 4")

# Programa principal
print("Programa principal \n")

opcao=1
while (opcao != 0):
    opcao=int(input("\n\n Informe a sua opção: "))

    if opcao==1:
        programa1()
    elif opcao ==2:
        programa2()
    else:
        print("Opção inválida")

print("\n Fim")
