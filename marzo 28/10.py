#hacer tablero de busca minas 10x10 donde:
#B es la bomba
#0 las posiciones donde no hay bombas cerca
#especificar el numero de bombas al rededor de cada espacio ???????????
#el usuario debe introducir el numero de minas que desea invocar

import numpy as np
import random

tablero = []
fila = []
columna = []

espacio_con_bomba = []


print('\n')
numero_de_minas = int(input("digite el numero de minas que desea invocar : "))
print(" ")


#generar tablero
for fila_en_tablero in range(1, 11):
    for columna_en_fila in range(1, 11):
        columna.append("*")
    fila.append(columna)
    tablero.append(fila)
    columna = []
    fila = []


#posiciones sin bombas
for filas in tablero:
    for columnas in filas:
        columnas[random.randrange(0,len(columnas))]="0"

#posiciones con minas
for filas in tablero:
    for columnas in filas:
        columnas[random.randrange(0,numero_de_minas)]="M"

    

#imprimir tablero con las modificaciones realizadas
for filas in tablero:
    for columnas in filas:
        print(*columnas, sep = " ")


