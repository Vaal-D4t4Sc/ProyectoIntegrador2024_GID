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

    def crear_registros_pluviales(self, year):
        # Verificar si el archivo ya existe
        filename = f'registroPluvial{year}.csv'
        try:
            df = pd.read_csv(filename)
            print(f"Registros pluviales cargados desde {filename}")
            return df
        except FileNotFoundError:
            # Generar registros aleatorios
            data = {month: [random.randint(0, 100) for _ in range(31)] for month in range(1, 13)}
            # Convertir a DataFrame
            df = pd.DataFrame.from_dict(data, orient='index').transpose().fillna(0)
            df.columns = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
            df.to_csv(filename, index=False)
            print(f"Registros pluviales generados y guardados en {filename}")
            return df

    def mostrar_registros_mes(self, df):
        month = int(input("Seleccione un mes (1-12): "))
        if month in df.columns:
            print(df[month-1])
        else:
            print("Mes no válido.")

    def graficar_registros(self, df):
        # Gráfico de barras
        df.sum().plot(kind='bar')
        plt.title('Lluvias Anuales')
        plt.xlabel('Meses')
        plt.ylabel('Milímetros de lluvia')
        plt.show()

        # Gráfico de dispersión
        for i in range(len(df)):
            plt.scatter(df.columns, df.iloc[i], label=f'Día {i+1}')
        plt.title('Lluvias Diarias')
        plt.xlabel('Meses')
        plt.ylabel('Milímetros de lluvia')
        plt.show()

        # Gráfico circular
        df.sum().plot(kind='pie', autopct='%1.1f%%')
        plt.title('Distribución de Lluvias por Mes')
        plt.show()                