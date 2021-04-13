# organizar por fechas de mayor a menor
# una lista de 40 elementos

# cada elemento es un registro
# con los campos:
# dia, mes, año y numero de contrato (todos tipo int)

# puede haben varios contratos con la misma fecha
# pero no con el mismo numero de contrato (ID)


import random
from datetime import datetime

basededatos = []


def dia_random():
    num = random.randint(1, 30)
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
    data = {
        "id": id_random(),
        "fecha": str(dia_random()) + "-" + str(mes_random()) + "-" + str(año_random())
    }
    basededatos.append(data)


basededatos.sort(key=lambda x: datetime.strptime(x['fecha'], '%d-%m-%Y'))


for i in basededatos:
    print("")
    for key, value in i.items():
        print(str(key)+": "+str(value))


#dictionary.get("fecha", None)
