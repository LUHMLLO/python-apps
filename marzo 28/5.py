# calcular el cuadrado de los primeros 100 numeros enteros
# y a continuacion escribir una tabla que contenga dichos numeros

def esEntero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False


for num in range(1, 101):
    if esEntero(num):
        print(pow(num, 2))
