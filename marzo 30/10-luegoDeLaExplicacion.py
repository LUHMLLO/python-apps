# hacer tablero de busca minas 10x10 donde:
# B = bomba
# 0 = zonas seguras
# M = minas
# el usuario debe introducir el numero de minas que desea invocar

from random import randint


def printBoard(tablero, filas, columnas):
    for fila in range(1, filas - 1):
        for columna in range(1, columnas - 1):
            print(tablero[fila][columna], end=" ")
        print()


def putBomb(tablero, filas, columnas, porcentaje):
    cantidad_de_bombas = 0
    while cantidad_de_bombas != porcentaje:
        for fila in range(1, filas - 1):
            for columna in range(1, columnas - 1):
                ran = randint(1, 100)
                if ran <= porcentaje and tablero[fila][columna] != "B":
                    tablero[fila][columna] = "B"
                    cantidad_de_bombas += 1
                if cantidad_de_bombas == porcentaje:
                    break
            if cantidad_de_bombas == porcentaje:
                break

    for fila in range(1, filas - 1):
        for columna in range(1, columnas - 1):
            valor = tablero[fila][columna]
            if valor == "B":
                for i in range(fila-1, fila+2):
                    for j in range(columna-1, columna+2):
                        inc = tablero[i][j]
                        if inc != "B":
                            tablero[i][j] = inc + 1

    printBoard(tablero, filas, columnas)


def makeBoard(tablero, filas, columnas, porcentaje):
    for i in range(filas):
        tablero.append([0 for j in range(columnas)])

    putBomb(tablero, filas, columnas, porcentaje)


tablero = []
filas, columnas = 10, 10
porcentaje = 25

print("")
makeBoard(tablero, filas + 2, columnas + 2, porcentaje)
print("")
