# db/clientes.py
from conexion import obtener_conexion, cerrar_conexion

# Obtener información de clientes
def obtener_informacion_clientes():
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    consulta = "SELECT DNI_CUIT, Nombre, Apellido FROM clientes;"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cerrar_conexion(conexion)

# Actualizar registro de un cliente
def actualizar_cliente(dni_cuit, nuevo_telefono, nueva_direccion):
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    consulta = """
    UPDATE clientes 
    SET Telefono = %s, Direccion = %s
    WHERE DNI_CUIT = %s;
    """
    cursor.execute(consulta, (nuevo_telefono, nueva_direccion, dni_cuit))
    conexion.commit()
    cerrar_conexion(conexion)
