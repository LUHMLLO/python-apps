# haga un programa en el cual se digiten:
# la temperatura para cada hora del dia
# que imprima por pantalla:
# la temperatura promedio para ese dia
# la temperatura mayor y la menor
# informando la hora a la cual ocurrieron dichas lecturas

registro_del_clima = []


def capturar_temperatura_por_hora(hora, meridiano):
    print("-----------------------------------")
    print(str(hora+1)+str(meridiano))
    temperatura = input(str("temperatura : "))
    registro_del_clima.append(temperatura)


print('\n'+"Digite las temperaturas registradas durante las 24 horas del dia :")

for hora in range(1):
    capturar_temperatura_por_hora(hora, "am")
for hora in range(1):
    capturar_temperatura_por_hora(hora, "pm")


print('\n')
for temp in registro_del_clima:
    index = registro_del_clima.index(temp)+1
    if(index > 12):
        hora = str(index)+"am"
    else:
        hora = str(index)+"pm"
    print(str(hora)+": "+str(temp)+" grados")

temperatura_mas_baja = min(registro_del_clima)
temperatura_mas_alta = max(registro_del_clima)

print("temperatura mas baja del dia "+str(temperatura_mas_baja+" grados"))
print("temperatura mas alta del dia "+str(temperatura_mas_alta+" grados"))
