import pandas as pd
import numpy as np

# Serie con índice explícito
serie_etiquetada = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print(serie_etiquetada)

# Acceder al array de valores
print("Valores:", serie_etiquetada.values)

# Acceder al índice
print("Índice:", serie_etiquetada.index)

# Valores: [100 200 300]
# Índice: Index(['a', 'b', 'c'], dtype='object')












# Serie con índice de fechas
fechas = pd.date_range('20230101', periods=3)
serie_temporal = pd.Series([10, 20, 30], index=fechas)
print(serie_temporal)



# 2023-01-01    10
# 2023-01-02    20
# 2023-01-03    30
# dtype: int64











# Creación desde un diccionario
datos_ciudades = {'Madrid': 3.2, 'Barcelona': 1.6, 'Valencia': 0.8, 'Sevilla': 0.7}
poblacion = pd.Series(datos_ciudades)
print(poblacion)



# Madrid       3.2
# Barcelona    1.6
# Valencia     0.8
# Sevilla      0.7
# dtype: float64











import numpy as np

# Desde array de NumPy básico
array_np = np.array([1, 2, 3, 4, 5])
serie_np = pd.Series(array_np)
print(serie_np)

# Desde array generado con funciones de NumPy
serie_lineal = pd.Series(np.linspace(0, 10, 5))  # 5 valores equidistantes entre 0 y 10
print("\nSerie con valores lineales:")
print(serie_lineal)

# Desde array con distribución aleatoria
serie_aleatoria = pd.Series(np.random.randn(5))  # 5 valores de distribución normal
print("\nSerie con valores aleatorios:")
print(serie_aleatoria)












# Función para generar secuencia de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Crear Serie con los primeros 8 números de Fibonacci
serie_fibonacci = pd.Series(list(fibonacci(8)))
print(serie_fibonacci)

# Función para generar datos con ruido
def datos_con_ruido(base, ruido, n):
    return [base + i + np.random.normal(0, ruido) for i in range(n)]

# Serie con tendencia lineal y ruido aleatorio
serie_tendencia = pd.Series(datos_con_ruido(100, 5, 5))
print("\nSerie con tendencia y ruido:")
print(serie_tendencia)










# Crear una Serie con datos numéricos
datos = pd.Series([12, 45, 23, 67, 34, 89, 56, 12])

# Estadísticas descriptivas básicas
print(f"Media: {datos.mean()}")
print(f"Mediana: {datos.median()}")
print(f"Desviación estándar: {datos.std()}")
print(f"Valor mínimo: {datos.min()}")
print(f"Valor máximo: {datos.max()}")

# Resumen estadístico completo
print("\nResumen estadístico:")
print(datos.describe())


# Media: 42.25
# Mediana: 39.5
# Desviación estándar: 27.79
# Valor mínimo: 12
# Valor máximo: 89

# Resumen estadístico:
# count     8.00
# mean     42.25
# std      27.79
# min      12.00
# 25%      17.50
# 50%      39.50
# 75%      61.50
# max      89.00
# dtype: float64


















# Crear una Serie con datos variados
calificaciones = pd.Series([85, 92, 78, 65, 98, 72, 88, 95], 
                          index=['Ana', 'Carlos', 'Elena', 'David', 
                                'Laura', 'Miguel', 'Sofía', 'Pablo'])

# Filtrado con condiciones booleanas
aprobados = calificaciones[calificaciones >= 70]
print("Estudiantes aprobados:")
print(aprobados)

# Filtrado múltiple
destacados = calificaciones[(calificaciones >= 90) & (calificaciones < 100)]
print("\nEstudiantes destacados:")
print(destacados)

# Usando query (más legible para condiciones complejas)
recuperacion = calificaciones.loc[calificaciones.between(65, 69)]
print("\nEstudiantes en recuperación:")
print(recuperacion)














# Serie con valores faltantes
datos_incompletos = pd.Series([10, np.nan, 30, np.nan, 50, 60])

# Detectar valores nulos
print("¿Dónde hay valores nulos?")
print(datos_incompletos.isna())

# Eliminar valores nulos
print("\nSerie sin valores nulos:")
print(datos_incompletos.dropna())

# Rellenar valores nulos
print("\nRellenando con ceros:")
print(datos_incompletos.fillna(0))

# Rellenar con el valor anterior o siguiente
print("\nRellenando con el valor anterior:")
print(datos_incompletos.fillna(method='ffill'))

print("\nRellenando con el valor siguiente:")
print(datos_incompletos.fillna(method='bfill'))

# Interpolación
print("\nInterpolación lineal:")
print(datos_incompletos.interpolate())




# ¿Dónde hay valores nulos?
# 0    False
# 1     True
# 2    False
# 3     True
# 4    False
# 5    False
# dtype: bool

# Serie sin valores nulos:
# 0    10.0
# 2    30.0
# 4    50.0
# 5    60.0
# dtype: float64

# Rellenando con ceros:
# 0    10.0
# 1     0.0
# 2    30.0
# 3     0.0
# 4    50.0
# 5    60.0
# dtype: float64

# Rellenando con el valor anterior:
# 0    10.0
# 1    10.0
# 2    30.0
# 3    30.0
# 4    50.0
# 5    60.0
# dtype: float64

# Rellenando con el valor siguiente:
# 0    10.0
# 1    30.0
# 2    30.0
# 3    50.0
# 4    50.0
# 5    60.0
# dtype: float64

