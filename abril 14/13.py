# Name: Franklin Junior Blanco Aquino
# ID: 1014-1034
# Exercise : 7

# encontrar la longitud de una lista
# de forma recursiva

ListaParaPrueba = []

for i in range(1,100+1):
    ListaParaPrueba.append(i)

def list_length(lista):
    if lista:
        return 1 + list_length(lista[1:])
    else:
        return 0
print(list_length(ListaParaPrueba))
