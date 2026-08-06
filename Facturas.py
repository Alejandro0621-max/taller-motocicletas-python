menu = {
    1: "Ingresar facturas",
    2: "Abrir caja",
    3: "Cerrar caja",
    4: "Volver"
}

def menu_facturas():
    while True:
        print("================\nMENU FACTURAS\n================")
        for clave, item in menu.items():
            print(f"{clave}. {item}")
        print("================")
        try:
            eleccion = int(input("Ingrese el numero de la consulta a realizar: "))
    
            if eleccion == 4:
                break
            elif eleccion in menu.keys():
                print(f"Usted eligio:\n{menu[eleccion]}\n")
            else:
                print("\nEleccion no se encuentra en el menu, ingrese nuevamente\n")
        except:
            print("\nPor favor ingrese solo los numeros del menú\n")