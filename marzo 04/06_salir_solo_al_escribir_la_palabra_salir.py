print("")
print("La unica forma de abandonar este programa es escribiendo [salir] sin mas caracteres agregados ni espacios")


def capturar_datos():
    capturar_datos.texto = str(input("Digite a su gusto : "))
    verificar_salida()


def verificar_salida():
    if capturar_datos.texto.lower() == "salir":
        print("Cerrando programa...")
    else:
        capturar_datos()


capturar_datos()
