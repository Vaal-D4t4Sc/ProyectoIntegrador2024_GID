# gestionAcceso.py
import pickle
from acceso import Acceso
from datetime import datetime

class GestionAcceso:
    def registrar_acceso(self, usuario):
        acceso = Acceso(id=len(self.cargar_accesos()) + 1, fechaIngreso=datetime.now(), fechaSalida=None, usuarioLogueado=usuario.get_username())
        with open('accesos.ispc', 'ab') as f:
            pickle.dump(acceso, f)
        print(f"Acceso registrado para {usuario.get_username()}")

    def cargar_accesos(self):
        try:
            with open('accesos.ispc', 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    def mostrar_accesos(self):
        accesos = self.cargar_accesos()
        if not accesos:
            print("No hay accesos registrados.")
            return
        
        print("\n--- Lista de Accesos ---")
        for acceso in accesos:
            print(f"ID: {acceso.id}, Usuario: {acceso.usuarioLogueado}, Fecha de Ingreso: {acceso.fechaIngreso}, Fecha de Salida: {acceso.fechaSalida}")

    def registrar_intento_fallido(self, username, password):
        with open('logs.txt', 'a') as f:
            f.write(f"{datetime.now()}: Intento fallido con usuario: {username}, Contraseña: {password}\n")
        print(f"Intento fallido registrado para {username}")
    
    def mostrar_logs_intentos_fallidos():
        try:
            with open('logs.txt', 'r') as f:
                logs = f.readlines()
                if not logs:
                    print("No hay intentos fallidos registrados.")
                    return
                print("\n--- Logs de Intentos Fallidos ---")
                for log in logs:
                    print(log.strip())
        except FileNotFoundError:
            print("El archivo de logs no existe.")
