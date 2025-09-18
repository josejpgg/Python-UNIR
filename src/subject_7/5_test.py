# Crea un DataFrame de Pandas que contenga información sobre ventas de productos. El DataFrame debe tener las siguientes columnas: 'producto', 'precio', 'unidades_vendidas' y 'fecha_venta'.

# Incluye al menos 5 productos diferentes con sus respectivos datos. Las fechas de venta deben estar en formato datetime y corresponder al año actual.

# Una vez creado el DataFrame, realiza las siguientes operaciones:

# Añade una nueva columna llamada 'ingresos_totales' que calcule el producto entre 'precio' y 'unidades_vendidas'.
# Muestra los productos ordenados de mayor a menor ingreso total.
# Calcula y muestra el precio promedio de todos los productos.
# Identifica y muestra el producto con más unidades vendidas.
# Puedes comenzar importando las bibliotecas necesarias y creando un diccionario con los datos para construir el DataFrame.

import pandas as pd

series_date = pd.date_range('20250201', periods=5)
df = pd.DataFrame({
	'producto': ['A', 'B', 'C', 'D', 'E'],
	'precio': [100, 150, 200, 250, 300],
	'unidades_vendidas': [10, 15, 20, 25, 30],
	'fecha_venta': series_date
})

df['ingresos_totales'] = df['precio'] * df['unidades_vendidas']
print(f"Productos ordenados de mayor a menor ingresos totales:\n{df.sort_values(by='ingresos_totales', ascending=False)}")
print(f"Precio promedio de todos los productos: {df['precio'].mean()}")
print(f"Producto con más unidades vendidas: {df.loc[df['unidades_vendidas'].idxmax()]['producto']}")
