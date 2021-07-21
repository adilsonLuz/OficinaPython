
nomes=()

qtde = 3

for cont in range(1,qtde+1):

    entrada = input(str(cont)+ "- Informe um nome:")

    tupla_entrada = (entrada,)
    nomes = nomes + tupla_entrada
    print(nomes)

print("\nitens da tupla")
for cont in range(0,qtde):
    print(nomes[cont])

print("\n\nFim")
