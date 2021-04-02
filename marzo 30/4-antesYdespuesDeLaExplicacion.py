# en el ajedrez, la reina posee los siguientes movimientos:
# vertical, horizontal y diagonal
# todos con un alcance de preferencia (ya sea 2 a 3 pasos o el tablero completo)

# escriba un programa que lea:
# una fila y una columna de un table de ajedrez
# el cual determine la posicion de la reina

# despliegue en pantalla en tablero, indicando:
# R = la posicion de la reina
# * las cuadriculas a las cuales la reina se podria mover
# "+" las demas cuadriculas


#import numpy as np

# tablero = np.array([
#    ["+", "*", "*", "*", "+", "+", "+", "+"],
#    ["*", "*", "R", "*", "*", "*", "*", "*"],
#    ["+", "*", "*", "*", "+", "+", "+", "+"],
#    ["+", "*", "*", "+", "*", "+", "+", "+"],
#    ["*", "+", "*", "+", "+", "*", "+", "+"],
#    ["+", "+", "*", "+", "+", "+", "*", "+"],
#    ["+", "+", "*", "+", "+", "+", "+", "*"],
#    ["+", "+", "*", "+", "+", "+", "+", "+"],
# ])

# for fila in tablero:
#    print(*fila, sep = " ")


boards = []


def printBoard(boards):
    for i in boards:
        for j in i:
            print(list(j), end=' ')
        print('\n')


def valid(x, y, i, j):
    if x == i and y == j:
        return "R"
    elif x == i or y == j or abs(x-i) == abs(y-j):
        return "*"
    else:
        return "+"


def solve(x, y):
    boards = []
    for i in range(1, 9):
        boards.append([valid(x, y, i, j) for j in range(1, 9)])

    printBoard(boards)


print("Digite la posicion de la reina (x,y): ")
x = int(input("X : "))
y = int(input("Y : "))
if x < 1 or x > 8 or y < 1 or y > 8:
    print("Coordenada incorrecta")
else:
    solve(x, y)
