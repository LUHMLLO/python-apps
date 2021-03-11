print("Digite un numero entero positivo : ")
capturar_numero = input()
numero_entero = capturar_numero
numeros_impares_de_1_al = []


def esEntero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False


def esDecimal(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False


if esEntero(numero_entero):
    if int(numero_entero) > 0:
        print(" ")
        print("el numero que digitaste es un entero positivo : "+str(numero_entero))
        print(" ")
        print("numeros impares del 1 hasta "+str(numero_entero)+":")

        for impar in range(1, int(numero_entero)):
            if impar % 2 != 0:
                numeros_impares_de_1_al.append(str(impar))
        numeros_impares_de_1_al.append(str(numero_entero))
        print(', '.join(numeros_impares_de_1_al))

    else:
        print("El numero que digito no es positivo : "+str(numero_entero))

elif esDecimal(numero_entero):
    print("El numero que digito es un decimal : "+str(numero_entero))

else:
    print("digito texto en vez de un numero(entero positivo) : "+str(numero_entero))
