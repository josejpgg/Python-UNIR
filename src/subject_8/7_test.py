
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
