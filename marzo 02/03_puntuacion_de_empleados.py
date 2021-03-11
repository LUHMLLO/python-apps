inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6

salario_base = 25000.00

empleados = {
    "raul": 0.0,
    "alan": 0.6,
    "carlos": 0.9,
    "mendez": 0.4,
    "garcia": 0.0,
    "carmen": 0.8,
    "rita": 0.6,
    "indiana": 0.4,
}

for key, value in empleados.items():
    if value == inaceptable:
        print("")
        print("el empleado "+str(key) +" posee una puntuacion inaceptable de "+str(value))
        print("su salario es de " + str(salario_base))
        print("")
    elif value == aceptable:
        print("")
        print("el empleado "+str(key) +" posee una puntuacion aceptable de "+str(value))
        print("su salario es de " + str(salario_base*value))
        print("")
    elif value >= meritorio:
        print("")
        print("el empleado "+str(key) +" posee una puntuacion meritoria de "+str(value))
        print("su salario es de " + str(salario_base*value))
        print("")
