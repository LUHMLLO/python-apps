print("")
año = int(input("Digite un año para determinar si es bisiesto : "))
print("")

if (año % 4) == 0 and (año % 100) != 0:
    print(str(año) + " Es un año bisiesto y multiplo de 4")

if (año % 4) == 0 and (año % 100) == 0 and (año % 400) == 0:
    print(str(año) + " No es un año bisiesto y multiplo de 100")

if (año % 400) and (año % 100) != 0 == 0:
    print(str(año) + " Es un año bisiesto y multiplo de 400")
