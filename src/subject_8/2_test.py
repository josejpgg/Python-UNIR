# 1.- Generación de los datos:

# Crea dos conjuntos de datos con numpy. El primer conjunto x contendrá 100 valores aleatorios entre 0 y 50, y el segundo conjunto y tendrá una relación lineal con x (por ejemplo, y = 2.5 * x + ruido, donde el ruido es una pequeña variación aleatoria para simular datos reales).

# Utiliza numpy.polyfit para calcular la línea de regresión lineal que mejor se ajuste a los datos.
# 3.- Configuración del gráfico de dispersión:

# Usa plt.scatter() para crear el gráfico de dispersión.
# Configura el color de los puntos a púrpura (purple) y ajusta el tamaño de los puntos a 50 para mejorar la visualización.
# Añade una línea de regresión con plt.plot() en color verde (green).
# Incluye una cuadrícula para mejorar la interpretación del gráfico.
# 4.- Etiquetas y título:

# Añade un título descriptivo para el gráfico, además de etiquetas para los ejes X e Y.
# 5.- Visualización:

# Muestra el gráfico utilizando plt.show().

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 50, 100)
ruido = np.random.normal(0, 10, 100)
y = 2.5 * x + ruido

#coeficientes de la recta
m, b = np.polyfit(x, y, 1)

plt.scatter(x, y, color='purple', alpha=0.5)
#linea de regresión
plt.plot(x, m*x + b, color='green')
plt.grid(True)
plt.title('Gráfico de dispersión con línea de regresión')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.show()
