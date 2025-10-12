import seaborn as sns
import matplotlib.pyplot as plt

datos = sns.load_dataset('tips')

sns.scatterplot(data=datos, x='total_bill', y='tip')
plt.show()










sns.scatterplot(data=datos, x='petal_length', y='petal_width', hue='species')
plt.xlabel('Longitud del pétalo')
plt.ylabel('Ancho del pétalo')
plt.title('Relación entre longitud y ancho del pétalo por especie')
plt.show()












import seaborn as sns
import matplotlib.pyplot as plt

datos = sns.load_dataset('fmri')


sns.lineplot(data=datos, x='timepoint', y='signal')
plt.show()


# hue is by field
sns.lineplot(data=datos, x='timepoint', y='signal', hue='event')
plt.show()





# Si deseamos distinguir aún más las líneas, podemos utilizar el parámetro style para variar el estilo según otra variable categórica
sns.lineplot(data=datos, x='timepoint', y='signal', hue='event', style='region')
plt.show()



















sns.catplot(data=datos, x='day', y='tip', hue='sex', kind='bar', errorbar=None)
plt.ylabel('Propina promedio')
plt.title('Propina promedio por día y sexo')
plt.show()

















# Gráficos de Barras Apiladas


tabla_pivot = datos.pivot_table(values='tip', index='day', columns='sex', aggfunc='sum', observed=False)

tabla_pivot.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
plt.ylabel('Propina total')
plt.title('Propina total por día y sexo (apilado)')
plt.legend(title='Sexo')
plt.xticks(rotation=0)
plt.show()




# Añadiendo etiquetas de datos

ax = tabla_pivot.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
plt.ylabel('Propina total')
plt.title('Propina total por día y sexo (apilado)')
plt.legend(title='Sexo')
plt.xticks(rotation=0)

for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', label_type='center')

plt.show()




# Gráficos de Barras Apiladas con porcentajes

tabla_porcentajes = tabla_pivot.div(tabla_pivot.sum(axis=1), axis=0)

ax = tabla_porcentajes.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'])
plt.ylabel('Proporción de propinas')
plt.title('Proporción de propinas por día y sexo')
plt.legend(title='Sexo')
plt.xticks(rotation=0)

for container in ax.containers:
    labels = [f'{v.get_height()*100:.1f}%' for v in container]
    ax.bar_label(container, labels=labels, label_type='center')

plt.show()





