# Crea un programa que genere un array NumPy tridimensional de tamaño 4x3x2 con valores aleatorios enteros entre 1 y 100. Luego, muestra por pantalla la siguiente información sobre el array:

# La forma (shape) del array
# El número de dimensiones (ndim) del array
# El número total de elementos (size) del array
# El tipo de datos (dtype) del array
# El tamaño en bytes de cada elemento (itemsize) del array
# El tamaño total en bytes (nbytes) del array
# Finalmente, verifica e imprime si el tamaño total en bytes (nbytes) es igual al producto del número de elementos (size) por el tamaño de cada elemento (itemsize).

import numpy as np

arr_3d = np.random.randint(1, 101, size=(4,3,2))

print(f"Forma shape: {arr_3d.shape}")
print(f"Numero de dimensiones ndim: {arr_3d.ndim}")
print(f"Tamaño size: {arr_3d.size}")
print(f"Tipo de datos dtype: {arr_3d.dtype}")
print(f"Tamaño de cada elemento itemsize (byte): {arr_3d.itemsize}")
print(f"Tamaño total nbytes (bytes): {arr_3d.nbytes}")

print(f"Comprobar tamaño bytes = size * itemsize: {'TRUE' if arr_3d.nbytes == arr_3d.size * arr_3d.itemsize else 'FALSE'}")
