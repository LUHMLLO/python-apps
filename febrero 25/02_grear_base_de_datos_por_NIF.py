
basededatos = [
    {
        "nif": "420",
        "nombre": "snoop dog",
        "direccion": "usa",
        "telefono": "5-555-5555",
        "correo": "snoopdd@gmail.com",
        "preferente": "",
    },
    {
        "nif": "111",
        "nombre": "russ",
        "direccion": "london",
        "telefono": "5-555-5555",
        "correo": "russ@gmail.com",
        "preferente": "snoop dog",
    }
]


def capturar_datos():
    capturar_datos.nif = str(input('Digite su NIF :_  ')).lower()
    capturar_datos.nombre = str(input('Digite su nombre :_  ')).lower()
    capturar_datos.direccion = str(input('Digite su direccion :_  ')).lower()
    capturar_datos.telefono = str(input('Digite su telefono :_  ')).lower()
    capturar_datos.correo = str(input('Digite su correo :_  ')).lower()
    capturar_datos.preferente = bool(
        input('Digite su preferente (dejar vacio si no posee un preferente) :_  '))
    agregar_cliente()


def agregar_cliente():
    data = {
        "nif": capturar_datos.nif,
        "nombre": capturar_datos.nombre,
        "direccion": capturar_datos.direccion,
        "telefono": capturar_datos.telefono,
        "correo": capturar_datos.correo,
        "preferente": capturar_datos.preferente,
    }
    basededatos.append(data)


def clientes_todos():
    for i in basededatos:
        print("")
        for key, value in i.items():
            print(str(key)+": "+str(value))


def clientes_con_referentes():
    for i in basededatos:
        print("")
        for key, value in i.items():
            if "preferente" in key:
                if value:
                    for key,value in i.items():
                        print(str(key)+": "+str(value))


def cliente_por_nif():
    nif = str(input('Digite el NIF del usuario :_  ')).lower()
    for i in basededatos:
        print("")
        for key, value in i.items():
            if "nif" in key:
                if nif in value:
                    for key,value in i.items():
                        print(str(key)+": "+str(value))


def eliminar_cliente():
    nif = str(input('Digite el NIF del usuario :_  ')).lower()
    for i in basededatos:
        print("")
        for key, value in i.items():
            if "nif" in key:
                if nif in value:
                    basededatos.remove(i)


def finalizar_programa():
    print("finalizando...")


def agregar_linea_en_blanco():
    print('\n')


def Acciones_A_Realizar():
    print('\n')
    print("Que desea hacer ?")
    print("[1] Agregar un cliente nuevo")
    print("[2] Ver todos los clientes")
    print("[3] Ver clientes con referentes")
    print("[4] Encontrar cliente por el NIF")
    print("[5] Eliminar un cliente existente")
    print("[6] Finalizar programa")
    accion_a_realizar = str(input('Digite el numero de la accion que desea realizar :_  '))
    
    if accion_a_realizar == "1":
        capturar_datos()
        agregar_linea_en_blanco()
        Acciones_A_Realizar()

    elif accion_a_realizar == "2":
        clientes_todos()
        agregar_linea_en_blanco()
        Acciones_A_Realizar()

    elif accion_a_realizar == "3":
        clientes_con_referentes()
        agregar_linea_en_blanco()
        Acciones_A_Realizar()

    elif accion_a_realizar == "4":
        cliente_por_nif()
        agregar_linea_en_blanco()
        Acciones_A_Realizar()

    elif accion_a_realizar == "5":
        eliminar_cliente()
        agregar_linea_en_blanco()
        Acciones_A_Realizar()

    elif accion_a_realizar == "6":
        finalizar_programa()
        agregar_linea_en_blanco()

    else:
        agregar_linea_en_blanco()
        Acciones_A_Realizar()


Acciones_A_Realizar()
