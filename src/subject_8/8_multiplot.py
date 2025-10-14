import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
diamonds = sns.load_dataset("diamonds")

# Crear una cuadrícula de plots segmentada por corte y color de diamante
g = sns.FacetGrid(diamonds, col="cut", row="color", margin_titles=True)
g.map(sns.histplot, "price")
plt.show()












# Cargar datos sobre ejercicios físicos
exercise = sns.load_dataset("exercise")

# Crear una cuadrícula de plots para visualizar la relación entre pulso y tiempo, segmentada por tipo de ejercicio
g = sns.FacetGrid(exercise, col="kind")
g.map(sns.scatterplot, "time", "pulse")
plt.show()














