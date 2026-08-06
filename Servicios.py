menu = {
    1: "Crear",
    2: "Modificar",
    3: "Eliminar",
    4: "Volver"
}

def menu_servicios():
    while True:
        print("================\nMENU SERVICIOS\n================")
        for clave, item in menu.items():
            print(f"{clave}. {item}")
        print("================")
        try:
            eleccion = int(input("Ingrese el numero de la consulta a realizar: "))
    
            if eleccion == 4:
                break
            elif eleccion in menu.keys():
                print(f"Usted eligio:\n{menu[eleccion]} servicios\n")
            else:
                print("\nEleccion no se encuentra en el menu, ingrese nuevamente\n")
        except:
            print("\nPor favor ingrese solo los numeros del menú\n")