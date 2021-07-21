num = 1
par: int = 0
impar: int = 0

while num != 0:
    num = int(input("Informe um número: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(" o resultado da soma \n dos numeros Par = " , par)
print(" Impar = " , impar)
print("Fim")
