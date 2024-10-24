from datetime import datetime

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado

    def __str__(self):
        return f'ID {self.id}, Usuario logueado: {self.usuarioLogueado}, Fecha de ingreso: {self.fechaIngreso}, Fecha de salida: {self.fechaSalida}'
