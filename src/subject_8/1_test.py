# Crea un histograma utilizando Matplotlib para visualizar la distribución de un conjunto de datos generado aleatoriamente. Debes seguir las siguientes especificaciones:

# 1.- Generación de datos:

# Usa numpy para crear un conjunto de 1500 datos con distribución normal (media=5, desviación estándar=2).
# 2.- Configuración del histograma:

# Utiliza plt.hist() para crear el histograma.
# Establece el número de intervalos (bins) en 40.
# Configura el color de las barras a verde con una transparencia (alpha) de 0.5.
# Añade bordes rojos a las barras para mejorar la claridad visual.
# 3.- Añadir información al gráfico:

# Incluye un título descriptivo, y etiquetas para los ejes x e y.

import numpy as np
import matplotlib.pyplot as plt

datos = np.random.normal(5, 2, 1500)

# Crear el histograma
plt.hist(datos, bins=40, color='green', alpha=0.5, edgecolor='red')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma básico')

# Mostrar el gráfico
plt.show()
