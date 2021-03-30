# escribe un programa que imprima la suma y producto de la matriz asignada
#     [2 0 1]      [1 0 1]
# A = [3 0 0]  B = [1 2 1]
#     [5 1 1]      [1 1 0]

import numpy as np

A = np.array([
    [2, 0, 1],
    [3, 0, 0],
    [5, 1, 1]
])

B = np.array([
    [1, 0, 1],
    [1, 2, 1],
    [1, 1, 0]
])

print(A + B)
