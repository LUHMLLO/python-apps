# calcular la media e imprimir los mayores o iguales a esta

temperutas = [22, 21, 24, 18, 19, 21, 22, 32, 28, 21, 19, 20, 22, 21]
temperaturas_longitud = len(sorted(temperutas))

media = round(sum(temperutas)*1.0/temperaturas_longitud, 2)


print('\n'+"media: " + str(media))

for num in temperutas:
    if num > media:
        print("Mayor a la media: " + str(num))
    elif num == media:
        print("Igual a la media: " + str(num))
