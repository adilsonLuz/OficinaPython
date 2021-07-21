def inverte(var_str):
    if ( var_str == ""):
        return ""

    pos_final = len(var_str) - 1
    nova_str = ""

    for cont in range(0, pos_final+1):
        nova_str = var_str[cont] + nova_str

    return nova_str

#--------------------------------------------------------------
# Programa principal
#--------------------------------------------------------------
string = "a"

while (string != "" ):
    print("\n\n-----------------------------------------------------------------\n")
    string = input("informe uma string : ")
    string_inv = inverte(string)

    print("\n string informada = ", string)
    print(" string invertida = ", string_inv)

print("Fim")
