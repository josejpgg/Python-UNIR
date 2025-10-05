import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3], [4, 5, 6], color='red')  # Usando nombre de color
plt.plot([1, 2, 3], [6, 5, 4], color='#FF5733')  # Usando código hexadecimal
plt.show()


plt.plot([1, 2, 3], [4, 5, 6], color=(0.1, 0.2, 0.5))  # RGB
plt.plot([1, 2, 3], [6, 5, 4], color=(0.1, 0.2, 0.5, 0.3))  # RGBA
plt.show()













from matplotlib.colors import LinearSegmentedColormap

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generación de datos aleatorios
data = rng.random((10, 10))

custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', ['red', 'blue', 'green'])
plt.imshow(data, cmap=custom_cmap)
plt.colorbar()
plt.show()
