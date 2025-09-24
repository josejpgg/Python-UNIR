import pandas as pd
import numpy as np


# concat(): Cuando queremos apilar DataFrames con estructura similar (vertical u horizontalmente)
# merge(): Cuando necesitamos relacionar datos basados en valores de columnas (como en bases de datos relacionales)
# join(): Cuando queremos combinar DataFrames basados en sus índices de forma sencilla




# CONCAT

# Creamos dos DataFrames con datos de ventas de diferentes trimestres
ventas_q1 = pd.DataFrame({
    'producto': ['A', 'B', 'C'],
    'ventas': [100, 200, 150]
})

ventas_q2 = pd.DataFrame({
    'producto': ['A', 'B', 'D'],
    'ventas': [120, 210, 190]
})

# Concatenamos verticalmente (por filas)
ventas_semestre = pd.concat([ventas_q1, ventas_q2], axis=0)
print("Concatenación vertical:")
print(ventas_semestre)














# MERGE

# Datos de productos
productos = pd.DataFrame({
    'producto_id': ['A', 'B', 'C', 'D'],
    'nombre': ['Laptop', 'Monitor', 'Teclado', 'Mouse'],
    'categoria': ['Computadoras', 'Periféricos', 'Periféricos', 'Periféricos']
})

# Datos de ventas
ventas = pd.DataFrame({
    'producto_id': ['A', 'B', 'B', 'C'],
    'tienda': ['Central', 'Norte', 'Sur', 'Central'],
    'unidades': [5, 3, 2, 7]
})

# Combinación inner (solo registros que coinciden en ambos DataFrames)
ventas_productos = pd.merge(ventas, productos, on='producto_id')
print("Merge inner:")
print(ventas_productos)

















# JOIN

# Datos de ventas
ventas = pd.DataFrame({
    'producto_id': ['A', 'B', 'B', 'C'],
    'tienda': ['Central', 'Norte', 'Sur', 'Central'],
    'unidades': [5, 3, 2, 7]
})

# DataFrame con nombre de columna diferente
inventario = pd.DataFrame({
    'codigo': ['A', 'B', 'C', 'E'],
    'stock': [15, 10, 20, 5]
})

# Configuramos índices
ventas_indexed = ventas.set_index('producto_id')

# Join con diferentes tipos
join_left = ventas_indexed.join(inventario.set_index('codigo'), how='left')
print("\nLeft join con método join():")
print(join_left)














# MELT

import pandas as pd
import numpy as np

# Creamos un DataFrame en formato ancho (ventas por producto y trimestre)
datos_ancho = pd.DataFrame({
    'producto': ['Laptop', 'Tablet', 'Móvil', 'Auriculares'],
    'Q1': [350, 270, 410, 170],
    'Q2': [390, 280, 430, 160],
    'Q3': [320, 290, 380, 190],
    'Q4': [400, 310, 450, 210]
})

print("Datos en formato ancho:")
print(datos_ancho)



# Transformamos de ancho a largo con melt()
datos_largo = pd.melt(
    datos_ancho,
    id_vars=['producto'],     # Columnas que mantienen su estructura
    value_vars=['Q1', 'Q2', 'Q3', 'Q4'],  # Columnas a "derretir"
    var_name='trimestre',     # Nombre para la columna de variables
    value_name='ventas'       # Nombre para la columna de valores
)

print("\nDatos transformados a formato largo con melt():")
print(datos_largo)


















# PIVOT
# La función pivot() realiza la operación inversa a melt(), convirtiendo datos de formato largo a ancho. Es como crear una tabla dinámica en Excel.

# Primero creamos datos en formato largo
datos_empleados = pd.DataFrame({
    'empleado': ['Ana', 'Ana', 'Ana', 'Carlos', 'Carlos', 'Carlos'],
    'año': [2021, 2022, 2023, 2021, 2022, 2023],
    'salario': [50000, 52000, 54000, 45000, 47000, 49000]
})

print("\nDatos originales en formato largo:")
print(datos_empleados)

# Transformamos a formato ancho con pivot()
tabla_pivote = datos_empleados.pivot(
    index='empleado',    # Filas de la tabla
    columns='año',       # Columnas de la tabla
    values='salario'     # Valores a mostrar
)

print("\nDatos transformados a formato ancho con pivot():")
print(tabla_pivote)
















# PIVOT TABLE
# Cuando tenemos valores duplicados en las combinaciones de índice y columnas, necesitamos usar pivot_table(), que permite especificar una función de agregación:


# Datos con valores duplicados
ventas_regionales = pd.DataFrame({
    'región': ['Norte', 'Norte', 'Sur', 'Sur', 'Norte', 'Sur'],
    'producto': ['A', 'B', 'A', 'B', 'A', 'B'],
    'ventas': [100, 150, 200, 250, 120, 230]
})

print("\nDatos con valores duplicados:")
print(ventas_regionales)

# Creamos una tabla pivote con agregación
tabla_agregada = pd.pivot_table(
    ventas_regionales,
    index='región',
    columns='producto',
    values='ventas',
    aggfunc='sum'  # Podemos usar 'mean', 'count', 'max', etc.
)

