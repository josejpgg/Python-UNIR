# Cargar el conjunto de datos: Utiliza el conjunto de datos penguins de Seaborn. Este conjunto de datos contiene información sobre características físicas de pingüinos, como el largo de su aleta, su peso y su especie.
# Crear una cuadrícula de facetas:
# Usa FacetGrid para crear una cuadrícula que segmente los datos por la especie (species) en las columnas y por el sexo (sex) en las filas.
# Dentro de cada faceta, representa la relación entre el largo de la aleta (flipper_length_mm) y el peso corporal (body_mass_g) utilizando un gráfico de dispersión (scatterplot).
# Personalización:
# Añade una variable adicional hue basada en la isla de origen (island) para diferenciar los datos dentro de cada faceta.
# Asegúrate de incluir una leyenda para identificar los subgrupos de hue.
# Ajusta el tamaño de las facetas y el espacio entre ellas para asegurar una visualización clara y legible.
# Añade títulos y etiquetas a los ejes para mejorar la interpretación de los gráficos.
# Ajusta los límites del eje x y del eje y para un rango consistente en todas las facetas.
# Mostrar la visualización: Configura y muestra la visualización completa.

import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("penguins")

g = sns.FacetGrid(data, col="species", row='sex', hue='island')
g.map(sns.scatterplot, "flipper_length_mm", "body_mass_g")
# Ajusta el tamaño de las facetas y el espacio entre ellas para asegurar una visualización clara y legible
g.fig.subplots_adjust(hspace=0.2, wspace=0.2)
# Añade títulos y etiquetas a los ejes para mejorar la interpretación de los gráficos.
g.set_axis_labels("Flipper Length (mm)", "Body Mass (g)")
g.add_legend()
g.set_titles(col_template="{col_name}", row_template="{row_name}")
g.set(xlim=(100, 250), ylim=(2000, 6500))
plt.show()
