import pickle
from datetime import datetime


class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f'ID: {self.id}, Username: {self.username}, Contraseña {self.password}, Email: {self.email}'


class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado

    def __str__(self):
        return f'ID {self.id}, Usuario logueado: {self.usuarioLogueado}, Fecha de ingreso: {self.fechaIngreso}, Fecha de salida: {self.fechaSalida}'


class U_Manager:
    def __init__(self):
        self.usuarios = self.cargar_usuarios()
        self.next_id = len(self.usuarios) + 1 if self.usuarios else 1

    def cargar_usuarios(self):
        try:
            with open('usuarios.ispc', 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    def guardar_usuarios(self):
        with open('usuarios.ispc', 'wb') as f:
            pickle.dump(self.usuarios, f)

    def agre_u(self, username, password, email):
        nuevo_usuario = Usuario(self.next_id, username, password, email)
        self.usuarios.append(nuevo_usuario)
        self.next_id += 1
        self.guardar_usuarios()
        print(f'Usuario {username} agregado exitosamente.')

    def buscar_u(self, identifier):
        for usuario in self.usuarios:
            if usuario.username == identifier or usuario.email == identifier:
                return usuario
        return None

    def verificar_acceso(self, username, password):
        usuario = self.buscar_u(username)
        if usuario and usuario.password == password:
            return usuario
        return None

    def registrar_acceso(self, usuario):
        fecha_hora = datetime.now().strftime("%d/%m/%y  %H:%M")
        acceso = Acceso(len(usuario.username), datetime.now(), None, usuario.username)
        with open('accesos.ispc', 'ab') as f:
            pickle.dump(acceso, f)

    def registrar_intento_fallido(self, username, password):
        fecha_hora = datetime.now().strftime("%d/%m/%y  %H:%M")
        with open('logs.txt', 'a') as f:
            f.write(f'{datetime.now()}: Intento fallido con usuario: {username}, Contraseña: {password}\n')

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
        print("6. Ingresar al Sistema")
        print("7. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            username = input("Ingrese el username: ")
            password = input("Ingrese la contraseña: ")
            email = input("Ingrese el email: ")
            manager.agre_u(username, password, email)
        elif choice == '2':
            username = input("Ingrese el username del usuario a modificar: ")
            new_username = input("Ingrese el nuevo username (deje vacío si no desea cambiarlo): ")
            new_password = input("Ingrese la nueva contraseña (deje vacío si no desea cambiarlo): ")
            new_email = input("Ingrese el nuevo email (deje vacío si no desea cambiarlo): ")
            manager.modif_u(username, new_username or None, new_password or None, new_email or None)
        elif choice == '3':
            identifier = input("Ingrese el username o email del usuario a eliminar: ")
            manager.elim_u(identifier)
        elif choice == '4':
            identifier = input("Ingrese el username o email del usuario a buscar: ")
            usuario = manager.buscar_u(identifier)
            if usuario:
                print(usuario)
            else:
                print(f'Usuario {identifier} no encontrado.')
        elif choice == '5':
            manager.mostrar_u()
        elif choice == '6':
            username = input("Ingrese el username: ")
            password = input("Ingrese la contraseña: ")
            usuario = manager.verificar_acceso(username, password)

            if usuario:
                print("Acceso correcto")
                manager.registrar_acceso(usuario)

                while True:
                    print("\nOpciones:")
                    print("1. Volver al Menú Principal")
                    print("2. Salir de la Aplicación")
                    option = input("Seleccione una opción: ")

                    if option == '1':
                        break
                    elif option == '2':
                        print("Saliendo de la aplicación.")
                        return
                    else:
                        print("Opción no válida.")
            else:
                print("Acceso incorrecto")
                manager.registrar_intento_fallido(username, password)
        elif choice == '7':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main_menu()
