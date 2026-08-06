#Sistema Taller de Motocicletas
#Menu principal
from Motocicletas import menu_motocicletas
from Clientes import menu_clientes
from Ordenes import menu_ordenes
from Mecanicos import menu_mecanicos
from Servicios import menu_servicios
from Vendedores import menu_vendedores
from Repuestos import menu_repuestos
from Facturas import menu_facturas

menu = {
    1: ("Motocicletas", menu_motocicletas),
    2: ("Clientes", menu_clientes),
    3: ("Ordenes", menu_ordenes),
    4: ("Mecanicos", menu_mecanicos),
    5: ("Servicios", menu_servicios),
    6: ("Vendedores", menu_vendedores),
    7: ("Repuestos", menu_repuestos),
    8: ("Facturas", menu_facturas),
    9: ("Salir", None)
}
#Bucle infinito
def menu_principal():
    while True:
        print("================\nMENU PRINCIPAL\n================")
        for clave, (item, _) in menu.items():
            print(f"{clave}. {item}")
        print("================")
        try:
            eleccion = int(input("Ingrese el numero de la consulta a realizar: "))
    
            if eleccion == 9:
                break
            elif eleccion in menu:
                
                _, funcion = menu[eleccion]
                funcion()
            else:
                print("\nEleccion no se encuentra en el menu, ingrese nuevamente\n")
        except ValueError:
            print("\nPor favor ingrese solo los numeros del menú\n")


menu_principal()