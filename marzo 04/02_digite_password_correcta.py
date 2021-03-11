passwords = ["el caballo blanco de napoleon era negro","las_contraseñas_no_llevan_espacios", "contraseña", "contrasena", "nomelase"]


def capturar_password():
    verificar_password.contraseña = str(
        input("Digite su contraseña para continuar : "))
    verificar_password()


def verificar_password():
    if verificar_password.contraseña in passwords:
        print("contraseña correcta")
    else:
        print("Intentelo de nuevo")
        print("\n")
        capturar_password()


capturar_password()
