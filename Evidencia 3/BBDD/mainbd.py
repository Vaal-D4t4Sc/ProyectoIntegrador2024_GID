# mainbd.py
from Consultas_clientes import obtener_informacion_clientes, actualizar_cliente
from conssultas_turnos import borrar_turno, insertar_turno
from joins import obtener_turnos_con_servicio, obtener_accesos_usuario, obtener_turnos_y_clientes

if __name__ == "__main__":
    # Clientes
    print("Información de clientes:")
    obtener_informacion_clientes()

    print("\nActualizar cliente:")
    actualizar_cliente(12345675, "9876565489", "Calle 55")

    # Turnos
    print("\nEliminar un turno:")
    borrar_turno(5)

    print("\nInsertar un nuevo turno:")
    insertar_turno("2024-10-14", "13:00:00", "Confirmado", 1, 12345675, 5, 5)

    # Consultas JOIN
    print("\nObtener turnos de un cliente con detalles de servicio y sucursal:")
    obtener_turnos_con_servicio(12345675)

    print("\nObtener accesos de un usuario:")
    obtener_accesos_usuario(1)

    print("\nRight JOIN para obtener turnos y clientes:")
    obtener_turnos_y_clientes()
