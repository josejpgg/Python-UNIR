# Dado un DataFrame con información de ventas mensuales, calcula las siguientes estadísticas:

# Utiliza el método describe() para obtener un resumen estadístico completo del DataFrame.
# Calcula la media, mediana y desviación estándar de la columna 'ventas'.
# Encuentra el valor máximo y mínimo de la columna 'unidades'.
# Calcula la correlación entre las columnas 'ventas' y 'unidades'.
# Para empezar, crea un DataFrame con los siguientes datos:

import pandas as pd

# Datos de ventas mensuales
data = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'ventas': [15200, 14800, 16700, 17500, 18200],
    'unidades': [120, 115, 140, 150, 160],
    'gastos': [5100, 4800, 5400, 5800, 6000]
}

# Crea el DataFrame
df_ventas = pd.DataFrame(data)

print(f"Resumen estadístico del Dataframe de ventas:\n{df_ventas.describe(include='all')}")

print("Calculo sobre la columna ventas:")
print(f"Media: {df_ventas['ventas'].mean()}")
print(f"Mediana: {df_ventas['ventas'].median()}")
print(f"Desviación estándar: {df_ventas['ventas'].std().round(4)}")
print(f"Correlación entre las columnas Ventas y Unidades: {
	df_ventas['ventas'].corr(df_ventas['unidades']).round(4)
}")

print("\nCalculo sobre la columna unidades:")
print(f"Valor mínimo: {df_ventas['unidades'].min()}")
print(f"Valor máximo: {df_ventas['unidades'].max()}")

