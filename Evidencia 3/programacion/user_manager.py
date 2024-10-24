import pickle
import random
import pandas as pd
import matplotlib.pyplot as plt
from usuario import Usuario
from acceso import Acceso
from datetime import datetime

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
        self.usuarios.sort(key=lambda u: u.username)  # Ordenar usuarios
        with open('usuarios.ispc', 'wb') as f:
            pickle.dump(self.usuarios, f)

    def agre_u(self, username, password, email):
        nuevo_usuario = Usuario(self.next_id, username, password, email)
        self.usuarios.append(nuevo_usuario)
        self.next_id += 1
        self.guardar_usuarios()
        print(f'Usuario {username} agregado exitosamente.')

    def buscar_u(self, identifier):
        self.usuarios.sort(key=lambda u: u.username)  # Asegurarse de que está ordenado para búsqueda binaria
        low, high = 0, len(self.usuarios) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.usuarios[mid].username == identifier or self.usuarios[mid].email == identifier:
                return self.usuarios[mid]
            elif self.usuarios[mid].username < identifier:
                low = mid + 1
            else:
                high = mid - 1
        return None
    
    def modif_u(self, identifier, new_username=None, new_password=None, new_email=None):
        usuario = self.buscar_u(identifier)
        if usuario:
            if new_username:
                usuario.username = new_username
            if new_password:
                usuario.password = new_password
            if new_email:
                usuario.email = new_email
            self.guardar_usuarios()
            print(f'Usuario {identifier} modificado exitosamente.')
        else:
            print(f'Usuario {identifier} no encontrado.')

    def elim_u(self, identifier):
        usuario = self.buscar_u(identifier)
        if usuario:
            self.usuarios.remove(usuario)
            self.guardar_usuarios()
            print(f'Usuario {identifier} eliminado exitosamente.')
        else:
            print(f'Usuario {identifier} no encontrado.')


    def verificar_acceso(self, username, password):
        usuario = self.buscar_u(username)
        if usuario and usuario.password == password:
            return usuario
        return None

    def registrar_acceso(self, usuario):
        try:
            acceso = Acceso(len(self.usuarios), datetime.now(), None, usuario.username)
            with open('accesos.ispc', 'ab') as f:
                pickle.dump(acceso, f)
            print(f"Acceso registrado para {usuario.username}")
        except Exception as e:
            print(f"Error al registrar acceso: {e}")

    def registrar_intento_fallido(self, username, password):
        try:
            with open('logs.txt', 'a') as f:
                f.write(f'{datetime.now()}: Intento fallido con usuario: {username}, Contraseña: {password}\n')
            print(f"Intento fallido registrado para {username}")
        except Exception as e:
            print(f"Error al registrar intento fallido: {e}")

    def mostrar_u(self):
        if not self.usuarios:
            print('No hay usuarios registrados.')
        else:
            for usuario in self.usuarios:
                print(usuario)
                
