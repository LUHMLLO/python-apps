print(" ")
print("Digite una oracion de mas de 10 palabras")

oracion = str(input("# : "))




todas_las_palabras = []
for palabra in oracion.split():
    todas_las_palabras.append(palabra)


print(" ")
numero_de_palabras = len(todas_las_palabras)
print("numero de palabras encontradas en la oracion : " + str(numero_de_palabras))


print(" ")
print("La palabra mas larga en la oracion es "+ max(todas_las_palabras, key=len))
