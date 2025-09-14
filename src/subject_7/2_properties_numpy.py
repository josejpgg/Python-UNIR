import numpy as np

# Array unidimensional (vector)
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"Array 1D: {arr_1d}")
print(f"Shape: {arr_1d.shape}")

# Array bidimensional (matriz)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nArray 2D:\n{arr_2d}")
print(f"Shape: {arr_2d.shape}")

# Array tridimensional (cubo)
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"\nArray 3D:\n{arr_3d}")
print(f"Shape: {arr_3d.shape}")













import numpy as np

# Creamos arrays de diferentes dimensiones
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2], [3, 4]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr_4d = np.zeros((2, 2, 2, 2))  # Array 4D de ceros

# Comprobamos el número de dimensiones
print(f"Dimensiones de arr_1d: {arr_1d.ndim}")
print(f"Dimensiones de arr_2d: {arr_2d.ndim}")
print(f"Dimensiones de arr_3d: {arr_3d.ndim}")
print(f"Dimensiones de arr_4d: {arr_4d.ndim}")








import numpy as np

# Creamos arrays de diferentes formas
vector = np.array([1, 2, 3, 4])
matriz = np.array([[1, 2, 3], [4, 5, 6]])
cubo = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Obtenemos el tamaño total (número de elementos)
print(f"Vector shape: {vector.shape}, size: {vector.size}")
print(f"Matriz shape: {matriz.shape}, size: {matriz.size}")
print(f"Cubo shape: {cubo.shape}, size: {cubo.size}")

# Comprobamos que size es el producto de las dimensiones
print(f"¿Es size de matriz igual a 2×3? {matriz.size == 2*3}")
print(f"¿Es size de cubo igual a 2×2×2? {cubo.size == 2*2*2}")











import numpy as np

# Creamos arrays con diferentes tipos de datos
enteros = np.array([1, 2, 3, 4])
decimales = np.array([1.0, 2.5, 3.7, 4.2])
complejos = np.array([1+2j, 3-4j, 5+6j])
booleanos = np.array([True, False, True])

# Examinamos sus tipos de datos
print(f"Tipo de datos de enteros: {enteros.dtype}")
print(f"Tipo de datos de decimales: {decimales.dtype}")
print(f"Tipo de datos de complejos: {complejos.dtype}")
print(f"Tipo de datos de booleanos: {booleanos.dtype}")












# Especificamos tipos de datos al crear arrays
enteros_16 = np.array([1, 2, 3, 4], dtype=np.int16)
decimales_32 = np.array([1.0, 2.5, 3.7, 4.2], dtype=np.float32)
enteros_sin_signo = np.array([10, 20, 30], dtype=np.uint8)

print(f"Enteros de 16 bits: {enteros_16.dtype}")
print(f"Decimales de 32 bits: {decimales_32.dtype}")
print(f"Enteros sin signo de 8 bits: {enteros_sin_signo.dtype}")










import numpy as np

# Creamos arrays con diferentes tipos de datos
int8_array = np.array([1, 2, 3], dtype=np.int8)
int16_array = np.array([1, 2, 3], dtype=np.int16)
int32_array = np.array([1, 2, 3], dtype=np.int32)
int64_array = np.array([1, 2, 3], dtype=np.int64)
float32_array = np.array([1.0, 2.0, 3.0], dtype=np.float32)
float64_array = np.array([1.0, 2.0, 3.0], dtype=np.float64)

# Mostramos el tamaño en bytes de cada elemento
print(f"Tamaño de int8: {int8_array.itemsize} byte")
print(f"Tamaño de int16: {int16_array.itemsize} bytes")
print(f"Tamaño de int32: {int32_array.itemsize} bytes")
print(f"Tamaño de int64: {int64_array.itemsize} bytes")
print(f"Tamaño de float32: {float32_array.itemsize} bytes")
print(f"Tamaño de float64: {float64_array.itemsize} bytes")












import numpy as np

# Creamos arrays con diferentes formas y tipos
array_1 = np.ones((10, 10), dtype=np.float64)
array_2 = np.ones((10, 10), dtype=np.float32)
array_3 = np.ones((5, 5), dtype=np.complex128)

# Calculamos el consumo de memoria
print(f"Array 1 (10×10 float64):")
print(f"  Elementos: {array_1.size}")
print(f"  Bytes por elemento: {array_1.itemsize}")
print(f"  Total bytes: {array_1.nbytes}")

print(f"\nArray 2 (10×10 float32):")
print(f"  Elementos: {array_2.size}")
print(f"  Bytes por elemento: {array_2.itemsize}")
print(f"  Total bytes: {array_2.nbytes}")

