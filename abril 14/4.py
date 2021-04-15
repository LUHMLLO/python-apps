# Name: Franklin Junior Blanco Aquino
# ID: 1014-1034
# Exercise : 4


# Leer una variable int por teclado
# esta variable sera la longitud de un triangulo

# ejemplo:
#
# x = 7
#        1
#       1 2
#      1   3
#     1     4
#    1       5
#   1         6
#  1           7
# 1  2 3 4 5 6  7
#


def triangulo(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
     
        for j in range(0, i+1):
            print("* ", end="")
     
        print("\r")


print('\n')
print("Digite el tamaño del triangulo deseado : ")

tablero = []
tamaño = int(input("Tamaño : "))

print('\n')
triangulo(tamaño)
