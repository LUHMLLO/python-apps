# haga un programa en el cual se digiten:
# la temperatura para cada hora del dia
# que imprima por pantalla:
# la temperatura promedio para ese dia
# la temperatura mayor y la menor
# informando la hora a la cual ocurrieron dichas lecturas

from statistics import mode

registro_del_clima = []


def capturar_temperatura_por_hora(hora, meridiano):
    print("-----------------------------------")
    print(str(hora+1)+str(meridiano))
    temperatura = input(str("temperatura : "))
    data = {
        str(hora+1)+str(meridiano): temperatura
    }
    registro_del_clima.append(data)


print('\n'+"Digite las temperaturas registradas durante las 24 horas del dia :")

for hora in range(1):
    capturar_temperatura_por_hora(hora, "am")
for hora in range(1):
    capturar_temperatura_por_hora(hora, "pm")


print('\n'+"-----------------------------------")
temperaturas_a_calcular = []
for registro in registro_del_clima:
    for key, value in registro.items():
        print(key+": "+value+" grados")
        temperaturas_a_calcular.append(value)



print('\n')
temperatura_mas_baja = min(temperaturas_a_calcular)
temperatura_mas_alta = max(temperaturas_a_calcular)
temperatura_promedio = mode(temperaturas_a_calcular)

print("temperatura mas baja del dia "+str(temperatura_mas_baja)+" grados")
print("temperatura mas alta del dia "+str(temperatura_mas_alta)+" grados")
print("temperatura promedio "+str(temperatura_promedio)+" grados")
print('\n')
