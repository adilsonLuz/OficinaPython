

def prestacao(valor, qtde_parc):
    v_prest = ( valor / qtde_parc ) * 1.05
    print("-----------------------------------------")
    print("valor do crediário:", valor )
    print("Qtde de parcelas :", qtde_parc)
    print("Valor mensal da parcela :", v_prest)

    print("-----------------------------------------")


# Programa principal
print("Programa principal \n")

cred = int(input("Informe o valor do crediário: "))
qtde = int(input("Informe a quantidade de parcelas: "))

prestacao(cred, qtde)
print("\n\n")
print("---------------[ outro cálculo ] -----------------------\n\n")
prestacao(1000, 10)

print("\n Fim")
