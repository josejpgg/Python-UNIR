import numpy as np
import matplotlib.pyplot as plt

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generación de datos aleatorios
data = rng.random(100)

# Creación de una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Configuración de los límites del eje x basados en los datos
ax.set_xlim(np.min(data), np.max(data))


ax.margins(x=0.1, y=0.2)
ax.set_xlim(0, 10, emit=False)
ax.set_xscale('log')


plt.show()
