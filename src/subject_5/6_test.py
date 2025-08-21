# Implementa un sistema básico de biblioteca utilizando composición. Crea una clase Libro con atributos para título, autor y año de publicación. Luego, crea una clase Biblioteca que contenga una colección de libros (relación "tiene un"). La clase Biblioteca debe incluir métodos para:

# Agregar un nuevo libro a la colección
# Buscar libros por título (devolviendo todos los que contengan la cadena de búsqueda)
# Contar cuántos libros hay de un autor específico
# No utilices herencia para resolver este ejercicio, solo composición. Asegúrate de que la clase Biblioteca delegue apropiadamente en los objetos Libro que contiene.

class Libro:

	def __init__(self, titulo, autor, ano):
		self.titulo = titulo
		self.autor = autor
		self.ano = ano

	def __str__(self):
		return f"{self.titulo} por {self.autor}, publicado en {self.ano}"

class Biblioteca:

	def __init__(self):
		self.libros = []

	def agregar_libro(self, libro):
		self.libros.append(libro)

	def buscar_libro_por_titulo(self, titulo):
		return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

	def contar_libros_por_autor(self, autor):
		return sum(1 for libro in self.libros if libro.autor.lower() == autor.lower())

libro1 = Libro("1984", "George Orwell", 1949)
libro2 = Libro("Animal Farm", "George Orwell", 1945)

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

[print(libro) for libro in biblioteca.buscar_libro_por_titulo("1984")]
print(biblioteca.contar_libros_por_autor("George Orwell"))