import pickle
from datetime import datetime
import os
from GestionUsuario import gestion_u

class ordenamiento_b:
    def __init__(self):
        self.usuario_manager = gestion_u()

    # 1. Ordenar usuarios por username usando burbuja y guardar en archivo específico
    def ordenar_usuarios_por_username(self):
        usuarios = self.usuario_manager.usuarios.copy()  # Copiar para no afectar el archivo original
        n = len(usuarios)

        # Ordenamiento burbuja
        for i in range(n):
            for j in range(0, n - i - 1):
                if usuarios[j].get_username() > usuarios[j + 1].get_username():
                    usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]

        # Guardar en archivo específico
        with open('búsquedasYordenamientos/usuariosOrdenadosPorUsername.ispc', 'wb') as f:
            pickle.dump(usuarios, f)
        print("Usuarios ordenados por username y guardados en usuariosOrdenadosPorUsername.ispc")

    # 2. Búsqueda por username con técnica secuencial o binaria
    def buscar_por_username(self, username):
        # Verificar si el archivo ordenado por username existe
        archivo_ordenado = 'búsquedasYordenamientos/usuariosOrdenadosPorUsername.ispc'
        if os.path.exists(archivo_ordenado):
            # Búsqueda binaria en el archivo ordenado
            with open(archivo_ordenado, 'rb') as f:
                usuarios = pickle.load(f)
            resultado, log = self.busqueda_binaria(usuarios, username, 'username')
            self.guardar_log_busqueda(log, 'buscandoUsuarioPorUsername')
        else:
            # Búsqueda secuencial en usuarios.ispc
            usuarios = self.usuario_manager.usuarios
            resultado, log = self.busqueda_secuencial(usuarios, username, 'username')
            print("Se utilizó la búsqueda secuencial para username.")

        # Mostrar el resultado
        if resultado:
            print(f"Usuario encontrado: {resultado}")
        else:
            print("Usuario no encontrado.")

    # 3. Búsqueda por DNI
    def buscar_por_dni(self, dni):
        usuarios = self.usuario_manager.usuarios  # usuarios.ispc está siempre ordenado por DNI
        resultado, log = self.busqueda_binaria(usuarios, dni, 'id')
        self.guardar_log_busqueda(log, 'buscandoUsuarioPorDNI')

        # Mostrar el resultado
        if resultado:
            print(f"Usuario encontrado: {resultado}")
        else:
            print("Usuario no encontrado.")

    # 4. Búsqueda secuencial por email
    def buscar_por_email(self, email):
        usuarios = self.usuario_manager.usuarios
        resultado, log = self.busqueda_secuencial(usuarios, email, 'email')

        # Mostrar el resultado
        if resultado:
            print("Se utilizó la búsqueda secuencial por email.")
            print(f"Usuario encontrado: {resultado}")
        else:
            print("Usuario no encontrado.")

    # Métodos de búsqueda
    def busqueda_binaria(self, usuarios, clave, tipo):
        log = []
        izquierda, derecha = 0, len(usuarios) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            log.append(f'Buscando en {usuarios[medio]}')
            if (tipo == 'username' and usuarios[medio].get_username() == clave) or (tipo == 'id' and usuarios[medio].get_id() == clave):
                return usuarios[medio], log
            elif (tipo == 'username' and usuarios[medio].get_username() < clave) or (tipo == 'id' and usuarios[medio].get_id() < clave):
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return None, log

    def busqueda_secuencial(self, usuarios, clave, tipo):
        log = []
        for usuario in usuarios:
            log.append(f'Comprobando {usuario}')
            if (tipo == 'username' and usuario.get_username() == clave) or (tipo == 'email' and usuario.get_email() == clave):
                return usuario, log
        return None, log

    def guardar_log_busqueda(self, log, nombre_archivo):
        with open(f'logs/{nombre_archivo}.txt', 'w') as f:
            for entry in log:
                f.write(f"{entry}\n")
        print(f"Log de búsqueda guardado en {nombre_archivo}.txt")

