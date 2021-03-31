# - extraer los n primeros caracteres de una cadena
# - extraer los ultimos caracteresS
# - eliminar espacios en blanco al comienzo de la cadena
# - eliminar espacios en blanco al final de la cadena
# - eliminar de una cadena los caracteres n que aparecen a partir de la posicion p
# - eliminar la primera aparicion de una cadena dentro de otra
# - insertar unar cadena dentro de otra a partir de la posicion p??

# sustituir una cadena por otra
# contaer el numero de veces que aparece una cadena dentro de otra
# borrar todas las apariciones de una cadena dentro de otra
# sustituir todas las apariciones de una cadena dentro de otra por una tercera
# convertir las palabras mayusculas a mininusculas y viceversa

# solo se pueden usar las funciones:
# subcadena
# posicion
# longitud


# cadena.replace(subcadena, '')
# cadena.replace(subcadena, 'fresas')
# cadena.index(subcadena)


espacio = " "
nueva_linea = '\n'
division = "----------------------------------------------------------------------------"
cadena_1 = "Hola mundo esto es una cadena de prueba su proposito es ser manipulada"
cadena_2 = espacio*10 + \
    "aqui se remueven los espacios del comienzo o final de esta cadena" + espacio*10
cadena_3 = "Tres tristes tigres comian trigo, o algo asi"
cadena_4 = cadena_3 + espacio + cadena_1 + espacio + cadena_3
cadena_5 = "Me estoy quedando sin ideas chulas"

###############################################################################################
print(nueva_linea+division)
print("["+cadena_1+"]")
print(division+nueva_linea)

p = int(input("Cuantos caracteres desde el inicio desea extraer ? :  "))
print(cadena_1[:p])
print(espacio)

p = int(input("Desde que posicion desea extraer los caracteres de esta cadena ? :  "))
print(cadena_1[p:])
print(espacio)

p = int(input("Cuantos caracteres desde el final desea extraer ? :  "))
print(cadena_1[-p:])
print(espacio)

###############################################################################################
print(nueva_linea+division)
print("Removiendo los espacios del inicio de la cadena")
print(cadena_2.lstrip())
print(espacio)

print("Removiendo los espacios del final de la cadena")
print(cadena_2.rstrip())
print(division+nueva_linea)

###############################################################################################
print(nueva_linea+division)
print("["+cadena_3+"]")
print(division+nueva_linea)
p = int(input("Desde que posicion desea eliminar los caracteres de esta cadena ? :  "))
n = int(input("Cuantos caracteres desea eliminar ? :  "))
print(cadena_3[p:].replace(cadena_3[n], "", 1))
print(espacio)

###############################################################################################
print(nueva_linea+division)
print("["+cadena_4+"]")
print(division+nueva_linea)
p = str(input("Digite una subcadena, la cual sera eliminada de la cadena ya mostrada :  "))
print(cadena_4.replace(p, '',1))

###############################################################################################
print(nueva_linea+division)
print("["+cadena_5+"]")
print(division+nueva_linea)
p = int(input("Desde que posicion desea insertar una subcadena dentro de esta ? :  "))
n = str(input("Digite la subcadena :  "))
print(cadena_5[:p] + n + cadena_5[p:])
print(espacio)
