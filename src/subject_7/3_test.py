# Crea un array NumPy bidimensional de 4x5 con números aleatorios entre 0 y 100. Luego, realiza las siguientes operaciones:

# Calcula la media de todo el array
# Calcula la desviación estándar de todo el array
# Encuentra el valor máximo y mínimo de todo el array
# Calcula la suma de cada fila del array
# Calcula la media de cada columna del array
# Guarda cada resultado en variables separadas llamadas: media_total, desviacion_estandar, valor_maximo, valor_minimo, suma_filas y media_columnas.

import numpy as np

arr_2d = np.random.randint(1, 101, size=(4,5))

media_total = arr_2d.mean()
desviacion_estandar = arr_2d.std()
valor_maximo = arr_2d.max()
valor_minimo = arr_2d.min()
suma_filas = arr_2d.sum(axis=1)
media_columnas = arr_2d.mean(axis=0)

print(f"Media:\t{media_total}")
print(f"Desviación estandar:\t{desviacion_estandar}")
print(f"Valor maximo:\t{valor_maximo}")
print(f"Valor minimo:\t{valor_minimo}")
print(f"Suma todas las filas:\t{suma_filas}")
print(f"Media de cada columna:\t{media_columnas}")
