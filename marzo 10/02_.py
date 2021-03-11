print(" ")
print("Para finalizar el programa, formule una oracion que no contenga ningun caracter en mayuscula")

def capturar_data():
    capturar_data.oracion = str(input())
    verificar_data()

def verificar_data():
    if capturar_data.oracion.islower():
        print("Su oracion cumple con todas las normas")
        print("Finalizando..")

    elif capturar_data.oracion.isupper():
        print("Se detectaron mayusculas en su oracion, por favor digite de nuevo")
        print('\n')
        capturar_data()

    elif not capturar_data.oracion.islower() and not capturar_data.oracion.isupper():
        print("Se detectaron mayusculas en su oracion, por favor digite de nuevo")
        print('\n')
        capturar_data()



capturar_data()
