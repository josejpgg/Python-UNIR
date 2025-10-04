# Crea un gráfico de dispersión multivariante utilizando Matplotlib para visualizar la relación entre cuatro variables. Genera un conjunto de datos aleatorios para las variables X, Y, color y tamaño. El gráfico debe seguir las siguientes especificaciones:

# 1.- Generación de datos:

# Usa numpy para generar 200 puntos de datos para las variables X e Y con valores aleatorios entre 0 y 10.
# La tercera variable debe mapearse a colores utilizando valores aleatorios entre 0 y 100.
# La cuarta variable debe ser utilizada para el tamaño de los puntos, con valores aleatorios multiplicados por 200 para que los tamaños sean visibles.
# 2.- Configuración del gráfico de dispersión:

# Usa plt.scatter() para crear el gráfico de dispersión.
# Configura el color de los puntos mapeado a la tercera variable utilizando la paleta de colores plasma.
# Ajusta el tamaño de los puntos mapeado a la cuarta variable y establece una transparencia (alpha) de 0.6 para mejorar la visibilidad.
# 3.- Etiquetas y título:

# Añade un título descriptivo al gráfico, y etiquetas para los ejes X e Y.
# 4.- Barra de colores:

# Añade una barra de colores que represente la escala de la tercera variable.
# 5.- Visualización:

# Muestra el gráfico.

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, 200)
y = np.random.uniform(0, 10, 200)
color = np.random.uniform(0, 100, 200)
size = np.random.uniform(0,100, 200) * 200

plt.scatter(x, y, c=color, s=size, alpha=0.6, cmap='plasma')
plt.title('Gráfico de dispersión multivariante')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.colorbar(label='Valor de Color')
plt.show()
