
from random import randrange

num: int = 0
par: int = 0
impar: int = 0

for cont in range(1,6):
    num = randrange(1, 20)
    print("Numero = ", num )
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(" Par = " , par)
print(" Impar = " , impar)
print("Fim")
