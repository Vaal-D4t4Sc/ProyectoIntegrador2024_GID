-- Obtener información de la tabla clientes
SELECT DNI_CUIT, Nombre, Apellido 
FROM turnero_banco.clientes;

-- Borrar un registro de la tabla turnos
Delete From turnero_banco.turnos
where IDturno = '5';

-- Inserción de un nuevo turno
INSERT INTO turnero_banco.turnos (Fecha_Turno, Hora_Turno, Estado, Recordatorio, ID_cliente, IDsucursal, IDserv) 
VALUES ('2024-10-14', '13:00:00', 'Confirmado', '1', '12345675', '5', '5');

-- actualizar registro de un cliente
UPDATE turnero_banco.clientes
SET Telefono = '987654321', Direccion = 'Calle Nueva 456'
WHERE DNI_CUIT = 12345675;

-- Inner joim para Obtener turnos de un cliente específico con información del servicio y la sucursal
SELECT t.IDturno, t.Fecha_Turno, t.Hora_Turno, t.Estado, s.Nombre AS Servicio, su.Nombre AS Sucursal
FROM turnos t
JOIN servicios s ON t.IDserv = s.IDserv
JOIN sucursales su ON t.IDsucursal = su.IDsucursal
WHERE t.ID_cliente = 12345675;

-- Inner join para Obtener los accesos de un usuario, incluyendo detalles de clientes relacionados
SELECT a.ID_accesos, a.Fecha_Ingreso, a.Fecha_Salida, u.Username, c.Nombre, c.Apellido
FROM accesos a
JOIN usuarios u ON a.usuarioLogueado = u.ID_usuario
JOIN clientes c ON u.DNI_CUIT = c.DNI_CUIT
WHERE u.ID_usuario = 1;

-- Right join Devuelve todos los clientes, incluso aquellos que no tienen turnos asociados
SELECT t.IDturno, t.Fecha_Turno, t.Hora_Turno, t.Estado, c.DNI_CUIT, c.Nombre, c.Apellido
FROM turnos t
RIGHT JOIN clientes c ON t.ID_cliente = c.DNI_CUIT;




