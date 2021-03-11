def imprimir_tipos_de_pizza():
    print("Que tipo de pizza desea ?")
    print("")
    print("[normal] - [vegetariana]")


def imprimir_menu_normal():
    print("Que ingrediente desea en su pizza?")
    print("")
    print("[peperoni] - [jamon] - [salmon]")


def imprimir_menu_vegetariano():
    print("Que ingrediente desea en su pizza?")
    print("")
    print("[pimiento] - [tofu]")


def capturar_tipo_de_pizza():
    capturar_tipo_de_pizza.tipo = input("tipo de pizza: ").lower()


def capturar_ingrediente_de_pizza():
    capturar_ingrediente_de_pizza.ingrediente = input("ingrediente de pizza: ").lower()


def verificar_tipo_de_pizza():
    print("")
    if capturar_tipo_de_pizza.tipo == "normal":
        print("Eligio ["+capturar_tipo_de_pizza.tipo+"]")
        pizza_normal()

    elif capturar_tipo_de_pizza.tipo == "vegetariana":
        print("Eligio ["+capturar_tipo_de_pizza.tipo+"]")
        pizza_vegetariana()

    else:
        print("El tipo de pizza que eligio no esta existe")
        print('\n')
        imprimir_tipos_de_pizza()
        capturar_tipo_de_pizza()

def pizza_normal():
    imprimir_menu_normal()
    capturar_ingrediente_de_pizza()
    print("")
    if capturar_ingrediente_de_pizza.ingrediente == "peperoni":
        print("Eligio ["+capturar_ingrediente_de_pizza.ingrediente+"]")

    elif capturar_ingrediente_de_pizza.ingrediente == "jamon":
        print("Eligio ["+capturar_ingrediente_de_pizza.ingrediente+"]")

    elif capturar_ingrediente_de_pizza.ingrediente == "salmon":
        print("Eligio ["+capturar_ingrediente_de_pizza.ingrediente+"]")

    else:
        print("El ingrediente que eligio no esta disponible en este tipo de pizza")
        print('\n')
        imprimir_menu_normal()
        capturar_ingrediente_de_pizza()

def pizza_vegetariana():
    imprimir_menu_vegetariano()
    capturar_ingrediente_de_pizza()
    print("")
    if capturar_ingrediente_de_pizza.ingrediente == "pimiento":
        print("Eligio ["+capturar_ingrediente_de_pizza.ingrediente+"]")

    elif capturar_ingrediente_de_pizza.ingrediente == "tofu":
        print("Eligio ["+capturar_ingrediente_de_pizza.ingrediente+"]")

    else:
        print("El ingrediente que eligio no esta disponible en este tipo de pizza")
        print('\n')
        imprimir_menu_vegetariano()
        capturar_ingrediente_de_pizza()


def imprimir_resultado(tipo, ingrediente):
    print('\n')
    print("tipo de pizza: "+str(tipo))
    print("ingrediente seleccionado: "+str(ingrediente))
    print("ingredientes generales: mozzarella y tomate")
    print('\n')




print('\n')
imprimir_tipos_de_pizza()
capturar_tipo_de_pizza()
verificar_tipo_de_pizza()
imprimir_resultado(capturar_tipo_de_pizza.tipo, capturar_ingrediente_de_pizza.ingrediente)
