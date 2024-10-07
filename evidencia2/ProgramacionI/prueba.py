class Usuario:
  def __init__(self) ->None:
    self.id = input("Ingrese ID: ")
    self.username = input("Ingrese usuario: ")
    self.password = input("Ingrese contraseña: ")
    self.email = input ("Ingrese correo electronico: ")


  def __str__(self) -> str:
    return f"  ID  {self.id}  Usuario: {self.usuario}  Contraseña ******  @Correo  {self.email}"



class Acceso():
  def __init__(self, fechaIngreso, fechaSalida, usuarioLogueado) -> None:
    self.fechaIngreso = fechaIngreso
    self.fechaSalida = fechaSalida
    self.usuarioLogueado = usuarioLogueado
    #self.id !!
    
