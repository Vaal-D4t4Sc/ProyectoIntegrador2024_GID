import random
import pandas as pd
import matplotlib.pyplot as plt

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
