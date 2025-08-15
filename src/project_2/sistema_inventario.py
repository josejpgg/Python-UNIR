# Implementación de la clase Producto
# Correcta definición de la clase Producto con sus atributos (nombre, precio, cantidad) y métodos (actualizar_precio, actualizar_cantidad, calcular_valor_total, __str__). Incluye validaciones básicas para los datos.
# Peso: 30%

class Producto:

	def __init__(self, nombre:str, precio:float, cantidad:int):
		if not nombre:
			raise ValueError("El nombre del producto no puede estar vacio.")
		self.nombre = nombre
		if precio < 0:
			raise ValueError("El precio no puede ser negativo.")
		self.precio = precio
		if cantidad < 0:
			raise ValueError("La cantidad no puede ser negativa.")
		self.cantidad = cantidad

	def actualizar_precio(self, nuevo_precio:float):
		if nuevo_precio < 0:
			raise ValueError("El precio no puede ser negativo.")
		self.precio = nuevo_precio

	def actualizar_cantidad(self, nueva_cantidad:int):
		if nueva_cantidad < 0:
			raise ValueError("La cantidad no puede ser negativa.")
		self.cantidad = nueva_cantidad

	def calcular_valor_total(self):
		return self.precio * self.cantidad

	def __str__(self):
		return f"Producto(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"


# Implementación de la clase Inventario
# Correcta implementación de la clase Inventario con métodos para agregar productos, buscar por nombre, calcular el valor total del inventario y listar todos los productos.
# Peso: 30%

class Inventario:
	def __init__(self):
		self.productos = []

	def agregar_producto(self, producto: Producto):
		self.productos.append(producto)

	def buscar_producto(self, nombre:str):
		return [producto for producto in self.productos if producto.nombre == nombre]

	def calcular_valor_total(self):
		return sum(producto.precio * producto.cantidad for producto in self.productos)

	def listar_productos(self):
		return [producto for producto in self.productos]

# Manejo de excepciones
# Implementación de bloques try-except para manejar errores como valores negativos, tipos de datos incorrectos o productos no encontrados.
# Peso: 20%

# Interfaz de usuario y funcionalidad
# Desarrollo de un menú interactivo que permita al usuario realizar todas las operaciones solicitadas (agregar, buscar, listar productos y calcular valor total).
# Peso: 20%

def menu_principal(inventario: Inventario):
	while True:
		print("\n\tSistema de Inventario")
		print("1. Agregar producto")
		print("2. Buscar producto")
		print("3. Listar productos")
		print("4. Calcular valor total del inventario")
		print("0. Salir")
		opcion = input("Seleccione una opción: ")
		if opcion == '1':
			try:
				nombre = input("Ingrese el nombre del producto: ")
				precio = float(input("Ingrese el precio del producto: "))
				cantidad = int(input("Ingrese la cantidad del producto: "))
				producto = Producto(nombre, precio, cantidad)
				inventario.agregar_producto(producto)
				print(f"Producto agregado exitosamente.\n{producto.__str__()}")
			except ValueError as e:
				print(f"Error al agregar producto: {e}")
		elif opcion == '2':
			nombre = input("Ingrese el nombre del producto a buscar: ")
			resultados = inventario.buscar_producto(nombre)
			if resultados:
				for prod in resultados:
					print(prod.__str__())
			else:
				print(f"No se encontraron productos con el nombre '{nombre}'.")
		elif opcion == '3':
			productos = inventario.listar_productos()
			if productos:
				for prod in productos:
					print(prod.__str__())
			else:
				print("No hay productos en el inventario.")
		elif opcion == '4':
			valor_total = inventario.calcular_valor_total()
			print(f"El valor total del inventario es: {valor_total} unidades monetarias.")
		elif opcion == '0':
			print("Saliendo del sistema de inventario.")
			break
		else:
			print("Opción no válida. Intente nuevamente.")
		input("\nPresione Enter para continuar...")

if __name__ == "__main__":
	inventario = Inventario()
	menu_principal(inventario)
