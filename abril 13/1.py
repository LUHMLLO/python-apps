# crear un algoritmo que
# almacene de 30 numeros random sin repetir del 1 al 50
# seleccionar metodos de busqueda: lineal o binaria

# debe introducir el numero que desea buscar
# y presentar la posicion donde se encuentra

# el programa debe seguir corriendo hasta que
# el usuario desee salir

# nota: se debe imprimir el array
# despues de que se generen los numeros
###################################################################################################


import random

basededatos = []


###################################################################################################


def generar_numero_random():
    generar_numero_random.num = random.randint(1, 50)


def verificar_existencia(num):
    if num in basededatos:
        generar_numero_random()
    else:
        basededatos.append(num)


###################################################################################################


def busqueda_lineal(lista, x):
    for num in lista:
        if num == x:
            return lista.index(num)
    return -1


def busqueda_binaria(lista, x, major, minor=0):
    if major >= minor:
        mid = minor + (major - minor) // 2

        if lista[mid] == x:
            return mid
        elif lista[mid] > x:
            return busqueda_binaria(lista, x, mid - 1, minor)
        else:
            return busqueda_binaria(lista, x, major, mid + 1)

    else:
        return -1

###################################################################################################


def verificar_existencia_del_numero_en_la_basededatos(resultado, buscado):
    if resultado != -1:
        print("El numero "+str(buscado) +
              " se encuentra en la posicion "+str(resultado))
    else:
        print("El numero "+str(buscado)+" no se encuentra en la lista")

    print('\n')
    print("[para finalizar el programa escriba 'FIN']")
    iniciar_buscador()


###################################################################################################


def esNumero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False


def esTexto(numero):
    try:
        str(numero)
        return True
    except ValueError:
        return False


###################################################################################################


def iniciar_basededatos():
    while len(basededatos) < 30:
        generar_numero_random()
        verificar_existencia(generar_numero_random.num)
    basededatos.sort()
    print('\n')
    print(len(basededatos), "numeros encontrados en la base de datos")
    print(basededatos)


def seleccionar_metodo():
    print('\n')
    print("Seleccione el metodo de busqueda que desea utilizar [0,1]")
    print("[0] - Lineal")
    print("[1] - Binaria")
    seleccionar_metodo.metodo_seleccionado = int(input("Opcion: "))


def iniciar_buscador():
    print('\n')
    print("Que numero desea buscar en la lista?:")

    capturar_input = input("Numero : ")

    if esNumero(capturar_input):
        numero_buscado = int(capturar_input)

        if seleccionar_metodo.metodo_seleccionado == 0:
            print("[utilizando busqueda lineal]")
            resultado = busqueda_lineal(basededatos, numero_buscado)

        if seleccionar_metodo.metodo_seleccionado == 1:
            print("[utilizando busqueda binaria]")
            resultado = busqueda_binaria(
                basededatos, numero_buscado, len(basededatos) - 1)

        verificar_existencia_del_numero_en_la_basededatos(
            resultado, numero_buscado)

    elif esTexto(capturar_input) and capturar_input.lower() == "fin":
        finalizar_programa()
    else:
        iniciar_buscador()


def finalizar_programa():
    print('\n')
    print("Finalizando programa...")


###################################################################################################


iniciar_basededatos()
seleccionar_metodo()
iniciar_buscador()
