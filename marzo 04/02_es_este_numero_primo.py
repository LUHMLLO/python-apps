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


def esPrimo(numero):
    if numero < 1:
        return False
    else:
        for primo in range(2, numero):
            if numero % primo == 0:
                return False
        return True


if esEntero(numero_entero):
    print(" ")
    print("el numero que digitaste es : "+str(numero_entero))
    if esPrimo(int(numero_entero)):
        print("Es un numero primo")
    else:
        print("No es un numero primo")


elif esDecimal(numero_entero):
    print("El numero que digito es un decimal : "+str(numero_entero))

else:
    print("digito texto en vez de un numero(entero) : "+str(numero_entero))
