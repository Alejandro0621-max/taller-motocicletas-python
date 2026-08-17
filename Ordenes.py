import manejo_datos as dat

archivo = "ordenes"

def crear():
    nuevo={
        "Orden":input("Ingrese el numero de orden: "),
        "Mecanico": input("Ingrese el mecanico asociado: "),
        "Servicio": input("Ingrese el servicio asociado: "),
        "Detalle": input("Ingrese algunos detalles: ")
    }
    dat.registrar(archivo, nuevo)
    print("informacion ingresada")
def ver():
    dat.buscar(archivo)
def Otro():
    print("Opcion no disponible en el momento")


menu = {
    1: ("Crear", crear),
    2: ("ver", ver),
    3: ("Modificar", Otro),
    4: ("Eliminar", Otro),
    5: ("Volver", None)
}

def menu_ordenes():
    while True:
        print("================\nMENU ORDENES\n================")
        for clave, (item, _) in menu.items():
            print(f"{clave}. {item}")
        print("================")
        try:
            eleccion = int(input("Ingrese el numero de la consulta a realizar: "))
    
            if eleccion == 5:
                break
            elif eleccion in menu:
                _, funcion = menu[eleccion]
                funcion()
            else:
                print("\nEleccion no se encuentra en el menu, ingrese nuevamente\n")
        except ValueError:
            print("\nPor favor ingrese solo los numeros del menú\n")