# Interpolación lineal:
# 0    10.0
# 1    20.0
# 2    30.0
# 3    40.0
# 4    50.0
# 5    60.0
# dtype: float64


















import pandas as pd
import numpy as np

# Crear una Serie con índice personalizado
ventas = pd.Series([1200, 1500, 900, 1800, 1350],
                  index=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'])


# Acceder a un único elemento
print("Ventas del martes:", ventas.loc['Martes'])

# Acceder a múltiples elementos
print("\nVentas de inicio de semana:")
print(ventas.loc[['Lunes', 'Martes']])

# Acceder a un rango de etiquetas (inclusivo)
print("\nVentas de mitad de semana:")
print(ventas.loc['Martes':'Jueves'])


# Ventas del martes: 1500

# Ventas de inicio de semana:
# Lunes     1200
# Martes    1500
# dtype: int64

# Ventas de mitad de semana:
# Martes      1500
# Miércoles    900
# Jueves      1800
# dtype: int64








# Acceder al primer elemento (posición 0)
print("Primer día:", ventas.iloc[0])

# Acceder a múltiples posiciones
print("\nPrimero y último día:")
print(ventas.iloc[[0, 4]])

# Acceder a un rango de posiciones (el último no inclusivo)
print("\nTres días centrales:")
print(ventas.iloc[1:4])

# Primer día: 1200

# Primero y último día:
# Lunes      1200
# Viernes    1350
# dtype: int64

# Tres días centrales:
# Martes      1500
# Miércoles    900
# Jueves      1800
# dtype: int64















# Creando un DataFrame con índice jerárquico
idx = pd.MultiIndex.from_tuples([
    ('España', 'Madrid'),
    ('España', 'Barcelona'),
    ('España', 'Sevilla'),
    ('España', 'Valencia')
], names=['país', 'ciudad'])

df = pd.DataFrame({
    'nombre': ['Ana', 'Carlos', 'Lucía', 'Miguel'],
    'edad': [28, 32, 25, 41]
}, index=idx)

print(df)

#                  nombre  edad
# país   ciudad                
# España Madrid       Ana    28
#        Barcelona  Carlos    32
#        Sevilla    Lucía    25
#        Valencia  Miguel    41













# Creamos un DataFrame más complejo para análisis
df_ventas = pd.DataFrame({
    'producto': ['A', 'B', 'C', 'D', 'E'] * 4,
    'región': ['Norte', 'Sur', 'Este', 'Oeste'] * 5,
    'ventas': np.random.randint(100, 1000, 20),
    'descuento': np.random.uniform(0, 0.3, 20),
    'fecha': pd.date_range('2023-01-01', periods=20)
})

# Explorando la estructura
print(df_ventas.shape)  # Dimensiones (filas, columnas)
print(df_ventas.info())  # Resumen completo
print(df_ventas.describe())  # Estadísticas descriptivas de columnas numéricas















# import sqlite3

# # Conexión a base de datos SQLite
# conexion = sqlite3.connect('base_datos.db')

# # Importando desde consulta SQL
# df_sql = pd.read_sql('SELECT * FROM ventas', conexion)

# # Importando tabla completa
# df_tabla = pd.read_sql_table('ventas', conexion)

# # Importando desde consulta parametrizada
# df_param = pd.read_sql('SELECT * FROM ventas WHERE region = ?', 
#                       conexion, params=('Norte',))

# # Cerrando conexión
# conexion.close()

















# Seleccionar filas donde el precio es mayor a 500
productos_caros = df.loc[df['precio'] > 500]
print(productos_caros)

# Seleccionar filas con múltiples condiciones
filtro_complejo = df.loc[(df['precio'] > 300) & (df['stock'] > 20)]
print(filtro_complejo)

# Seleccionar filas que cumplen condiciones y solo algunas columnas
resultado = df.loc[df['disponible'] == True, ['producto', 'precio']]
print(resultado)








# Modificar un valor específico
df.loc['C', 'disponible'] = True

# Modificar múltiples valores
df.loc['A':'B', 'precio'] = [1300, 650]

# Modificar valores basados en una condición
df.loc[df['stock'] < 20, 'stock'] += 5

print(df)


















# Seleccionar la primera fila
primera_fila = df.iloc[0]
print(primera_fila)

# Seleccionar múltiples filas por posición
filas_seleccionadas = df.iloc[[0, 2, 4]]
print(filas_seleccionadas)

# Seleccionar filas y columnas por posición
subset_posicional = df.iloc[1:3, 0:2]
print(subset_posicional)

# Seleccionar filas alternas
filas_alternas = df.iloc[::2]  # Filas 0, 2, 4
print(filas_alternas)

# Seleccionar la última fila
ultima_fila = df.iloc[-1]
print(ultima_fila)













# .at[]: Acceso rápido a un único elemento usando etiquetas
# .iat[]: Acceso rápido a un único elemento usando posiciones enteras

# Acceder a un valor específico con .at (usando etiquetas)
precio_tablet = df.at['B', 'precio']
print(f"Precio de la tablet: {precio_tablet}")

# Acceder a un valor específico con .iat (usando posiciones)
stock_movil = df.iat[2, 2]  # Fila 2, columna 2
print(f"Stock de móviles: {stock_movil}")

# Modificar un valor específico
df.at['D', 'stock'] = 12
df.iat[0, 1] = 1250  # Actualizar el precio de la laptop

print(df)














