# gestionUsuario.py
import pickle
from usuario import Usuario
import os
from datetime import datetime

class GestionUsuario:
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
        self.usuarios.sort(key=lambda u: u.get_id())  # Ordenar por ID
        with open('usuarios.ispc', 'wb') as f:
            pickle.dump(self.usuarios, f)

    def agregar_usuario(self, username, DNI, password, email):
        nuevo_usuario = Usuario(self.next_id, username, DNI, password, email)
        self.usuarios.append(nuevo_usuario)
        self.next_id += 1
        self.guardar_usuarios()
        print(f'Usuario {username} agregado exitosamente.')

    def modificar_usuario(self, identifier, new_username=None, new_password=None, new_email=None):
        usuario = self.buscar_usuario(identifier)
        if usuario:
            if new_username:
                usuario.set_username(new_username)
            if new_password:
                usuario.set_password(new_password)
            if new_email:
                usuario.set_email(new_email)
            self.guardar_usuarios()
            print(f'Usuario {identifier} modificado exitosamente.')
        else:
            print(f'Usuario {identifier} no encontrado.')
    
    def buscar_usuario(self, identifier):
    # Buscar usuario por DNI, username o email
        for usuario in self.usuarios:
            if usuario.get_DNI() == identifier or usuario.get_username() == identifier or usuario.get_email() == identifier:
                return usuario
        return None

    def eliminar_usuario(self, identifier):
        usuario = self.buscar_usuario(identifier)
        if usuario:
            self.usuarios.remove(usuario)
            self.guardar_usuarios()
            print(f'Usuario {identifier} eliminado exitosamente.')
        else:
            print(f'Usuario {identifier} no encontrado.')