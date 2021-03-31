# crear lista de 50 elementos con numeros random del 0 al 300
# imprimir el menor y el mayor
# calcular el promedio, desviacion, estandar, moda y mediana
# identificar los grupos de 3 que sean adyacentes


import numpy as np
import random

lista_de_50_elementos = []

# generar numeros random
for num in range(50):
    num = random.randint(0, 301)
    lista_de_50_elementos.append(num)


# calcular la media
lista_longitud = len(sorted(lista_de_50_elementos))
media = round(sum(lista_de_50_elementos)*1.0/lista_longitud, 2)


# calcular la mediana
medio = len(sorted(lista_de_50_elementos))/2
if medio % 2 == 0:
    mediana = ((medio/2+1) + (medio/2+2)) / 2
else:
    mediana = (medio/2+1)*1


# calcular la moda
repetir = 0
for i in lista_de_50_elementos:
    aparece = lista_de_50_elementos.count(i)
    if aparece > repetir:
        repetir = aparece

moda = []
for i in lista_de_50_elementos:
    aparece = lista_de_50_elementos.count(i)
    if aparece == repetir and i not in moda:
        moda.append(i)
#

print(" ")
print(sorted(lista_de_50_elementos))
print("Numero menor : "+str(min(lista_de_50_elementos)))
print("Numero mayor : "+str(max(lista_de_50_elementos)))
print("Media : "+str(media))
print("Mediana : "+str(mediana))
print("Moda : "+str(moda))
