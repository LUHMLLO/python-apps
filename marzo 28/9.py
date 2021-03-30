# suma de numeros pares y suma de numeros impares
import random

impares = []
pares = []


for num in range(1, 101):
    num = random.randint(-1, 101)
    if num % 2 != 0:
        impares.append(num)
    else:
        pares.append(num)


print("Suma de numeros pares : "+str(sum(pares)))
print("Suma de numeros impares : "+str(sum(impares)))
