from GestionUsuario import GestionUsuario
from GestionAcceso import GestionAcceso
from OrdenamientoyBusqueda import OrdenamientoBusqueda
from analisis_de_datos import AnalisisDatos

def mostrar_menu_principal():
    print("Bienvenido a la Aplicación de Gestión de Usuarios y Accesos")
    print("1. Usuarios y Accesos de la Aplicación")
    print("2. Ingresar al sistema con los datos de usuario")
    print("3. Análisis de datos")
    print("4. Salir de la aplicación")

def mostrar_menu_usuarios_accesos():
    print("\n1. Usuarios y Accesos de la Aplicación")
    print("a. Acceder al CRUD de los Usuarios en POO")
    print("b. Mostrar los datos de Accesos")
    print("c. Ordenamiento y Búsqueda de Usuarios")
    print("d. Volver al Menú principal")

def menu_crud_usuarios(usuario_manager):
    while True: 
        print("\n--- CRUD de Usuarios ---")
        print("i. Agregar un nuevo usuario")
        print("ii. Modificar un usuario")
        print("iii. Eliminar un usuario (por username o email)")
        print("iv. Volver al menú anterior")
        opcion = input("Selecciona una opción: ")

        if opcion == "i":
            DNI = input("DNI: ")
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            usuario_manager.agregar_usuario(username, DNI, password, email)
        elif opcion == "ii":
            identifier = input("DNI, username o email del usuario a modificar: ")
            new_username = input("Nuevo username (o Enter para omitir): ")
            new_password = input("Nueva contraseña (o Enter para omitir): ")
            new_email = input("Nuevo email (o Enter para omitir): ")
            usuario_manager.modificar_usuario(identifier, new_username, new_password, new_email)
        elif opcion == "iii":
            identifier = input("Username o email del usuario a eliminar: ")
            usuario_manager.eliminar_usuario(identifier)
        elif opcion == "iv":
            return
        else:
            print("Opción no válida. Intente nuevamente.")
            
def menu_mostrar_accesos(acceso_manager):
    while True: 
        print("\n--- Mostrar los datos de Accesos ---")
        print("i. Mostrar los Accesos (accesos.ispc)")
        print("ii. Mostrar los logs de intentos fallidos (logs.txt)")
        print("iii. Volver al menú anterior")
        opcion = input("Selecciona una opción: ")

        if opcion == "i":
            acceso_manager.mostrar_accesos()
        elif opcion == "ii":
            acceso_manager.mostrar_intentos_fallidos()
        elif opcion == "iii":
            return
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_ordenamiento_busqueda_usuarios(usuario_manager,ordenamiento_busqueda):
    while True:
        print("\n--- Ordenamiento y Búsqueda de Usuarios ---")
        print("i. Ordenar los Usuarios por username")
        print("ii. Buscar y Mostrar Usuarios")
        print("iii. Mostrar todos los usuarios")
        print("iv. Volver al menú anterior")
        opcion = input("Selecciona una opción: ")

        if opcion == "i":
            ordenamiento_busqueda.ordenar_usuarios_por_username()
        elif opcion == "ii":
            menu_buscar_usuarios(usuario_manager)
        elif opcion == "iii":
            usuario_manager.mostrar_todos_usuarios()
        elif opcion == "iv":
            return
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_buscar_usuarios(usuario_manager):
    while True:
        print("\n--- Buscar y Mostrar Usuarios ---")
        print("1. Búsqueda por DNI")
        print("2. Búsqueda por username")
        print("3. Búsqueda por email")
        print("4. Volver al menú anterior")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            dni = input("Ingrese el DNI del usuario: ")
            usuario_manager.buscar_usuario(dni)
        elif opcion == "2":
            username = input("Ingrese el username del usuario: ")
            usuario_manager.buscar_usuario(username)
        elif opcion == "3":
            email = input("Ingrese el email del usuario: ")
            usuario_manager.buscar_usuario(email)
        elif opcion == "4":
            return
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_ingresar_sistema(usuario_manager, acceso_manager):
    print("\n--- Ingresar al sistema ---")
    username = input("Username: ")
    password = input("Password: ")
    usuario = usuario_manager.verificar_acceso(username, password)
    
    if usuario:
        acceso_manager.registrar_acceso(usuario)
        print("Acceso correcto. Bienvenido a la Gestión de Base de Datos.")
        menu_gestion_base_datos()
    else:
        print("Acceso incorrecto. Intenta de nuevo.")

def menu_gestion_base_datos():
    print("\n--- Gestión de Base de Datos ---")
    print("1. Productos en stock")  # Ejemplo
    print("2. Listado de Empleados")  # Ejemplo
    print("3. Búsqueda de Empleado por DNI")  # Ejemplo
    print("4. Volver al menú anterior")
    opcion = input("Selecciona una opción: ")
    # Lógica para ejecutar las consultas SQL correspondientes

def menu_analisis_datos():
    print("\n--- Análisis de Datos ---")
    year = int(input("Ingrese el año para analizar los registros pluviales: "))
    analisis_datos = AnalisisDatos()
    df = analisis_datos.crear_registros_pluviales(year)
    
    # Ahora puedes mostrar los registros o graficarlos
    while True:
        print("\nSeleccione una opción:")
        print("1. Mostrar registros de un mes")
        print("2. Graficar registros pluviales")
        print("3. Volver al menú anterior")
        option = input("Opción: ")
        
        if option == "1":
            analisis_datos.mostrar_registros_mes(df)
        elif option == "2":
            analisis_datos.graficar_registros(df)
        elif option == "3":
            return
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    usuario_manager = GestionUsuario()
    acceso_manager = GestionAcceso()
    ordenamiento_busqueda = OrdenamientoBusqueda()  

    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_menu_usuarios_accesos()
            subopcion = input("Selecciona una opción: ")

            if subopcion == "a":
                menu_crud_usuarios(usuario_manager)
            elif subopcion == "b":
                menu_mostrar_accesos(acceso_manager)
            elif subopcion == "c":
                 menu_ordenamiento_busqueda_usuarios(usuario_manager, ordenamiento_busqueda)
            elif subopcion == "d":
                break
            print("Opción no válida. Intente nuevamente.")

        elif opcion == "2":
            menu_ingresar_sistema(usuario_manager, acceso_manager)

        elif opcion == "3":
            menu_analisis_datos()

        elif opcion == "4":
            print("Saliendo de la aplicación.")
            break

if __name__ == "__main__":
    main()