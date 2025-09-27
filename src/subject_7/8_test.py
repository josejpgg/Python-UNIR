# Crea un DataFrame de ventas con las siguientes columnas: 'producto', 'categoria', 'precio' y 'stock'. Incluye al menos 8 productos de diferentes categorías (por ejemplo: 'Electrónica', 'Ropa', 'Hogar'). Luego, realiza las siguientes operaciones de filtrado:

# Filtra los productos que pertenecen a la categoría 'Electrónica'.
# Encuentra los productos con precio mayor a 50 y stock menor a 20.
# Selecciona los productos que contengan la letra 'a' en su nombre.
# Utiliza el método query() para encontrar productos de la categoría 'Hogar' con precio menor a 30.
# Muestra el resultado de cada filtrado por separado.

import pandas as pd

ventas = pd.DataFrame(
{
#8 producto de diferentes categorias
    'producto':['Monitor', 'Sudadera', 'Sillon', 'Call of Duty', 'Licuadora', 'Smartphone', 'Camiseta', 'Cafetera'],
    'categoria':['Electrónica', 'Moda', 'Hogar', 'Juegos', 'Cocina', 'Electrónica', 'Moda', 'Cocina'],
    'precio':[300, 50, 700, 60, 80, 1000, 20, 150],
    'stock':[20, 100, 5, 50, 80, 10, 200, 15]
})

print(f"Lista de productos en la categoría Electrónica:\n{
ventas[ventas['categoria']=='Electrónica']['producto'].tolist()
}")

print(f"Productos con precio mayor a 50 y stock menor a 20:\n{
ventas[(ventas['precio']>50) & (ventas['stock'] < 20)]['producto'].tolist()
}")

print(f"Productos son letra 'a' en su nombre:\n{
ventas[ventas['producto'].str.contains('a')]['producto'].tolist()
}")

print("Productos de la categoria Hogar y precio menor a 30 con query():")
print(ventas.query("categoria == 'Hogar' and precio < 30")['producto'].tolist())


