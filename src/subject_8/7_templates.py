# darkgrid: fondo gris con cuadrículas.
# whitegrid: fondo blanco con cuadrículas.
# dark: fondo gris sin cuadrículas.
# white: fondo blanco sin cuadrículas.
# ticks: similar a 'white' pero con marcas de graduación en los ejes.

import seaborn as sns

sns.set_style("whitegrid")
sns.despine()


# También es posible combinar los temas con ajustes de contexto a través de sns.set_context(), que modifica el tamaño de los elementos del gráfico según el entorno deseado (e.g., 'paper', 'notebook', 'talk', 'poster'):
sns.set_context("talk")



import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
sns.set_context("notebook")

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [5, 7, 9, 6, 8]

# Crear gráfico
sns.lineplot(x=x, y=y)

# Mostrar gráfico
plt.title("Gráfico con estilo whitegrid")
plt.show()










# Colores y personalización de colores en seaborn

# Para crear una paleta personalizada, se puede especificar una lista de colores:
custom_palette = sns.color_palette(["#2ecc71", "#e74c3c", "#3498db"])
sns.set_palette(custom_palette)

# Para mejorar la accesibilidad y crear gráficos aptos para personas con daltonismo, se recomienda utilizar la paleta "colorblind":
sns.set_palette("colorblind")



