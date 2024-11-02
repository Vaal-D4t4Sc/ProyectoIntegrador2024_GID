import pickle
from datetime import datetime
from acceso import Acceso  # Asegúrate de importar la clase Acceso

class gestion_a:
    def __init__(self):
        self.accesos = self.cargar_accesos()

    def cargar_accesos(self):
        try:
            with open('accesos.ispc', 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    def guardar_accesos(self):
        with open('accesos.ispc', 'wb') as f:
            pickle.dump(self.accesos, f)

    def registrar_acceso(self, usuario):
        fecha_ingreso = datetime.now()
        nuevo_acceso = Acceso(len(self.accesos) + 1, fecha_ingreso, None, usuario.get_username())
        self.accesos.append(nuevo_acceso)
        self.guardar_accesos()
        print(f'Acceso registrado para {usuario.get_username()}.')

    def finalizar_acceso(self, usuario):
        for acceso in self.accesos:
            if acceso.get_usuarioLogueado() == usuario.get_username() and acceso.get_fechaSalida() is None:
                acceso.set_fechaSalida(datetime.now())
                self.guardar_accesos()
                print(f'Acceso finalizado para {usuario.get_username()}.')
                return
        print(f'No se encontró un acceso activo para {usuario.get_username()}.')

    def mostrar_accesos(self):
        for acceso in self.accesos:
            print(acceso)

    def mostrar_intentos_fallidos(self):
        # Aquí se implementaría la lógica para mostrar los intentos fallidos.
        print("Mostrar logs de intentos fallidos aún no implementado.")
