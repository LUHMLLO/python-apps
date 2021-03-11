
print('\n' * 2)
print("Imprimiendo graficos...")

print("")
grafico_A = []

for aterisco in range(6):
    grafico_A.append("*")

for aterisco in range(6):
    aterisco += 1
    aterisco -= 7
    resultado = aterisco * -1
    print(', '.join(grafico_A[:resultado]))


print("")
grafico_B = []

for aterisco in range(9):
    grafico_B.append("*")

for aterisco in range(9):
    if aterisco in range(0,4):
        grafico_B[aterisco] = " "
    elif aterisco in range(5,9):
        grafico_B[aterisco] = " "
print(''.join(grafico_B))

for aterisco in range(9):
    if aterisco in range(3,6):
        grafico_B[aterisco] = "*"
print(''.join(grafico_B))

for aterisco in range(9):
    if aterisco in range(2,7):
        grafico_B[aterisco] = "*"
print(''.join(grafico_B))

for aterisco in range(9):
    if aterisco in range(1,8):
        grafico_B[aterisco] = "*"
print(''.join(grafico_B))

for aterisco in range(9):
    if aterisco in range(0,9):
        grafico_B[aterisco] = "*"
print(''.join(grafico_B))


print("")
grafico_C = []

for aterisco in range(9):
    grafico_C.append("*")

for aterisco in range(9):
    if aterisco in range(0,4):
        grafico_C[aterisco] = " "
    elif aterisco in range(5,9):
        grafico_C[aterisco] = " "
print(''.join(grafico_C))

for aterisco in range(9):
    if aterisco in range(3,6):
        grafico_C[aterisco] = "*"
print(''.join(grafico_C))

for aterisco in range(9):
    if aterisco in range(2,7):
        grafico_C[aterisco] = "*"
print(''.join(grafico_C))

for aterisco in range(9):
    if aterisco in range(1,8):
        grafico_C[aterisco] = "*"
print(''.join(grafico_C))

for aterisco in range(9):
    if aterisco in range(0,9):
        grafico_C[aterisco] = "*"
print(''.join(grafico_C))

for aterisco in range(9):
    if aterisco in range(0,1):
        grafico_C[aterisco] = " "
    elif aterisco in range(8,9):
        grafico_C[aterisco] = " "
print(''.join(grafico_C))
for aterisco in range(9):
    if aterisco in range(0,2):
        grafico_C[aterisco] = " "
    elif aterisco in range(7,9):
        grafico_C[aterisco] = " "
print(''.join(grafico_C))
for aterisco in range(9):
    if aterisco in range(0,3):
        grafico_C[aterisco] = " "
    elif aterisco in range(6,9):
        grafico_C[aterisco] = " "
print(''.join(grafico_C))
for aterisco in range(9):
    if aterisco in range(0,4):
        grafico_C[aterisco] = " "
    elif aterisco in range(5,9):
        grafico_C[aterisco] = " "
print(''.join(grafico_C))