print(f"\nArray 3 (5×5 complex128):")
print(f"  Elementos: {array_3.size}")
print(f"  Bytes por elemento: {array_3.itemsize}")
print(f"  Total bytes: {array_3.nbytes}")

# Verificamos que nbytes = size × itemsize
print(f"\n¿Es nbytes = size × itemsize para array_1? {array_1.nbytes == array_1.size * array_1.itemsize}")



# Array 1 (10×10 float64):
#   Elementos: 100
#   Bytes por elemento: 8
#   Total bytes: 800

# Array 2 (10×10 float32):
#   Elementos: 100
#   Bytes por elemento: 4
#   Total bytes: 400

# Array 3 (5×5 complex128):
#   Elementos: 25
#   Bytes por elemento: 16
#   Total bytes: 400

# ¿Es nbytes = size × itemsize para array_1? True













import numpy as np

# Creamos un array de float64
original = np.array([1.5, 2.7, 3.9, 4.2], dtype=np.float64)

# Convertimos a diferentes tipos
como_float32 = original.astype(np.float32)
como_int32 = original.astype(np.int32)
como_bool = original.astype(np.bool_)

# Comparamos tipos y consumo de memoria
print(f"Original (float64):")
print(f"  Valores: {original}")
print(f"  Tipo: {original.dtype}")
print(f"  Bytes totales: {original.nbytes}")

print(f"\nConvertido a float32:")
print(f"  Valores: {como_float32}")
print(f"  Tipo: {como_float32.dtype}")
print(f"  Bytes totales: {como_float32.nbytes}")

print(f"\nConvertido a int32:")
print(f"  Valores: {como_int32}")  # Nota la pérdida de decimales
print(f"  Tipo: {como_int32.dtype}")
print(f"  Bytes totales: {como_int32.nbytes}")

print(f"\nConvertido a bool:")
print(f"  Valores: {como_bool}")  # Todos los valores distintos de cero son True
print(f"  Tipo: {como_bool.dtype}")
print(f"  Bytes totales: {como_bool.nbytes}")


# Original (float64):
#   Valores: [1.5 2.7 3.9 4.2]
#   Tipo: float64
#   Bytes totales: 32

# Convertido a float32:
#   Valores: [1.5 2.7 3.9 4.2]
#   Tipo: float32
#   Bytes totales: 16

# Convertido a int32:
#   Valores: [1 2 3 4]
#   Tipo: int32
#   Bytes totales: 16

# Convertido a bool:
#   Valores: [ True  True  True  True]
#   Tipo: bool
#   Bytes totales: 4













import numpy as np

arr = np.arange(24)

# NumPy calcula automáticamente el valor de la dimensión con -1
matriz_4xN = arr.reshape(4, -1)  # NumPy deduce que N debe ser 6
matriz_Nx6 = arr.reshape(-1, 6)  # NumPy deduce que N debe ser 4
tensor_2x3xN = arr.reshape(2, 3, -1)  # NumPy deduce que N debe ser 4

print(f"Matriz 4×N: {matriz_4xN.shape}")
print(f"Matriz N×6: {matriz_Nx6.shape}")
print(f"Tensor 2×3×N: {tensor_2x3xN.shape}")



# Matriz 4×N: (4, 6)
# Matriz N×6: (4, 6)
# Tensor 2×3×N: (2, 3, 4)









import numpy as np

# Creamos una matriz 2D
matriz = np.array([[1, 2, 3], 
                   [4, 5, 6]])
print(f"Matriz original:\n{matriz}")
print(f"Forma original: {matriz.shape}")

# Transponemos la matriz
transpuesta = matriz.T
print(f"\nMatriz transpuesta:\n{transpuesta}")
print(f"Forma transpuesta: {transpuesta.shape}")


# Matriz original:
# [[1 2 3]
#  [4 5 6]]
# Forma original: (2, 3)

# Matriz transpuesta:
# [[1 4]
#  [2 5]
#  [3 6]]
# Forma transpuesta: (3, 2)











import numpy as np

# Creamos un array 3D (2×3×4)
arr = np.arange(24).reshape(2, 3, 4)
print(f"Array original shape: {arr.shape}")

# Intercambiamos diferentes pares de ejes
swap_0_1 = arr.swapaxes(0, 1)
swap_0_2 = arr.swapaxes(0, 2)
swap_1_2 = arr.swapaxes(1, 2)

print(f"Después de swapaxes(0, 1): {swap_0_1.shape}")
print(f"Después de swapaxes(0, 2): {swap_0_2.shape}")
print(f"Después de swapaxes(1, 2): {swap_1_2.shape}")

# Array original shape: (2, 3, 4)
# Después de swapaxes(0, 1): (3, 2, 4)
# Después de swapaxes(0, 2): (4, 3, 2)
# Después de swapaxes(1, 2): (2, 4, 3)















