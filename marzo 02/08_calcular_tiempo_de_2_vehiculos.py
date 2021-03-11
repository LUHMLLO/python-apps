
print('\n')
print("Distancia y velocidad del vehiculo #1")
print("")
print("Que distancia debe recorrer este vehiculo ? (KM/H) : ")
auto_1_d = float(input("Distancia : "))
print("A que velocidad recorre esta ? (KM/H) : ")
auto_1_v = float(input("Velocidad : "))

print('\n')
print("Distancia y velocidad del vehiculo #2")
print("")
print("Que distancia debe recorrer este vehiculo ? (KM/H) : ")
auto_2_d = float(input("Distancia : "))
print("A que velocidad recorre esta ? (KM/H) : ")
auto_2_v = float(input("Velocidad : "))

distancia = auto_1_d + auto_2_d
velocidad = auto_1_v + auto_2_v

tiempo = float(distancia / velocidad)
tiempo_final = round(tiempo, 2)

if tiempo_final >= 1.0:
    print("tiempo de encuentro : " + str(tiempo_final)+" hora")
elif tiempo_final >= 0.59:
    print("tiempo de encuentro : " + str(tiempo_final)+" minutos")
else:
    print("tiempo de encuentro : " + str(tiempo_final)+" segundos")


