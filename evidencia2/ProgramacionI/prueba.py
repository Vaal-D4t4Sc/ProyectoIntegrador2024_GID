class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f'ID: {self.id}, Username: {self.username}, Contraseña ****, Email: {self.email}'


class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado
        return f'ID {self.id}, Usuario logueado: {self.usuarioLogueado}, Fecha de ingreso: {self.fechaIngreso}, Fecha de salida: {self.fechaSalida}'


class U_Manager:
    def __init__(self):
        self.usuarios = []
        self.next_id = 1

    def agre_u(self, username, password, email):
        nuevo_usuario = Usuario(self.next_id, username, password, email)
        self.usuarios.append(nuevo_usuario)
        self.next_id += 1
        print(f'Usuario {username} agregado exitosamente.')

    def modif_u(self, username, new_username=None, new_password=None, new_email=None):
        usuario = self.buscar_u(username)
        if usuario:
            if new_username:
                usuario.username = new_username
            if new_password:
                usuario.password = new_password
            if new_email:
                usuario.email = new_email
            print(f'Usuario {username} modificado exitosamente.')
        else:
            print(f'Usuario {username} no encontrado.')

    def elim_u(self, identifier):
        usuario = self.buscar_u(identifier)
        if usuario:
            self.usuarios.remove(usuario)
            print(f'Usuario {identifier} eliminado exitosamente.')
        else:
            print(f'Usuario {identifier} no encontrado.')

    def buscar_u(self, identifier):
        for usuario in self.usuarios:
            if usuario.username == identifier or usuario.email == identifier:
                return usuario
        return None

    def mostrar_u(self):
        if not self.usuarios:
            print('No hay usuarios registrados.')
        else:
            for usuario in self.usuarios:
                print(usuario)


def main_menu():
    manager = U_Manager()

    while True:
        print("\nMenú Principal:")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar Todos los Usuarios")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            username = input("Ingrese el username: ")
            password = input("Ingrese la contraseña: ")
            email = input("Ingrese el email: ")
            manager.agregar_usuario(username, password, email)
        elif choice == '2':
            username = input("Ingrese el username del usuario a modificar: ")
            new_username = input("Ingrese el nuevo username (deje vacío si no desea cambiarlo): ")
            new_password = input("Ingrese la nueva contraseña (deje vacío si no desea cambiarlo): ")
            new_email = input("Ingrese el nuevo email (deje vacío si no desea cambiarlo): ")
            manager.modificar_usuario(username, new_username or None, new_password or None, new_email or None)
        elif choice == '3':
            identifier = input("Ingrese el username o email del usuario a eliminar: ")
            manager.eliminar_usuario(identifier)
        elif choice == '4':
            identifier = input("Ingrese el username o email del usuario a buscar: ")
            usuario = manager.buscar_usuario(identifier)
            if usuario:
                print(usuario)
            else:
                print(f'Usuario {identifier} no encontrado.')
        elif choice == '5':
            manager.mostrar_usuarios()
        elif choice == '6':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main_menu()

