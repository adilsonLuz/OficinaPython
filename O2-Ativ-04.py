var_str = input("informe uma string : ")
pos_final = len(var_str) - 1
nova_str = ""

# comando for descrescente
for cont in range(10, 0,-1):
    print(" cont = ", cont)


for cont in range(pos_final, -1, -1):
    print("posicao ", cont, "  letra=", var_str[cont])
    nova_str += var_str[cont]
    print(" string invertida parcial = ", nova_str)

print(" string informada = ", var_str)
print(" string invertida = ", nova_str)

# segunda forma
print("\n\n\n Segunda forma ")
nova_str =""
for cont in range(0, pos_final+1):
    print("posicao ", cont, "  letra=", var_str[cont])
    nova_str = var_str[cont] + nova_str
    print(" string invertida parcial = ", nova_str)

print(" string informada = ", var_str)
print(" string invertida = ", nova_str)

print("Fim")
