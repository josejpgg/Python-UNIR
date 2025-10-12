
# Utilizando Seaborn, crea una visualización bivariante que analice la relación entre dos variables numéricas del conjunto de datos tips. Personaliza el gráfico según los siguientes requisitos:

# Carga el conjunto de datos tips utilizando sns.load_dataset.
# Configura el estilo del gráfico a  whitegrid.
# Crea un gráfico de dispersión entre las variables total_bill y tip.
# Usa una paleta personalizada con el parámetro palette configurado como coolwarm.
# Diferencia los puntos en función del sexo con el parámetro hue='sex'.
# Ajusta el nivel de transparencia de los puntos con alpha=0.6 para mejorar la visualización en datos densos.
# Añade un título descriptivo y etiquetas claras para ambos ejes.
# Superpón una línea de regresión utilizando sns.regplot() para observar tendencias entre las variables, ocultando los puntos de dispersión con scatter=False.
# Muestra el gráfico combinando ambas visualizaciones en un solo espacio.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

datos = sns.load_dataset('tips')
sns.set_style('whitegrid')
sns.scatterplot(data=datos, x='total_bill', y='tip', 
palette='coolwarm', hue='sex', alpha=0.6)
sns.regplot(data=datos, scatter=False, x='total_bill', y='tip')
plt.title('Relación entre el total de la cuenta y la propina')
plt.xlabel('Total de la cuenta ($)')
plt.ylabel('Propina ($)')
plt.show()



