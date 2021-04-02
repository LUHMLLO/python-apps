# hacer tablero de busca minas 10x10 donde:
# B = bomba
# 0 = zonas seguras
# M = minas
# el usuario debe introducir el numero de minas que desea invocar

import numpy as np
import random
import textwrap


tablero = []

print('\n')
numero_de_minas = int(input("digite el numero de minas que desea invocar : "))
print(" ")

# generar tablero
for fila_en_tablero in range(10):
    for columna_en_fila in range(10):
       tablero.append("*")

#zonas seguras

for i in range(random.randint(1, 30)):
    tablero[random.randrange(0,len(tablero))]="0"

#minas
for i in range(numero_de_minas+1):
    tablero[random.randrange(0,len(tablero))]="M"

#bomba
tablero[random.randrange(0,len(tablero))]="B"

#remover parentesis y comas de la lista
tablero_lineal = ''.join(map(str, tablero))
print(textwrap.fill(tablero_lineal, 10))
print("")
print("Cantidad de bombas : "+str(tablero_lineal.count("B")))
print("Cantidad de minas : "+str(tablero_lineal.count("M")))
print("Cantidad de zonas seguras : "+str(tablero_lineal.count("0")))
