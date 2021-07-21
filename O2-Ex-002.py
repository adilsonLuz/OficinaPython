condicao=True

while condicao:
    nota = float(input("Informe a sua nota:"))
    if nota != 10:
        condicao = True
        print("Você pode melhorar!")
    else:
        condicao = False
        print("Excelente")

print("Fim")
