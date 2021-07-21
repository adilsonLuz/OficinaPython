def altera(par_str):
    if ( par_str == ""):
        return ""

    pos_final = len(par_str)
    parte1 = ""
    parte2 = ""

    # extrai a primeira parte
    for cont in range(0, pos_final, 2):
        parte1 += par_str[cont]

    # extrai a segunda parte
    for cont in range(1, pos_final, 2):
        parte2 += par_str[cont]

    nova = parte1 + parte2
    return nova

    print(" String modificada final: ", nova)

#--------------------------------------------------------------
# Programa principal
#--------------------------------------------------------------
string = "a"

while (string != "" ):
    print("\n\n-----------------------------------------------------------------\n")
    string = input("informe uma string : ")
    string_alt = altera(string)

    print("\n string informada = ", string)
    print(" string alterada = ", string_alt)


print("Fim")


