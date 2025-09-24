# Tienes dos DataFrames con información de ventas y productos. El primer DataFrame ventas contiene las columnas 'id_producto', 'fecha' y 'unidades_vendidas'. El segundo DataFrame productos contiene las columnas 'id_producto', 'nombre' y 'precio'. Debes realizar las siguientes tareas:

# Crea los dos DataFrames con los siguientes datos:
# ventas: id_producto (A1, A2, A3, A4, A2), fecha (usar fechas consecutivas desde '2023-01-01'), unidades_vendidas (10, 5, 8, 12, 7)
# productos: id_producto (A1, A2, A3, A5), nombre ('Laptop', 'Monitor', 'Teclado', 'Mouse'), precio (1200, 300, 100, 50)
# Realiza una unión (merge) de tipo 'inner' entre ambos DataFrames usando la columna 'id_producto'.

# Realiza una unión (merge) de tipo 'left' entre ambos DataFrames.

# Realiza una unión (merge) de tipo 'outer' entre ambos DataFrames.

# Crea una nueva columna 'valor_total' en el resultado de la unión 'inner' que multiplique las 'unidades_vendidas' por el 'precio'.

# Muestra el resultado de cada operación.

import pandas as pd

ventas = pd.DataFrame({
	'id_producto': ['A1', 'A2', 'A3', 'A4', 'A2'],
	'fecha': pd.date_range(start='2023-01-01', periods=5, freq='D'),
	'unidades_vendidas': [10, 5, 8, 12, 7]
})

productos = pd.DataFrame({
	'id_producto': ['A1', 'A2', 'A3', 'A5'],
	'nombre': ['Laptop', 'Monitor', 'Teclado', 'Mouse'],
	'precio': [1200, 300, 100, 50]
})

union_inner = pd.merge(ventas, productos, how='inner', on='id_producto')

union_left = pd.merge(ventas, productos, how='left', on='id_producto')

union_outer = pd.merge(ventas, productos, how='outer', on='id_producto')

new_inner_column = union_inner.copy()
new_inner_column['valor_total'] = new_inner_column['unidades_vendidas'] * new_inner_column['precio']

print(f"Union Inner:\n{union_inner}\n")

print(f"Union Left:\n{union_left}\n")

print(f"Union Outer:\n{union_outer}\n")

print(f"Valor Total en Union Inner:\n{new_inner_column[['id_producto', 'valor_total']]}\n")

