import pyodbc


def obtener_conexion():
    servidor = "DESKTOP-8LGNTTN"
    base_datos = "tallerMotos"

    conexion = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={servidor};"
        f"DATABASE={base_datos};"
        "Trusted_Connection=yes;"
    )

    return conexion