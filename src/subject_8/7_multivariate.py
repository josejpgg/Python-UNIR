import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
datos = sns.load_dataset('tips')


sns.scatterplot(data=datos, x='total_bill', y='tip')
plt.show()

# Para agregar una variable categórica como color, empleamos el parámetro hue. Por ejemplo, coloreamos los puntos según el día de la semana:
# hue nombre de campo
sns.scatterplot(data=datos, x='total_bill', y='tip', hue='day')
plt.show()


# Si queremos representar una variable numérica mediante el tamaño de los puntos, utilizamos el parámetro size. Ajustemos el tamaño según el número de comensales:
sns.scatterplot(data=datos, x='total_bill', y='tip', size='size')
plt.show()





# Es importante considerar la transparencia para mejorar la legibilidad cuando hay superposición de puntos. Podemos ajustar el parámetro alpha:
sns.scatterplot(data=datos, x='total_bill', y='tip', hue='day', size='size', alpha=0.7)
plt.show()











# Diagramas de Calor (Heatmaps) para Múltiples Variables

import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
datos = sns.load_dataset('flights')

# Reestructurar los datos en una tabla pivot
tabla_pivot = datos.pivot(index='month', columns='year', values='passengers')

# Crear el diagrama de calor
sns.heatmap(tabla_pivot)
plt.show()


# Para mejorar la interpretación del gráfico, es útil ajustar parámetros como la paleta de colores y añadir anotaciones:
# Crear el diagrama de calor con personalización
sns.heatmap(
    tabla_pivot,
    cmap='YlGnBu',
    annot=True,
    fmt='d'
)
plt.show()
