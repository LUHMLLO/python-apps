# El número de 5 dígitos 16807=75 se conoce como quita potencia ya que la última cifra
# es igual a la base y la cantidad de dígitos es igual al exponente. 
# Encuentre todos los
# números que presentan esta situación en el rango del 1-10 como base y 2 al 10 como
# exponente.



bases = []
for base in range(1,10+1):
    bases.append(pow(base, 5))

exponentes = []
for exponente in range(2,10+1):
    exponentes.append(pow(exponente, 5))

print(bases)
print(exponentes)
