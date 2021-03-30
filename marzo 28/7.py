# calcular suma de vector 100

import numpy as np
import random

vector = []
for random_num in range(1, 101):
    random_num = random.randint(1, 101)
    vector.append(random_num)

vector_longitud = np.array(vector)
vector_suma = vector_longitud.sum()


vector_media_longitud = len(sorted(vector))
vector_media = round(sum(vector)*1.0/vector_media_longitud, 2)

print("Vector de 100 elementos : "+str(vector))
print("Suma del vector : "+str(vector_suma))
print("Media del vector : "+str(vector_media))
