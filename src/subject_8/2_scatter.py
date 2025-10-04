import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear un gráfico de dispersión
plt.scatter(x, y, color='blue')
plt.title('Gráfico de dispersión de ejemplo')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.show()














import matplotlib.pyplot as plt

# Datos de ejemplo
x = [10, 20, 30, 40, 50]
y = [15, 25, 35, 45, 55]

# Crear un gráfico de dispersión
plt.scatter(x, y, c='green', marker='o')
plt.title('Gráfico de dispersión básico')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.grid(True)
plt.show()


















import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos de ejemplo
x = rng.random(50)
y = rng.random(50)
tamaño = rng.random(50) * 1000
colores = rng.random(50)

# Crear un gráfico de dispersión con tamaño y color
plt.scatter(x, y, s=tamaño, c=colores, alpha=0.5, cmap='viridis')
plt.colorbar()  # Añadir barra de color
plt.title('Gráfico de dispersión con tamaño y color')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.show()
















# Datos de ejemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Calcular coeficientes de la línea de regresión
m, b = np.polyfit(x, y, 1)

# Crear gráfico de dispersión
plt.scatter(x, y, color='red')
plt.plot(x, m*x + b, color='blue')  # Añadir línea de regresión
plt.title('Gráfico de dispersión con línea de regresión')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.show()




















import matplotlib.pyplot as plt

# Datos de ejemplo
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Crear una gráfica de línea (unir puntos)
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Gráfica de línea básica')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.grid(True)
plt.show()
















# Datos de ejemplo
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]

# Crear una gráfica de línea con dos variables
plt.plot(x, y1, label='Cuadrados', marker='o')
plt.plot(x, y2, label='Lineal', marker='s')
plt.title('Comparación de dos variables')
plt.xlabel('Variable X')
plt.ylabel('Valor')
plt.legend()
plt.show()

















import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos de ejemplo
data = rng.random((10, 10))

# Crear un diagrama de calor
plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Intensidad')
plt.title('Diagrama de calor básico')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()
















import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos de ejemplo
data = rng.random((10, 10))

# Crear un diagrama de calor con personalización
plt.imshow(data, cmap='hot', interpolation='bicubic')
plt.colorbar(label='Intensidad')
plt.title('Diagrama de calor personalizado')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Personalizar etiquetas de los ejes
plt.xticks(ticks=np.arange(10), labels=[f'X{i}' for i in range(10)])
plt.yticks(ticks=np.arange(10), labels=[f'Y{i}' for i in range(10)])

# Mostrar gráfico
plt.show()




















import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D']
valores1 = [3, 2, 5, 7]
valores2 = [4, 6, 2, 5]

# Crear gráfico de barras apiladas
plt.bar(categorias, valores1, label='Conjunto 1')
plt.bar(categorias, valores2, bottom=valores1, label='Conjunto 2')
plt.title('Gráfico de barras apiladas')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.legend()
plt.show()




















