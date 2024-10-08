print("Menú Principal:")
print("1. Agregar Usuario")
print("2. Modificar Usuario")
print("3. Eliminar Usuario")
print("4. Buscar Usuario")
print("5. Mostrar Todos los Usuarios")
print("6. Salir")


class Usuario:
  def __init__(self) ->None:
    self.id = ID  
    self.username = username
    self.password = password
    self.email = email


  def __str__(self) -> str:
    return f"  ID  {self.id}  Usuario: {self.username}  Contraseña ******  @Correo  {self.email}"



class Acceso():
  def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado) -> None:
    self.id = id
    self.fechaIngreso = fechaIngreso
    self.fechaSalida = fechaSalida
    self.usuarioLogueado = usuarioLogueado
   
    def __str__(self) -> str:
    return f"ID {self.id}, Usuario logueado: {self.usuarioLogueado}, Fecha de ingreso: {self.fechaIngreso}, Fecha de salida: {fechaSalida}"

class U_Manager:
  def __init__(self) ->None:
    self.usuarios= []
    self.next_id = 1

  def agregar_u (self, username, password, email):
    nuevo_usuario = Usuario (self.next_id, username, password, email)
    self.usuarios.append (nuevo_usuario)
    self.next_id +1
    print (f'Usuario {username} agregadop exitosamente.')

  def modificar_u (self, username, password, email):
    #??
