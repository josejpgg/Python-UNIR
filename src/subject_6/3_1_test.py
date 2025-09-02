# Crea una matriz de multiplicación de 5x5 utilizando bucles anidados. La matriz debe contener el resultado de multiplicar el número de fila por el número de columna. Por ejemplo, en la posición [2][3] debe estar el valor 6 (2×3). Después de crear la matriz, muestra su contenido en la consola con un formato de tabla, donde cada fila aparezca en una línea diferente y los números estén separados por espacios.

matriz = [[i * j for j in range (0, 5)] for i in range(0, 5)]

for fila in matriz:
	print(" ".join([str(num) for num in fila]))






