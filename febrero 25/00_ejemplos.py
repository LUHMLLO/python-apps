

dia = "domingo"
print("hoy es " + dia) #este funcionara porque la variable sigue siendo string

dia = "lunes"
print("hoy es " + str(dia)) #este funcionara porque declaramos la variable como string

dia_en_numero = 15
print("hoy es lunes " + dia_en_numero) #este dara error porque la variable es tipo int

dia_en_numero = 15
print("hoy es lunes " + str(dia_en_numero)) #este funcionara porque convertimos la variable a string


