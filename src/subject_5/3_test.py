# Crea una clase llamada Biblioteca que gestione libros utilizando variables de clase e instancia adecuadamente.

# La clase debe tener:

# Una variable de clase total_libros inicializada en 0 que lleve la cuenta de todos los libros en el sistema.
# Una variable de clase nombre_biblioteca con el valor "Biblioteca Central".
# En el método __init__, recibe el parámetro nombre_seccion (por ejemplo "Ficción", "Historia", etc.) y crea una variable de instancia para almacenarlo.
# En el método __init__, inicializa una variable de instancia libros como una lista vacía para almacenar los libros de esa sección.
# Un método agregar_libro(self, titulo) que añada el título a la lista de libros de la sección e incremente la variable de clase total_libros.
# Un método obtener_informe(self) que devuelva un string con el formato: "Sección [nombre_seccion] de [nombre_biblioteca]: [cantidad] libros".
# Finalmente, crea dos instancias de la clase con diferentes secciones, agrega algunos libros a cada una y muestra sus informes para verificar que la variable de clase se comparte correctamente.


class Biblioteca:
	total_libros = 0
	nombre_biblioteca = "Biblioteca Central"

	@classmethod
	def incrementar_libros(cls):
		cls.total_libros += 1

	@classmethod
	def obtener_nombre_biblioteca(cls) -> str:
		return cls.nombre_biblioteca

	def __init__(self, nombre_seccion:str):
		self.nombre_seccion = nombre_seccion
		self.libros = []


	def __str__(self):
		return f"Sección {self.nombre_seccion} de {self.obtener_nombre_biblioteca()}: {len(self.libros)} libros"


	def agregar_libro(self, titulo:str):
		self.libros.append(titulo)
		self.incrementar_libros()


	def obtener_informe(self):
		return self.__str__()


seccion1 = Biblioteca("Ficción")
seccion1.agregar_libro("Cien años de soledad")
seccion1.agregar_libro("1984")
seccion1.agregar_libro("La Guia del autoestopiesta galactico")

seccion2 = Biblioteca("Historia")
seccion2.agregar_libro("Sapiens")
seccion2.agregar_libro("El origen de las especies")

print(f"Total de libros en la biblioteca: {Biblioteca.total_libros}")
print(seccion1.obtener_informe())
print(seccion2.obtener_informe())
