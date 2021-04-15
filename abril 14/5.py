# Name: Franklin Junior Blanco Aquino
# ID: 1014-1034
# Exercise : 5


# Leer una variable int por teclado
# esta variable sera la longitud de un triangulo

# ejemplo:
#
# x = 7
#1 - 1
#2 - 2 3
#3 - 4 5 6
#4 - 7 8 9 10
#5 - 11 12 13 14 15
#
 

def triangulo(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
     
        print("\r")
 

print('\n')
print("Digite el tamaño del triangulo deseado : ")

tamaño = int(input("Tamaño : "))

print('\n')
triangulo(tamaño)
print('\n')
