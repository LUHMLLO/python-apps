# crear un algoritmo que
# almacene de 60 numeros random sin repetir del 1 al 100

# seleccionar metodos de busque organizacion: insertion, merge, quick o bubble

# nota: se debe imprimir el array
# antes de organizar los numeros
###################################################################################################


import random

basededatos = []


###################################################################################################


def generar_numero_random():
    generar_numero_random.num = random.randint(1, 100)


def verificar_existencia(num):
    if num in basededatos:
        generar_numero_random()
    else:
        basededatos.append(num)


###################################################################################################


def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]

        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        else:
            if lista[j + 1] != key:
                lista[j + 1] = key


def merge_sort():
    return -1


def partition(lista, low, high):
    i = (low - 1)
    pivot = lista[high]

    for j in range(low, high):
        if lista[j] < pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[high] = lista[high], lista[i + 1]
    return i + 1


def quick_sort(lista, high, low=0):
    if low < high:
        pi = partition(lista, low, high)
        quick_sort(lista, pi - 1, low)
        quick_sort(lista, high, pi + 1)


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

###################################################################################################


def iniciar_basededatos():
    while len(basededatos) < 60:
        generar_numero_random()
        verificar_existencia(generar_numero_random.num)
    print('\n')
    print(len(basededatos), "numeros encontrados en la base de datos")
    print(basededatos)


def seleccionar_metodo():
    print('\n')
    print("Seleccione el metodo de ordenacion que desea utilizar [0,1]")
    print("[0] - Insertion Sort")
    print("[1] - Merge Sort")
    print("[2] - Quick Sort")
    print("[3] - Bubble Sort")
    seleccionar_metodo.metodo_seleccionado = int(input("Opcion: "))


def iniciar_sort():
    print('\n')
    if seleccionar_metodo.metodo_seleccionado == 0:
        print("[utilizando insertion sort]")
        insertion_sort(basededatos)
        print(basededatos)

    if seleccionar_metodo.metodo_seleccionado == 1:
        print("[utilizando merge sort]")

    if seleccionar_metodo.metodo_seleccionado == 2:
        print("[utilizando quick sort]")
        quick_sort(basededatos, len(basededatos) - 1)
        print(basededatos)

    if seleccionar_metodo.metodo_seleccionado == 3:
        print("[utilizando bubble sort]")
        bubble_sort(basededatos)
        print(basededatos)


###################################################################################################


iniciar_basededatos()
seleccionar_metodo()
iniciar_sort()
