def capturar_datos():
    nombre = str(input('Digite su nombre : ')).lower()
    sexo = str(input('Digite el genero [hombre, mujer] : ')).lower()

    mujer_A = ["a", "b", "c", "d", "e", "f", "g", "h"]
    mujer_B = ["i", "j", "k", "l", "m", "n", "o"]
    mujer_C = ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    hombre_A = ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    hombre_B = ["a", "b", "c", "d", "e", "f", "g", "h"]
    hombre_C = ["i", "j", "k", "l", "m", "n", "o"]

    if sexo == "hombre":
        if nombre[0] in hombre_A:
            print("asignado al grupo A")
        elif nombre[0] in hombre_B:
            print("asignado al grupo B")
        elif nombre[0] in hombre_C:
            print("asignado al grupo C")
        else:
            print('\n')
            print("su nombre debe comenzar con una letra")
            print('\n')
            capturar_datos()

    elif sexo == "mujer":
        if nombre[0] in mujer_A:
            print("asignado al grupo A")
        elif nombre[0] in mujer_B:
            print("asignado al grupo B")
        elif nombre[0] in mujer_C:
            print("asignado al grupo C")
        else:
            print('\n')
            print("su nombre debe comenzar con una letra")
            print('\n')
            capturar_datos()

    else:
        print('\n')
        print("su genero debe ser [hombre] o [mujer]")
        print('\n')
        capturar_datos()


capturar_datos()
