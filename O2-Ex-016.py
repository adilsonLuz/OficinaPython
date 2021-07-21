# Python
import random

frutas = ( "banana", "laranja", "uva", "morango" , "mamão", "pera", "graviola")
print("todas frutas = ",frutas)

for cont in range(1,21):
    sorteio = random.randrange(len(frutas))
    print("Repetição =", cont)
    print("Sorteio =", sorteio)
    print("Fruta sorteada: ", frutas[sorteio] , "\n", "=" * 40)

#print("\n\n\nparte B")
#for cont in range(1,10):
#    print("Sorteio =", random.randrange(3))  # sorteio dos numeros 0,1 ou 2

print("\nFim")

