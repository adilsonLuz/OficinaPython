
def programa1():
    print("Rodando o Programa 1")

def programa2():
    print("Rodando o Programa 2")

# Programa principal
print("Programa principal \n")

opcao=int(input("Informe a sua opção: "))

if opcao==1:
    programa1()
elif opcao ==2:
    programa2()
else:
    print("Opção inválida")

print("\n Fim")
