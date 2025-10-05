# Las gráficas univariantes son herramientas visuales que permiten analizar la distribución de una variable en un conjunto de datos. Su objetivo principal es resumir y visualizar las características fundamentales de una sola variable, como su tendencia central, dispersión, asimetría y posibles valores atípicos. Estas gráficas son esenciales para entender la estructura de los datos antes de aplicar modelos estadísticos más complejos.




import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
df = sns.load_dataset('tips')

# Crear un histograma de la variable 'total_bill'
sns.histplot(data=df, x='total_bill')

plt.xlabel('Total de la factura')
plt.ylabel('Frecuencia')
plt.title('Distribución del total de las facturas')
plt.show()













# Histograma con diferenciación por sexo
sns.histplot(data=df, x='total_bill', hue='sex', multiple='stack')









# Colocar las barras de categorías lado a lado
sns.histplot(data=df, x='total_bill', hue='sex', multiple='dodge')












# Personalizar color y transparencia
sns.histplot(data=df, x='total_bill', color='teal', alpha=0.6)











# Configurar el estilo del gráfico
sns.set_style('whitegrid')

sns.histplot(data=df, x='total_bill', kde=True, color='purple')
plt.xlabel('Total de la factura')
plt.ylabel('Frecuencia')
plt.title('Histograma del total de las facturas con KDE')
plt.show()



















import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos 'fmri'
df = sns.load_dataset('fmri')

# Crear una gráfica de línea básica
sns.lineplot(data=df, x='timepoint', y='signal')

plt.xlabel('Punto en el tiempo')
plt.ylabel('Señal')
plt.title('Evolución de la señal cerebral a lo largo del tiempo')
plt.show()
















# Gráfica de línea diferenciada por región
sns.lineplot(data=df, x='timepoint', y='signal', hue='region')

plt.xlabel('Punto en el tiempo')
plt.ylabel('Señal')
plt.title('Señal cerebral por región a lo largo del tiempo')
plt.legend(title='Región')
plt.show()
