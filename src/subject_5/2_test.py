# Crea una clase llamada Libro con los siguientes requisitos:

# El constructor debe inicializar tres atributos de instancia: titulo, autor y paginas.

# Implementa un método llamado describir que devuelva un string con el formato: "[Titulo] escrito por [Autor] - [Paginas] páginas".

# Implementa un método llamado es_largo que devuelva True si el libro tiene más de 300 páginas, y False en caso contrario.

# Implementa un método llamado resumir que reciba un parámetro longitud y devuelva un string con el formato: "[Titulo] - Resumen de [longitud] caracteres". Si no se proporciona el parámetro longitud, debe usar un valor predeterminado de 50.

# Prueba tu clase creando al menos dos instancias diferentes de Libro y llamando a todos sus métodos.

class Libro:
	__slots__ = ('titulo', 'autor', 'paginas')

	def __init__(self, titulo:str,autor:str,paginas:int):
		self.titulo = titulo
		self.autor = autor
		self.paginas = paginas

	def describir(self) -> str:
		return f"{self.titulo} escrito por {self.autor} - {self.paginas} páginas"

	def es_largo(self) -> bool:
		return self.paginas > 300

	def resumir(self, longitud:int = 50) -> str:
		return f"{self.titulo} - Resumen de {longitud} caracteres"


libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro2 = Libro("El túnel", "Ernesto Sabato", 216)

mensaje = """
Libro: {0}
Autor: {1}
Páginas: {2}
¿Es largo?: {3}
Resumen: {3}
"""

print(mensaje.format(
	libro1.titulo,
	libro1.autor,
	libro1.paginas,
	"SI" if libro1.es_largo() else "NO",
	libro1.resumir()
))

print(mensaje.format(
	libro2.titulo,
	libro2.autor,
	libro2.paginas,
	"SI" if libro2.es_largo() else "NO",
	libro2.resumir()
))
