import pandas as pd
import numpy as np

# Creamos un DataFrame de ejemplo
df = pd.DataFrame({
    'numérico': [10, 20, 30, 40, 50, np.nan],
    'categórico': ['a', 'b', 'c', 'a', 'b', 'c'],
    'fecha': pd.date_range('20230101', periods=6)
})

# Aplicamos describe() al DataFrame
resumen = df.describe()
print(resumen)








# Incluir todos los tipos de datos
resumen_completo = df.describe(include='all')
print(resumen_completo)

# Especificar percentiles personalizados
resumen_percentiles = df.describe(percentiles=[0.2, 0.4, 0.6, 0.8])
print(resumen_percentiles)







# Solo columnas numéricas (comportamiento por defecto)
df.describe(include=[np.number])

# Solo columnas de texto
df.describe(include=['object'])

# Solo columnas de fecha
df.describe(include=['datetime64'])

# Combinación de tipos
df.describe(include=['object', 'datetime64'])






# En Pandas 2 podemos usar datetime_is_numeric=True para tratar fechas como numéricas
# df.describe(datetime_is_numeric=True)

# También podemos excluir ciertos tipos de datos
df.describe(exclude=['datetime64'])









# Aplicar varias funciones a todas las columnas numéricas
resultado = df.agg(['sum', 'mean', 'median', 'min', 'max'])
print(resultado)

# Aplicar diferentes funciones a diferentes columnas
resultado_personalizado = df.agg({
    'A': ['sum', 'mean'],
    'B': ['min', 'max', 'std'],
    'C': 'median'
})
print(resultado_personalizado)







# Agrupar por la columna 'grupo' y calcular la media de cada grupo
agrupado = df.groupby('grupo').mean()
print("Media por grupo:\n", agrupado)

# Aplicar múltiples agregaciones a un groupby
agregaciones_multiples = df.groupby('grupo').agg(['count', 'sum', 'mean', 'std'])
print("Múltiples agregaciones por grupo:\n", agregaciones_multiples)














