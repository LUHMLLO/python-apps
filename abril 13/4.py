# Name: Franklin Junior Blanco Aquino
# ID: 1014-1034
# Exercise : 4

# dada la lista ordenada de mayor a menor del ejercicio anterior
# obtener el numero de contratos realizados en una determinada fecha


import random
from datetime import datetime

basededatos = []


def dia_random():
    num = random.randint(1, 28)
    return num


def mes_random():
    num = random.randint(1, 12)
    return num


def año_random():
    num = random.randint(17, 21)
    return int("20"+str(num))


def id_random():
    num = random.randint(1, 10000000)
    return num


for num in range(1, 40):
    d = dia_random()
    m = mes_random()
    y = año_random()
    data = {
        "id": id_random(),
        "dia": d,
        "mes": m,
        "año": y,
        "fecha": str(d) + "-" + str(m) + "-" + str(y)
    }
    basededatos.append(data)
basededatos.sort(key=lambda x: datetime.strptime(x['fecha'], "%d-%m-%Y"))


##########################################################################################################


def obtener_contrato_por_fecha_completa():
    print('\n')
    print("Digite la fecha del documento [from 1-1-2017 to 28-12-2021]")
    fecha_a_buscar = str(input("Fecha : "))

    for i in basededatos:
        for key, value in i.items():
            if "fecha" in key:
                if fecha_a_buscar in value:
                    print(" ")
                    for key, value in i.items():
                        print(str(key)+": "+str(value))


def obtener_contrato_por_año():
    print('\n')
    print("Digite el año del documento [from 2017 to 2021]")
    fecha_a_buscar = str(input("Año : "))

    for i in basededatos:
        for key, value in i.items():
            if "año" in key:
                if fecha_a_buscar in str(value):
                    print(" ")
                    for key, value in i.items():
                        print(str(key)+": "+str(value))


def obtener_contrato_por_mes():
    print('\n')
    print("Digite el mes del documento [from 1 to 12]")
    fecha_a_buscar = str(input("Mes : "))

    for i in basededatos:
        for key, value in i.items():
            if "mes" in key:
                if fecha_a_buscar in str(value):
                    print(" ")
                    for key, value in i.items():
                        print(str(key)+": "+str(value))


def obtener_contrato_por_dia():
    print('\n')
    print("Digite el dia del documento [from 1 to 28]")
    fecha_a_buscar = str(input("Dia : "))

    for i in basededatos:
        for key, value in i.items():
            if "dia" in key:
                if fecha_a_buscar in str(value):
                    print(" ")
                    for key, value in i.items():
                        print(str(key)+": "+str(value))


##########################################################################################################


print('\n')
print("Como desea encontrar los contratos guardados ? ")
print("[0] - por dia")
print("[1] - por mes")
print("[2] - por año")
print("[3] - por fecha completa")
modo_de_busqueda = int(input("Opcion : "))
print('\n')

if modo_de_busqueda == 0:
    obtener_contrato_por_dia()

if modo_de_busqueda == 1:
    obtener_contrato_por_mes()

if modo_de_busqueda == 2:
    obtener_contrato_por_año()

if modo_de_busqueda == 3:
    obtener_contrato_por_fecha_completa()
