print(" ")
#print("Digite el numero del cual desea encontrar los palindromos que lo componen")
#numero = int(input("Digite : "))

numeros_en_el_rango =[]

for num in range(2,1000+1):
    numeros_en_el_rango.append(num)


def invertir_valor(x):
    x = str(x)
    x = x[::-1]
    x = int(x)
    return x

palindromos = []

for num in numeros_en_el_rango:
    if num == invertir_valor(num):
        palindromos.append(num)


palindromos_cuadrados = []

for num in palindromos:
    if pow(num,2) < 4164:
        palindromos_cuadrados.append(pow(num,2))


print(palindromos_cuadrados)
print(len(palindromos_cuadrados))
print(sum(palindromos_cuadrados))
