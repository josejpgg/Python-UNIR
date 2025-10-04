import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generación de datos aleatorios
x = rng.random(100)
y = rng.random(100)
colors = rng.random(100)
sizes = 1000 * rng.random(100)

# Creación del gráfico de dispersión
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Gráfico de dispersión multivariante')
plt.colorbar()  # Agrega una barra de color para interpretar los valores
plt.show()






















import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Creación de un DataFrame de ejemplo
data = pd.DataFrame({
    'Variable A': rng.random(100),
    'Variable B': rng.random(100),
    'Variable C': rng.random(100),
    'Variable D': rng.random(100)
})

# Creación del pairplot
sns.pairplot(data)
plt.show()















# Añadir una variable categórica
data['Categoría'] = rng.choice(['Grupo 1', 'Grupo 2'], size=100)

# Creación del pairplot con hue
sns.pairplot(data, hue='Categoría')
plt.show()























import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generación de datos aleatorios y cálculo de la matriz de correlación
data = rng.random((10, 12))
correlation_matrix = np.corrcoef(data, rowvar=False)

# Creación del heatmap
plt.figure(figsize=(8, 6))
heatmap = plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(heatmap, label='Coeficiente de correlación')
plt.title('Diagrama de calor de la matriz de correlación')
plt.xlabel('Variables')
plt.ylabel('Variables')
plt.xticks(ticks=np.arange(12), labels=[f'Var{i+1}' for i in range(12)], rotation=45)
plt.yticks(ticks=np.arange(12), labels=[f'Var{i+1}' for i in range(12)])
plt.show()



