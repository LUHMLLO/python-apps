# Name: Franklin Junior Blanco Aquino
# ID: 1014-1034
# Exercise : 15

# crear tablero de ajedrez
# determinar la posicion del caballo y la reina
# mostrar por pantalla las posibles jugadas

# nota: el caballo y la reina no pueden tener la misma posicion

# R ---reina
# x ---movimientos

# C ---caballo
# y ---movimientos

# O ---cruzes
# + ---demas espacios


boards = []


def printBoard(boards):
    for i in boards:
        for j in i:
            print(*list(j), end="  ")
        print('\n')


def valid(rx, ry, cx, cy, i, j):
    if rx == i and ry == j:
        return "R"
    elif rx == i or ry == j or abs(rx-i) == abs(ry-j):
        return "X"

    if cx == i and cy == j:
        return "C"
    elif cx == i or cy == j or abs(cx-i) == abs(cy-j):
        return "Y"    
    
    if rx == i or ry == j or abs(rx-i) == abs(ry-j) and cx == i or cy == j or abs(cx-i) == abs(cy-j):
        return "O"
    else:
        return "+"


def solve(rx, ry, cx, cy):
    boards = []
    for i in range(1, 9):
        boards.append([valid(rx, ry, cx, cy, i, j) for j in range(1, 9)])

    print('\n')
    printBoard(boards)


print('\n')
print("Digite la posicion de la reina (x,y): ")
reina_x = int(input("X : "))
reina_y = int(input("Y : "))

print('\n')
print("Digite la posicion del caballo (x,y): ")
caballo_x = int(input("X : "))
caballo_y = int(input("Y : "))

if reina_x < 1 or reina_x > 8 or reina_y < 1 or reina_y > 8:
    print("Coordenada incorrecta")
if caballo_x < 1 or caballo_x > 8 or caballo_y < 1 or caballo_y > 8:
    print("Coordenada incorrecta")
else:
    solve(reina_x, reina_y, caballo_x, caballo_y)
