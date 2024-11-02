import pandas as pd
import random
import matplotlib.pyplot as plt

class AnalisisDatos:
    def crear_registros_pluviales(self, year):
        filename = f'registroPluvial{year}.csv'
        try:
            df = pd.read_csv(filename)
            print(f"Registros pluviales cargados desde {filename}")
            return df
        except FileNotFoundError:
            # Generar registros aleatorios
            data = {}
            for month in range(1, 13):
                if month in [1, 3, 5, 7, 8, 10, 12]:  # 31 días
                    dias = [random.randint(0, 100) for _ in range(31)]
                elif month == 2:  # Febrero, asumiendo 28 días
                    dias = [random.randint(0, 100) for _ in range(28)]
                else:  # 30 días
                    dias = [random.randint(0, 100) for _ in range(30)]
                data[month] = dias
            
            # Convertir a DataFrame
            df = pd.DataFrame.from_dict(data, orient='index').transpose().fillna(0)
            df.columns = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
            df.to_csv(filename, index=False)
            print(f"Registros pluviales generados y guardados en {filename}")
            return df

    def mostrar_registros_mes(self, df):
        month = int(input("Seleccione un mes (1-12): "))
        if 1 <= month <= 12:
            print(f"Registros de {df.columns[month - 1]}:")
            print(df[df.columns[month - 1]])
        else:
            print("Mes no válido.")

    def graficar_registros(self, df):
        # Gráfico de barras
        df.sum().plot(kind='bar')
        plt.title('Lluvias Anuales')
        plt.xlabel('Meses')
        plt.ylabel('Milímetros de lluvia')
        plt.xticks(rotation=45)
        plt.show()

        # Gráfico de dispersión
        for i in range(len(df)):
            plt.scatter(df.columns, df.iloc[i], label=f'Día {i + 1}')
        plt.title('Lluvias Diarias')
        plt.xlabel('Meses')
        plt.ylabel('Milímetros de lluvia')
        plt.legend()
        plt.show()

        # Gráfico circular en sentido horario
        df.sum().plot(kind='pie', autopct='%1.1f%%', counterclock=False)
        plt.title('Distribución de Lluvias por Mes')
        plt.ylabel('')
        plt.show()