menu = {
    1: "Ingresar",
    2: "Modificar",
    3: "Volver"
}

def menu_ordenes():
    while True:
        print("================\nMENU ORDENES\n================")
        for clave, item in menu.items():
            print(f"{clave}. {item}")
        print("================")
        try:
            eleccion = int(input("Ingrese el numero de la consulta a realizar: "))
    
            if eleccion == 3:
                break
            elif eleccion in menu.keys():
                print(f"Usted eligio:\n{menu[eleccion]} orden\n")
            else:
                print("\nEleccion no se encuentra en el menu, ingrese nuevamente\n")
        except:
            print("\nPor favor ingrese solo los numeros del menú\n")