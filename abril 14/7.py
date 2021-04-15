# Name: Franklin Junior Blanco Aquino
# ID: 1014-1034
# Exercise : 7

# imprimir todas las permutaciones de una cadena
# sin el usa de recursivas

from itertools import permutations

print('\n')
print("Una cadena que sera permutada")

cadena = input("Cadena : ")

print([''.join(p) for p in permutations(cadena)])
print('\n')
