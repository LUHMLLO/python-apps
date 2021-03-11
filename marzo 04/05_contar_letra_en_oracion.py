print("Digite una palabra")
palabra = str(input("Palabra : "))
print("")
print("Digite un caracter")
caracter = str(input("Caracter : "))

if caracter in palabra:
    print("este caracter se encuentra en esta palabra")
    apariciones = palabra.count(caracter)
    print("y se repite "+str(apariciones)+ " veces")
else:
    print("este caracter no existe en esta palabra")
