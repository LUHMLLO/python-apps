# hacer tablero de busca minas 10x10 donde:
# B = bomba
# 0 = zonas seguras
# M = minas
# el usuario debe introducir el numero de minas que desea invocar

from random import randint


def printBoard(boards, row, column):
    for r in range(1, row - 1):
        for c in range(1, column - 1):
            print(boards[r][c], end=" ")
        print()


def putBomb(boards, row, column, percentage):
    qtyB = 0
    while qtyB != percentage:
        for r in range(1, row - 1):
            for c in range(1, column - 1):
                ran = randint(1, 100)
                if ran <= percentage and boards[r][c] != "B":
                    boards[r][c] = "B"
                    qtyB += 1
                if qtyB == percentage:
                    break
            if qtyB == percentage:
                break

    for r in range(1, row - 1):
        for c in range(1, column - 1):
            valor = boards[r][c]
            if valor == "B":
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        inc = boards[i][j]
                        if inc != "B":
                            boards[i][j] = inc + 1

    printBoard(boards, row, column)


def makeBoard(boards, row, column, percentage):
    for i in range(row):
        boards.append([0 for j in range(column)])

    putBomb(boards, row, column, percentage)


boards, row, column, percentage = [], 10, 10, 25
makeBoard(boards, row + 2, column + 2, percentage)
