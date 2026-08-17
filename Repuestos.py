import manejo_datos as dat

archivo = "Repuestos"

def crear():
    nuevo={
        "Codigo": input("Ingrese el codigo: "),
        "Repuesto":input("Ingrese el nombre del repuesto a crear: "),
        "Cantidad": input("Ingrese la cantidad de producto: "),
        "Precio": input("Ingrese el Precio del producto: ")
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

def menu_repuestos():
    while True:
        print("================\nMENU REPUESTOS\n================")
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
