import re
import random
import datetime
from aritmetica import *

usuarios = {}

def validar_usuario(nombreUsuario):
    return 6 <= len(nombreUsuario) <= 12

def validar_clave(clave):
    return (len(clave) >= 8 and
            re.search(r'[a-z]', clave) and
            re.search(r'[A-Z]', clave) and
            re.search(r'[0-9]', clave) and
            re.search(r'[^a-zA-Z0-9]', clave))

def captcha():
    operaciones = [sumar, restar, dividir, multiplicar]
    op = random.choice(operaciones)
    a = round(random.uniform(1, 10), 2)
    b = round(random.uniform(1, 10), 2)
    resultado = op(a, b)
    print(f"Resuelve la siguiente operación: {a} {op.__name__} {b} = ?")
    respuesta = float(input("Ingresa el resultado (con dos decimales): "))
    return round(respuesta, 2) == resultado

def registrar_usuario():
    nombreUsuario = input("Nombre de Usuario: ")
    while not validar_usuario(nombreUsuario) or nombreUsuario in usuarios:
        print("El nombre de usuario no es válido o ya existe.")
        nombreUsuario = input("Nombre de Usuario: ")

    clave = input("Clave: ")
    while not validar_clave(clave):
        print("La clave no cumple con los requisitos.")
        clave = input("Clave: ")

    dni = input("DNI: ")
    while dni in [u['dni'] for u in usuarios.values()]:
        print("El DNI ya existe.")
        dni = input("DNI: ")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo Electrónico: ")
    fecha_nacimiento = input("Fecha de Nacimiento (DD/MM/AAAA): ")

    if captcha():
        usuarios[nombreUsuario] = {
            'clave': clave,
            'dni': dni,
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'fecha_nacimiento': fecha_nacimiento
        }
        with open("app/usuariosCreados.txt", "a") as f:
            f.write(f"Usuario: {nombreUsuario}, DNI: {dni}, Nombre: {nombre} {apellido}, Correo: {correo}, Fecha Nacimiento: {fecha_nacimiento}\n")
        print("Usuario registrado correctamente.")
    else:
        print("CAPTCHA incorrecto. Registro no completado.")

def iniciar_sesion():
    nombreUsuario = input("Usuario: ")
    clave = input("Clave: ")
    intentos = 0

    while intentos < 4:
        if nombreUsuario in usuarios and usuarios[nombreUsuario]['clave'] == clave:
            with open("app/ingresos.txt", "a") as f:
                f.write(f"{nombreUsuario} ingresó en {datetime.datetime.now()}\n")
            print("Bienvenido a la aplicación.")
            return True
        else:
            intentos += 1
            if intentos == 4:
                with open("app/log.txt", "a") as f:
                    f.write(f"Bloqueo de {nombreUsuario} por intentos fallidos\n")
                print("Usuario bloqueado por intentos fallidos.")
                return False
            print(f"Intento {intentos}/4 fallido. Intenta nuevamente.")
            clave = input("Clave: ")

def menu():
    print("Bienvenido al Sistema de Turnos")
    while True:
        print("\n1. Iniciar Sesión")
        print("2. Registrar Usuario")
        print("3. Olvidé mi Contraseña")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            if iniciar_sesion():
                break
        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            print("Función de recuperación de contraseña no implementada.")
        elif opcion == '4':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
