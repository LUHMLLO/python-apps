print(" ")
print("Digite 5 numeros en enteros")


def esEntero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False


numeros_digitados = []

def capturar_numero_1():
    capturar_numero_1.numero = input("Numero #1 : ")

    if esEntero(capturar_numero_1.numero):
        numeros_digitados.append(int(capturar_numero_1.numero))
    else:
        print("el numero que digito no es un entero, por favor digite nuevamente")
        capturar_numero_1()
    

def capturar_numero_2():
    capturar_numero_2.numero = input("Numero #2 : ")

    if esEntero(capturar_numero_2.numero):
        numeros_digitados.append(int(capturar_numero_2.numero))
    else:
        print("el numero que digito no es un entero, por favor digite nuevamente")
        capturar_numero_2()

def capturar_numero_3():
    capturar_numero_3.numero = input("Numero #3 : ")

    if esEntero(capturar_numero_3.numero):
        numeros_digitados.append(int(capturar_numero_3.numero))
    else:
        print("el numero que digito no es un entero, por favor digite nuevamente")
        capturar_numero_3()

def capturar_numero_4():
    capturar_numero_4.numero = input("Numero #4 : ")

    if esEntero(capturar_numero_4.numero):
        numeros_digitados.append(int(capturar_numero_4.numero))
    else:
        print("el numero que digito no es un entero, por favor digite nuevamente")
        capturar_numero_4()

def capturar_numero_5():
    capturar_numero_5.numero = input("Numero #5 : ")

    if esEntero(capturar_numero_5.numero):
        numeros_digitados.append(int(capturar_numero_5.numero))
    else:
        print("el numero que digito no es un entero, por favor digite nuevamente")
        capturar_numero_5()


capturar_numero_1()
capturar_numero_2()
capturar_numero_3()
capturar_numero_4()
capturar_numero_5()

primer_valor = numeros_digitados[0]
numeros_digitados.remove(numeros_digitados[0])

cercano = float("inf")
for val in numeros_digitados:
    if abs(val - primer_valor) < cercano:
        final_value = val
        cercano = abs(val - primer_valor)
print(final_value)
