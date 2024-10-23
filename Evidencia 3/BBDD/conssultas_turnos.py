# db/turnos.py
from conexion import obtener_conexion, cerrar_conexion

# Borrar un turno
def borrar_turno(id_turno):
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    consulta = "DELETE FROM turnos WHERE IDturno = %s;"
    cursor.execute(consulta, (id_turno,))
    conexion.commit()
    cerrar_conexion(conexion)

# Insertar un nuevo turno
def insertar_turno(fecha_turno, hora_turno, estado, recordatorio, id_cliente, id_sucursal, id_servicio):
    conexion = obtener_conexion()
    if conexion is None:
        return
    cursor = conexion.cursor()
    consulta = """
    INSERT INTO turnos (Fecha_Turno, Hora_Turno, Estado, Recordatorio, ID_cliente, IDsucursal, IDserv)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    valores = (fecha_turno, hora_turno, estado, recordatorio, id_cliente, id_sucursal, id_servicio)
    cursor.execute(consulta, valores)
    conexion.commit()
    cerrar_conexion(conexion)