print("\nTabla pivote con agregación (suma):")
print(tabla_agregada)





# pivot_table() ofrece opciones adicionales para personalizar la agregación:

# Tabla pivote con múltiples funciones de agregación
tabla_multi_agg = pd.pivot_table(
    ventas_regionales,
    index='región',
    columns='producto',
    values='ventas',
    aggfunc=['sum', 'mean', 'count']
)

print("\nTabla pivote con múltiples agregaciones:")
print(tabla_multi_agg)

# Tabla pivote con valores de relleno y totales
tabla_completa = pd.pivot_table(
    ventas_regionales,
    index='región',
    columns='producto',
    values='ventas',
    aggfunc='sum',
    fill_value=0,       # Valor para celdas vacías
    margins=True,       # Añadir totales
    margins_name='Total'  # Nombre para la fila/columna de totales
)

print("\nTabla pivote con totales:")
print(tabla_completa)


















# AGG
# El método agg() permite aplicar múltiples funciones a diferentes columnas en una sola operación:

# Aplicamos diferentes funciones a distintas columnas
resumen_completo = ventas.groupby('vendedor').agg({
    'unidades': ['sum', 'mean'],
    'valor_total': ['sum', 'mean', 'max'],
    'fecha': ['min', 'max']  # Primera y última venta
})

print("\nResumen completo por vendedor:")
print(resumen_completo)





# Además de las funciones integradas, podemos usar funciones personalizadas con agg():

# Definimos una función personalizada para calcular el ratio de valor/unidades
def valor_por_unidad(x):
    return x.sum() / len(x)

# Función para calcular el porcentaje del total
def porcentaje_del_total(x):
    return x.sum() / ventas['valor_total'].sum() * 100

# Aplicamos funciones personalizadas
metricas_avanzadas = ventas.groupby('vendedor')['valor_total'].agg([
    'sum',
    ('promedio_por_venta', valor_por_unidad),
    ('porcentaje_total', porcentaje_del_total)
])

print("\nMétricas avanzadas por vendedor:")
print(metricas_avanzadas)














# FILTER

# El método filter() permite seleccionar grupos completos basándose en una condición:

# Filtramos para mostrar solo vendedores con más de 10 unidades vendidas
vendedores_top = ventas.groupby('vendedor').filter(lambda x: x['unidades'].sum() > 10)
print("\nVendedores con más de 10 unidades vendidas:")
print(vendedores_top[['vendedor', 'unidades', 'valor_total']])

# Filtramos para mostrar solo productos con valor total superior a 5000
productos_premium = ventas.groupby('producto').filter(lambda x: x['valor_total'].sum() > 5000)
print("\nProductos con valor total superior a 5000:")
print(productos_premium[['producto', 'unidades', 'valor_total']])




















# APPLY

# El método apply() es probablemente el más versátil y permite ejecutar una función a lo largo de un eje específico de un DataFrame o Series. Puede trabajar tanto con filas como con columnas.

import pandas as pd
import numpy as np

# Creamos un DataFrame de ejemplo
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

print("DataFrame original:")
print(df)

# Calculamos estadísticas básicas para cada columna
estadisticas = df.apply(lambda x: pd.Series({
    'suma': x.sum(),
    'media': x.mean(),
    'max': x.max(),
    'min': x.min()
}))

print("\nEstadísticas por columna:")
print(estadisticas)











# Calculamos la suma de cada fila
df['suma_fila'] = df.apply(lambda x: x.sum(), axis=1)

# Calculamos el valor máximo de cada fila
df['max_fila'] = df.apply(lambda x: x.max(), axis=1)

print("\nDataFrame con cálculos por fila:")
print(df)
















# APPLYMAP

# El método applymap() aplica una función a cada elemento individual de un DataFrame, permitiendo transformaciones elemento a elemento en toda la estructura.

# Creamos un DataFrame con valores mixtos
df_mixto = pd.DataFrame({
    'A': [1, -2, 3, -4, 5],
    'B': [0.1, 0.2, -0.3, 0.4, -0.5],
    'C': ['10%', '20%', '30%', '40%', '50%']
})

print("\nDataFrame con valores mixtos:")
print(df_mixto)

# Aplicamos valor absoluto a todos los elementos numéricos
# y dejamos las cadenas sin cambios
def valor_abs(x):
    try:
        return abs(float(x.strip('%')) if isinstance(x, str) and '%' in x else x)
    except:
        return x

df_abs = df_mixto.applymap(valor_abs)
print("\nDataFrame con valores absolutos:")
print(df_abs)










# DataFrame con valores numéricos
df_numerico = pd.DataFrame({
    'A': [1.23456, 2.34567, 3.45678],
    'B': [10.1234, 20.2345, 30.3456],
    'C': [100.123, 200.234, 300.345]
})

print("\nDataFrame numérico original:")
print(df_numerico)

# Formateamos todos los valores a 2 decimales
df_formateado = df_numerico.applymap(lambda x: f"{x:.2f}")
print("\nDataFrame con valores formateados:")
print(df_formateado)











