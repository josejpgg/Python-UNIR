# Utilizando Seaborn en Python, crea un script que genere un gráfico de barras (barplot) con datos ficticios. El gráfico debe cumplir los siguientes requisitos:

# Crea un DataFrame con datos ficticios:
# El DataFrame debe tener dos columnas:
# Categoría, que contiene las categorías A, B, C, D.
# Valor, que contiene los valores numéricos 10, 15, 7, 12.
# Aplica el tema predefinido whitegrid al gráfico.
# Utiliza la paleta de colores pastel para las barras.
# Crea un gráfico de barras:
# Usa la función sns.barplot() para graficar los datos del DataFrame:
# Eje x: la columna Categoría.
# Eje y: la columna Valor.
# Asigna la columna Categoría al parámetro hue para garantizar compatibilidad con futuras versiones de Seaborn.
# Establece la paleta de colores pastel mediante el argumento palette.
# Personaliza el título del gráfico:
# El título debe ser: Gráfico de barras personalizado.
# Debe tener:
# Tamaño de fuente de 16.
# Color azul.
# Negrita (bold).
# Personaliza las etiquetas de los ejes:
# Cambia la etiqueta del eje x a Categorías y la del eje y a Valores.
# Ambas etiquetas deben tener:
# Tamaño de fuente de 12.
# Color gris oscuro.
# Elimina bordes específicos del gráfico:
# Usa sns.despine() para eliminar los bordes izquierdo y derecho del gráfico.
# Muestra el gráfico resultante.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
	'Categoría': ['A', 'B', 'C', 'D'],
	'Valor': [10, 15, 7, 12]
}
)

sns.set_style("whitegrid")
sns.barplot(x='Categoría', y='Valor', data=df, hue='Categoría', palette='pastel')
plt.title("Gráfico de barras personalizado", fontsize=16, fontweight='bold', color='darkblue')
plt.xlabel("Categorías", fontsize=12, color='darkgray')
plt.ylabel("Valores", fontsize=12, color='darkgray')
sns.despine()
plt.show()
