import pickle
from datetime import datetime
import os
from GestionUsuario import GestionUsuario

class OrdenamientoBusqueda:
    def __init__(self):
        self.usuario_manager = GestionUsuario()

    # 1. Ordenar usuarios por username usando burbuja y guardar en archivo específico
    def ordenar_usuarios_por_username(self):
  
        usuarios = self.usuario_manager.usuarios.copy()  # Copiar para no afectar el archivo original
        n = len(usuarios)
        
        # Ordenamiento burbuja
        for i in range(n):
            for j in range(0, n - i - 1):
                if usuarios[j].get_username() > usuarios[j + 1].get_username():
                    usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]

        # Verifica si la carpeta existe, si no, la crea
        if not os.path.exists('búsquedasYordenamientos'):
            os.makedirs('búsquedasYordenamientos')

        # Guardar en archivo específico
        try:
            with open('búsquedasYordenamientos/usuariosOrdenadosPorUsername.ispc', 'wb') as f:
                pickle.dump(usuarios, f)
            print("Usuarios ordenados por username y guardados en usuariosOrdenadosPorUsername.ispc")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    # 2. Búsqueda por username con técnica secuencial o binaria según la existencia del archivo de ordenamiento
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
    
    # 3. Búsqueda binaria para DNI
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
            print("Se utilizó la búsqueda secuencial para email.")
            print(f"Usuario encontrado: {resultado}")
        else:
            print("Usuario no encontrado.")

    # Búsqueda secuencial
    def busqueda_secuencial(self, lista, valor, atributo):
        log = []
        for usuario in lista:
            log.append(f"Comparando con {getattr(usuario, 'get_' + atributo)()}")
            if getattr(usuario, 'get_' + atributo)() == valor:
                return usuario, log
        log.append("Usuario no encontrado.")
        return None, log

    # Búsqueda binaria
    def busqueda_binaria(self, lista, valor, atributo):
        log = []
        left, right = 0, len(lista) - 1
        while left <= right:
            mid = (left + right) // 2
            usuario_mid = getattr(lista[mid], 'get_' + atributo)()
            log.append(f"Comparando {valor} con {usuario_mid}")
            if usuario_mid == valor:
                log.append("Usuario encontrado.")
                return lista[mid], log
            elif usuario_mid < valor:
                log.append("Buscar en la mitad derecha.")
                left = mid + 1
            else:
                log.append("Buscar en la mitad izquierda.")
                right = mid - 1
        log.append("Usuario no encontrado.")
        return None, log

    # Guardar log de búsquedas binarias
    def guardar_log_busqueda(self, log, filename_prefix):
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f'búsquedasYordenamientos/{filename_prefix}-{fecha}.txt'
        with open(filename, 'w') as f:
            for entry in log:
                f.write(entry + "\n")
        print(f"Log de búsqueda guardado en {filename}")
