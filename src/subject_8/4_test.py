
import seaborn as sns
import matplotlib.pyplot as plt


tip = sns.load_dataset('tips')
sns.set_style('darkgrid')
sns.histplot(data=tip, x='tip', kde=True, color='blue', bins=40, stat='density')
plt.xlabel('Tip')
plt.ylabel('Densidad')
plt.title('Histograma de propinas con KDE')
plt.show()

