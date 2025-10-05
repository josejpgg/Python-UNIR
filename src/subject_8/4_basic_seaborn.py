import seaborn as sns
import matplotlib.pyplot as plt

# Configurar el tema de Seaborn
sns.set_theme()

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('tips')

# Crear un diagrama de dispersión
sns.scatterplot(data=datos, x='total_bill', y='tip', hue='time')

# Mostrar el gráfico
plt.show()













import pandas as pd

# Crear un DataFrame de ejemplo
datos = pd.DataFrame({
    'edad': [23, 45, 12, 36, 22],
    'ingresos': [50000, 80000, 20000, 60000, 45000],
    'sexo': ['M', 'F', 'M', 'F', 'M']
})

# Crear un gráfico de barras con Seaborn
sns.barplot(data=datos, x='sexo', y='ingresos')

# Mostrar el gráfico
plt.show()











import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Suponiendo un DataFrame 'ventas' con una columna de fechas
ventas = pd.DataFrame({
    'fecha': pd.date_range(start='2023-01-01', periods=12, freq='ME'),
    'monto': rng.integers(1000, 5000, size=12)
})

# Convertir la columna 'fecha' en el índice del DataFrame
ventas.set_index('fecha', inplace=True)

# Crear un gráfico de línea con Seaborn
sns.lineplot(data=ventas, x=ventas.index, y='monto')

# Mostrar el gráfico
plt.show()



























# Cargar el dataset "tips"
datos = sns.load_dataset('tips')

# Mostrar las primeras cinco filas del dataset
print(datos.head())


import matplotlib.pyplot as plt

# Crear un gráfico de dispersión
sns.scatterplot(data=datos, x='total_bill', y='tip')

# Mostrar el gráfico
plt.show()




















# Cargar el dataset "penguins"
datos_penguins = sns.load_dataset('penguins')

# Crear un histograma de la longitud del pico
sns.histplot(data=datos_penguins, x='bill_length_mm', hue='species', multiple='stack')

# Mostrar el gráfico
plt.show()
















import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
diamonds = sns.load_dataset('diamonds')

# Histograma de los precios de los diamantes
sns.histplot(data=diamonds, x='price', kde=True)
plt.show()
























import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
datos = sns.load_dataset('penguins')

# Crear un gráfico de dispersión
sns.scatterplot(data=datos, x='bill_length_mm', y='bill_depth_mm', hue='species')

# Guardar el gráfico en formato PNG
plt.savefig('grafico_penguins.png', dpi=300)

# Mostrar el gráfico en pantalla
plt.show()

















import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('iris')

# Crear un gráfico de dispersión con Seaborn
grafico = sns.scatterplot(data=datos, x='sepal_length', y='sepal_width', hue='species')

# Personalizar el gráfico utilizando Matplotlib
grafico.set_title('Relación entre longitud y ancho de sépalo')
grafico.set_xlabel('Longitud del sépalo (cm)')
grafico.set_ylabel('Ancho del sépalo (cm)')

# Mostrar el gráfico
plt.show()
