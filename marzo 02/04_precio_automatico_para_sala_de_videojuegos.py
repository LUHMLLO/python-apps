def capturar_datos():
    edad = int(input("Digite su edad : "))

    if edad in range(0,5):
        print("costo de entrada gratis")
        capturar_datos()

    elif edad in range(5,19):
        print("costo de entrada RD$250.00")
        capturar_datos()

    elif edad in range(19,60):
        print("costo de entrada RD$500.00")
        capturar_datos()

    else:
        print("costo de entrada gratis")
        capturar_datos()
    


capturar_datos()
