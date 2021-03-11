print("")
print("La unica forma de abandonar este programa es si la suma de ambos resultados es negativa")


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


def esTexto(numero):
    try:
        str(numero)
        return True
    except ValueError:
        return False


def verificar_numeros():
    if esEntero(capturar_datos.valor_1) and esEntero(capturar_datos.valor_2):
        verificar_numeros.suma = int(capturar_datos.valor_1) + int(capturar_datos.valor_2)
        verificar_salida()

    elif esDecimal(capturar_datos.valor_1) and esDecimal(capturar_datos.valor_2):
        verificar_numeros.suma = float(capturar_datos.valor_1) + float(capturar_datos.valor_2)
        verificar_salida()

    elif esDecimal(capturar_datos.valor_1) and esEntero(capturar_datos.valor_2):
        verificar_numeros.suma = float(capturar_datos.valor_1) + int(capturar_datos.valor_2)
        verificar_salida()

    elif esEntero(capturar_datos.valor_1) and esDecimal(capturar_datos.valor_2):
        verificar_numeros.suma = int(capturar_datos.valor_1) + float(capturar_datos.valor_2)
        verificar_salida()

    elif esTexto(capturar_datos.valor_1) or esTexto(capturar_datos.valor_2):
        print("digito texto en vez de 2 numeros : " +str(capturar_datos.valor_1)+" "+str(capturar_datos.valor_2))
        capturar_datos()

    else:
        print("digito texto en vez de 2 numeros : " +str(capturar_datos.valor_1)+" "+str(capturar_datos.valor_2))
        capturar_datos()


def capturar_datos():
    capturar_datos.valor_1 = input("Valor 1 = ")
    capturar_datos.valor_2 = input("Valor 2 = ")
    verificar_numeros()


def verificar_salida():

    if verificar_numeros.suma < 0:
        print("El resultado es negativo : "+str(verificar_numeros.suma))
        print("Abandonando programa...")
    else:
        print("El resultado es positivo : "+str(verificar_numeros.suma))
        capturar_datos()


capturar_datos()
