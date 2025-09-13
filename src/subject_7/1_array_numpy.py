import numpy as np

# Crear array a partir de una lista
lista = [1, 2, 3, 4, 5]
arr = np.array(lista)
print(arr)  # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>

# Crear array bidimensional
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
# [[1 2 3]
#  [4 5 6]]












# Especificar tipo de datos
arr_float = np.array([1, 2, 3], dtype=np.float64)
print(arr_float)  # [1. 2. 3.]
print(arr_float.dtype)  # float64

# Forzar tipo de datos entero
arr_int = np.array([1.1, 2.2, 3.3], dtype=np.int32)
print(arr_int)  # [1 2 3]










# Array unidimensional de ceros
ceros = np.zeros(5)
print(ceros)  # [0. 0. 0. 0. 0.]

# Array bidimensional de ceros (matriz 3x4)
matriz_ceros = np.zeros((3, 4))
print(matriz_ceros)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# Especificar tipo de datos
ceros_enteros = np.zeros(5, dtype=int)
print(ceros_enteros)  # [0 0 0 0 0]











# Array lleno de 7s
sietes = np.full(5, 7)
print(sietes)  # [7 7 7 7 7]

# Matriz 2x3 llena de pi
matriz_pi = np.full((2, 3), np.pi)
print(matriz_pi)
# [[3.14159265 3.14159265 3.14159265]
#  [3.14159265 3.14159265 3.14159265]]











import numpy as np

# Secuencia básica de enteros
arr1 = np.arange(5)
print(arr1)  # [0 1 2 3 4]

# Especificando inicio y fin (fin no incluido)
arr2 = np.arange(2, 8)
print(arr2)  # [2 3 4 5 6 7]

# Con paso personalizado
arr3 = np.arange(1, 10, 2)
print(arr3)  # [1 3 5 7 9]

# Con paso decimal
arr4 = np.arange(0, 1, 0.2)
print(arr4)  # [0.  0.2 0.4 0.6 0.8]












# Diccionario simple
diccionario = {'a': 1, 'b': 2, 'c': 3}

# Convertir solo los valores
valores = np.array(list(diccionario.values()))
print(valores)  # [1 2 3]

# Convertir claves y valores como arrays separados
claves = np.array(list(diccionario.keys()))
print(claves)  # ['a' 'b' 'c']

# Diccionario de arrays
dict_arrays = {'x': [1, 2, 3], 'y': [4, 5, 6]}
x_array = np.array(dict_arrays['x'])
y_array = np.array(dict_arrays['y'])









from scipy import sparse

# Crear una matriz dispersa en SciPy
matriz_dispersa = sparse.csr_matrix((3, 4), dtype=np.int8)
matriz_dispersa[0, 0] = 1
matriz_dispersa[2, 3] = 2

print(matriz_dispersa)
# (0, 0)	1
# (2, 3)	2

# Convertir a array denso de NumPy
arr_denso = matriz_dispersa.toarray()
print(arr_denso)
# [[1 0 0 0]
#  [0 0 0 0]
#  [0 0 0 2]]
