# calcular el numero de elementos negativos, cero y positivos de un vector dado de 60 elementos

import numpy as np
import random

vector = []

positivos = []
valor_zero = []
negativos = []

for random_num in range(1, 61):
    random_num = random.randint(-61, 61)
    vector.append(random_num)

for num in vector:
    if num > 0:
        positivos.append(num)
    elif num == 0:
        valor_zero.append(num)
    else:
        negativos.append(num)

print("Vector de 60 elementos : "+str(vector))
print("Cantidad de valores positivos: "+str(len(positivos)))
print("Cantidad de valores iguales a 0: "+str(len(valor_zero)))
print("Cantidad de valores negativos: "+str(len(negativos)))
