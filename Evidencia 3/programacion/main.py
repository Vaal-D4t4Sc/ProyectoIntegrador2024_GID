from user_manager import U_Manager

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
        print("7. Registros Pluviales")
        print("8. Salir")

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
                        pass
        elif choice == '3':
            identifier = input("Ingrese el username o email del usuario a eliminar: ")
            manager.elim_u(identifier)
                       pass
        elif choice == '4':
            identifier = input("Ingrese el username o email del usuario a buscar: ")
            usuario = manager.buscar_u(identifier)
            if usuario:
                print(usuario)
                print("Búsqueda realizada por técnica de búsqueda binaria.")
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
                    print("\nOpciones: ")
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
            year = 2023
            df = manager.crear_registros_pluviales(year)
            if df is not None:
                manager.mostrar_registros_mes(df)
                manager.graficar_registros(df)
        elif choice == '8':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main_menu()
