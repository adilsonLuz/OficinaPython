def substitui(par_str, carac1, carac2):
    if ( par_str == ""):
        return ""

    #var_str = input("informe uma string : ")
    pos_final = len(par_str) - 1
    nova_str = ""

    for cont in range(pos_final, -1, -1):
        # print("Cont=", cont)
        letra = par_str[cont]

        if letra == carac1:
            letra = carac2
        elif letra == carac2:
            letra = carac1

        nova_str += letra

    return  nova_str

#--------------------------------------------------------------
# Programa principal
#--------------------------------------------------------------
string = "a"

while (string != "" ):
    print("\n\n-----------------------------------------------------------------\n")
    string = input("informe uma string : ")
    string_inv = substitui(string, 'a', 'o')

    print("\n string informada = ", string)
    print(" string invertida, trocando 'a' e 'o'  = ", string_inv)
    print(" troca a string trocada  = ", substitui(string_inv, 'a', 'o'))

    string_inv = substitui(string, 'e', 'i')
    print(" string invertida, trocando 'e' e 'i'  = ", string_inv)

print("Fim")

