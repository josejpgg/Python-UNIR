import matplotlib.pyplot as plt


# La interfaz pyplot, inspirada en MATLAB, proporciona una forma más sencilla y directa de crear gráficos

plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico simple con pyplot')
plt.show()










# La interfaz orientada a objetos proporciona un control más detallado sobre los elementos gráficos.

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Gráfico con interfaz orientada a objetos')
plt.show()











# Gráficos de líneas: Son útiles para mostrar tendencias a lo largo del tiempo o la relación entre dos variables continuas. Se utilizan cuando se desea resaltar cambios o patrones en los datos

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Gráfico de líneas')
plt.show()




# Gráficos de barras: Ideales para comparar cantidades discretas entre diferentes categorías. Se emplean cuando se quiere visualizar diferencias en magnitud entre grupos.

import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C']
valores = [4, 7, 1]
plt.bar(categorias, valores)
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.title('Gráfico de barras')
plt.show()






# Histogramas: Se utilizan para representar la distribución de un conjunto de datos continuos, mostrando la frecuencia de ocurrencias en intervalos específicos. Son útiles para identificar patrones como la normalidad o la asimetría.

import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar los datos aleatorios utilizando el generador
datos = rng.standard_normal(1000)

# Crear el histograma
plt.hist(datos, bins=30)
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma')

# Mostrar el gráfico
plt.show()









# Diagramas de dispersión: Utilizados para mostrar la relación entre dos variables numéricas, permitiendo identificar correlaciones o patrones de agrupamiento. Son esenciales en análisis de regresión y minería de datos.

import matplotlib.pyplot as plt

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 5, 6, 7]
y = [7, 4, 3, 8, 3, 2, 4, 9, 6, 1, 8, 7, 1, 2, 6]
plt.scatter(x, y)
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Diagrama de dispersión')
plt.show()









# Gráficos de sectores (pastel): Útiles para representar proporciones de un todo, mostrando cómo se descompone un conjunto en sus partes constituyentes. Sin embargo, son menos efectivos cuando hay muchas categorías o diferencias pequeñas.

import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Gráfico de sectores')
plt.show()










# Mapas de calor: Se utilizan para visualizar matrices de datos donde el color de cada celda representa la magnitud de los valores. Son útiles en análisis de correlación y para identificar patrones o anomalías en grandes conjuntos de datos.

import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos aleatorios utilizando el generador
data = rng.random((10, 10))

# Crear el mapa de calor
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Mapa de calor')

# Mostrar el gráfico
plt.show()




















import matplotlib.pyplot as plt

# Creación de un gráfico simple
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# Guardar el gráfico en formato PNG
fig.savefig('grafico.png', dpi=300)





# inclusión de metadatos en archivos PDF

fig.savefig('grafico_con_metadatos.pdf', metadata={'Title': 'Mi Gráfico', 'Author': 'Nombre del Autor'})













