import numpy as np

# Creamos dos arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Operaciones básicas
suma = a + b          # [6, 8, 10, 12]
resta = a - b         # [-4, -4, -4, -4]
multiplicacion = a * b  # [5, 12, 21, 32]
division = a / b      # [0.2, 0.33, 0.43, 0.5]
potencia = a ** 2     # [1, 4, 9, 16]








# Array y escalar
c = np.array([10, 20, 30, 40])
escalar = 5

suma_escalar = c + escalar      # [15, 25, 35, 45]
mult_escalar = c * escalar      # [50, 100, 150, 200]
div_escalar = c / escalar       # [2., 4., 6., 8.]










# Broadcasting con arrays de diferentes dimensiones
a = np.array([1, 2, 3])  # Shape: (3,)
b = np.array([[1], [2], [3]])  # Shape: (3, 1)

# NumPy hace broadcasting automáticamente
resultado = a + b
print(resultado)
# Resultado:
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]












# Array 1D y 2D
vector = np.array([1, 2, 3])  # Shape: (3,)
matriz = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)

# Broadcasting del vector a través de cada fila de la matriz
resultado = matriz + vector
print(resultado)
# Resultado:
# [[2 4 6]
#  [5 7 9]]










# Datos de ejemplo (cada fila es una muestra, cada columna una característica)
datos = np.array([
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40],
    [25, 35, 45]
])

# Calculamos media y desviación estándar por columna
medias = np.mean(datos, axis=0)  # [17.5, 27.5, 37.5]
desviaciones = np.std(datos, axis=0)  # [6.45, 6.45, 6.45]

# Normalizamos los datos usando broadcasting
datos_normalizados = (datos - medias) / desviaciones
print(datos_normalizados)
# Resultado aproximado:
# [[-1.16, -1.16, -1.16]
#  [-0.39, -0.39, -0.39]
#  [ 0.39,  0.39,  0.39]
#  [ 1.16,  1.16,  1.16]]











# Anatomía de una ufunc

import numpy as np

# Creamos un array de ejemplo
arr = np.array([0, np.pi/4, np.pi/2, np.pi])

# Aplicamos una ufunc trigonométrica
senos = np.sin(arr)
print(senos)  # [0.0, 0.7071067811865475, 1.0, 0.0]














# Creamos arrays de ejemplo
a = np.array([-2, -1, 0, 1, 2])
b = np.array([1, 2, 3, 4, 5])

# Valor absoluto
abs_a = np.abs(a)  # [2, 1, 0, 1, 2]

# Raíz cuadrada (valores negativos resultan en NaN)
sqrt_b = np.sqrt(b)  # [1.0, 1.414, 1.732, 2.0, 2.236]

# Redondeo
c = np.array([1.49, 1.51, 2.49, 2.51])
redondeado = np.round(c)  # [1.0, 2.0, 2.0, 3.0]
redondeado_abajo = np.floor(c)  # [1.0, 1.0, 2.0, 2.0]
redondeado_arriba = np.ceil(c)  # [2.0, 2.0, 3.0, 3.0]















import numpy as np
from numpy import linalg as LA  # Es común importarlo con un alias


# Vector de ejemplo
v = np.array([3, 4])

# Norma L2 (euclidiana) - la distancia desde el origen
norma_l2 = LA.norm(v)  # 5.0 (el teorema de Pitágoras: √(3² + 4²))

# Norma L1 (suma de valores absolutos)
norma_l1 = LA.norm(v, ord=1)  # 7.0 (|3| + |4|)

# Norma infinito (valor máximo absoluto)
norma_inf = LA.norm(v, ord=np.inf)  # 4.0 (max(|3|, |4|))

# Normas para matrices
A = np.array([[1, 2], [3, 4]])
norma_frobenius = LA.norm(A)  # 5.477 (raíz cuadrada de la suma de cuadrados)











