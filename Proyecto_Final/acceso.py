from datetime import datetime

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.__id = id
        self.__fechaIngreso = fechaIngreso
        self.__fechaSalida = fechaSalida
        self.__usuarioLogueado = usuarioLogueado

    # Métodos get
    def get_id(self):
        return self.__id

    def get_fechaIngreso(self):
        return self.__fechaIngreso

    def get_fechaSalida(self):
        return self.__fechaSalida

    def get_usuarioLogueado(self):
        return self.__usuarioLogueado

    # Métodos set
    def set_fechaIngreso(self, fechaIngreso):
        self.__fechaIngreso = fechaIngreso

    def set_fechaSalida(self, fechaSalida):
        self.__fechaSalida = fechaSalida

    def set_usuarioLogueado(self, usuarioLogueado):
        self.__usuarioLogueado = usuarioLogueado

    # Representación en string
    def __str__(self):
        return f'ID {self.__id}, Usuario logueado: {self.__usuarioLogueado}, Fecha de ingreso: {self.__fechaIngreso}, Fecha de salida: {self.__fechaSalida}'