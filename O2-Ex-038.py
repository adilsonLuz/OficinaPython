lista = [ "alberto" , "roberto" , "luiz", "ricardo" , "pamela" ]

dicionario = dict.fromkeys( lista, 0 )

print("Lista: \n",lista)
print("\n Dicionário criado a partir da lista : \n",dicionario)

print("Luiz=",dicionario["luiz"])

dicionario["luiz"] = 7.0
print("\n\nAlteração do valor do Luiz.")
print("Luiz=",dicionario["luiz"])

print("Dicionario: ",dicionario)

print("\n\n Fim")






