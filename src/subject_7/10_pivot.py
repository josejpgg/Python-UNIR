import pandas as pd
import numpy as np

# Sintaxis básica
# df.pivot_table(
#     values='columna_valores',
#     index='columna_filas',
#     columns='columna_columnas',
#     aggfunc='función_agregación',
#     fill_value=0,
#     margins=False
# )












# values: Especifica qué columna(s) contiene los valores a agregar.
# index: Define qué columna(s) se usará como índice de filas.
# columns: Determina qué columna(s) se usará para las columnas.
# aggfunc: Función de agregación a aplicar ('sum', 'mean', 'count', etc., o funciones personalizadas).
# fill_value: Valor para reemplazar los NaN.
# margins: Si es True, agrega filas y columnas de totales.

# Creamos un DataFrame de ejemplo
data = {
    'fecha': pd.date_range(start='2023-01-01', periods=20),
    'producto': np.random.choice(['Laptop', 'Tablet', 'Smartphone'], 20),
    'región': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], 20),
    'ventas': np.random.randint(5, 50, 20),
    'unidades': np.random.randint(1, 10, 20)
}

df = pd.DataFrame(data)

# Creamos una tabla pivotante básica
tabla_ventas = df.pivot_table(
    values='ventas',
    index='producto',
    columns='región',
    aggfunc='sum'
)

print(tabla_ventas)
# El resultado mostrará una tabla donde cada producto aparece en las filas, cada región en las columnas, y los valores son la suma de ventas para cada combinación.





















# pd.crosstab(
#     index=df['columna_filas'],
#     columns=df['columna_columnas'],
#     values=df['columna_valores'],
#     aggfunc='función_agregación',
#     normalize=False,
#     margins=False
# )

# normalize: Permite normalizar los valores (por filas, columnas o total).
# Análisis de frecuencias: Es ideal para analizar distribuciones conjuntas.

# Tabla de contingencia básica
tabla_contingencia = pd.crosstab(
    index=df['producto'],
    columns=df['región']
)

print(tabla_contingencia)

# Esta tabla mostrará el recuento de ocurrencias para cada combinación de producto y región.




















# Preagregación de datos para mejorar rendimiento
df_preaggregated = df_ventas.groupby(['producto', 'región']).agg({
    'ventas': ['sum', 'mean'],
    'unidades': 'sum',
    'margen': 'sum'
}).reset_index()

# Ahora creamos la tabla pivotante con datos preagregados
tabla_optimizada = df_preaggregated.pivot_table(
    index='producto',
    columns='región',
    values=[('ventas', 'sum'), ('ventas', 'mean'), 
            ('unidades', 'sum'), ('margen', 'sum')]
)

print("\nTabla optimizada con datos preagregados:")
print(tabla_optimizada.round(2))










