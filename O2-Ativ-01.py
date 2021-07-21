par = 0
impar = 0

for cont in range(1,11):
    num = int(input("Informe o número : "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(" Par = " , par)
print(" Impar = " , impar)

print("Fim")