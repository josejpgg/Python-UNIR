# Crea los siguientes arrays de NumPy:

# Un array unidimensional con los números del 1 al 10 utilizando array()
# Una matriz de ceros de tamaño 3x3 utilizando zeros()
# Un array unidimensional con 5 unos utilizando ones()
# Un array con 8 valores equidistantes entre 0 y 1 (ambos incluidos) utilizando linspace()
# Un array con los números pares del 2 al 20 utilizando arange()
# Asegúrate de importar NumPy correctamente al inicio de tu código.

import numpy as np

arr_uni = np.array(np.arange(1,11))
arr_zero = np.zeros((3,3))
arr_uni_ones = np.ones(5)
arr_linspace = np.linspace(0,1,8)
arr_pair = np.arange(2,21,2)

print(f"Array unidimensional con números del 1 al 10: {arr_uni}")
print(f"Matriz de ceros de tamaño 3x3: \n{arr_zero}")
print(f"Array unidimensional con 5 unos: {arr_uni_ones}")
print(f"Array con 8 valores equidistantes entre 0 y 1: {arr_linspace}")
print(f"Array con números pares del 2 al 20: {arr_pair}")

