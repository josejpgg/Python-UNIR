# Utilizando Pandas, crea una tabla pivotante que analice datos de ventas por categoría de producto y región.

# Primero, crea un DataFrame con los siguientes datos:

# 'categoría': Distribuye 30 valores entre ['Electrónica', 'Ropa', 'Hogar']
# 'región': Distribuye 30 valores entre ['Norte', 'Sur', 'Este', 'Oeste']
# 'ventas': 30 valores aleatorios entre 100 y 1000
# 'unidades': 30 valores aleatorios entre 1 y 20
# Luego, crea una tabla pivotante que muestre:

# La suma total de ventas para cada combinación de categoría y región
# Incluye totales por fila y columna (usando el parámetro margins)
# Reemplaza los valores NaN con ceros
# Tu solución debe importar las bibliotecas necesarias, crear el DataFrame de ejemplo y generar la tabla pivotante según las especificaciones.

import pandas as pd
import numpy as np

list_categoria = ['Electrónica', 'Ropa', 'Hogar']
list_region = ['Norte', 'Sur', 'Este', 'Oeste']

df_pivot = pd.DataFrame(
	{
		'categoria':np.random.choice(list_categoria, 30),
		'region':np.random.choice(list_region, 30),
		'ventas':np.random.randint(100,1000,30),
		'unidades':np.random.randint(1,20,30)
	}
)

print(f"La suma total de ventas para cada combinación de categoría y región:\n{
	df_pivot.pivot_table(
     index=['categoria','region'],
     values='ventas',
     aggfunc='sum',
     fill_value=0
	)
}")

print(f"Incluye totales por fila y columna:\n{
	df_pivot.pivot_table(
     index=['categoria','region'],
     values='ventas',
     aggfunc='sum',
     fill_value=0,
     margins=True,
     margins_name='Total'
	).reset_index()
}")

