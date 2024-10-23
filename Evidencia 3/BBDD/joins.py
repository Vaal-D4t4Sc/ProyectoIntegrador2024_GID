# db/joins.py
from conexion import obtener_conexion, cerrar_conexion

# Obtener turnos de un cliente con información del servicio y la sucursal
def obtener_turnos_con_servicio(id_cliente):
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    consulta = """
    SELECT t.IDturno, t.Fecha_Turno, t.Hora_Turno, t.Estado, s.Nombre AS Servicio, su.Nombre AS Sucursal
    FROM turnos t
    JOIN servicios s ON t.IDserv = s.IDserv
    JOIN sucursales su ON t.IDsucursal = su.IDsucursal
    WHERE t.ID_cliente = %s;
    """
    cursor.execute(consulta, (id_cliente,))
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cerrar_conexion(conexion)

# Obtener los accesos de un usuario, incluyendo detalles de clientes
def obtener_accesos_usuario(id_usuario):
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    consulta = """
    SELECT a.ID_accesos, a.Fecha_Ingreso, a.Fecha_Salida, u.Username, c.Nombre, c.Apellido
    FROM accesos a
    JOIN usuarios u ON a.usuarioLogueado = u.ID_usuario
    JOIN clientes c ON u.DNI_CUIT = c.DNI_CUIT
    WHERE u.ID_usuario = %s;
    """
    cursor.execute(consulta, (id_usuario,))
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cerrar_conexion(conexion)

# Right JOIN para obtener turnos y clientes
def obtener_turnos_y_clientes():
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    consulta = """
    SELECT t.IDturno, t.Fecha_Turno, t.Hora_Turno, t.Estado, c.DNI_CUIT, c.Nombre, c.Apellido
    FROM turnos t
    RIGHT JOIN clientes c ON t.ID_cliente = c.DNI_CUIT;
    """
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cerrar_conexion(conexion)
