from conexion import obtener_conexion


conexion = obtener_conexion()

print("Conexión exitosa")

conexion.close()