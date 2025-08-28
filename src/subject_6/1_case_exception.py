# Excepciones base
class BibliotecaError(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass

# Excepciones relacionadas con libros
class LibroError(BibliotecaError):
    """Excepción base para errores relacionados con libros."""
    pass

class LibroNoEncontradoError(LibroError):
    """El libro solicitado no existe en la biblioteca."""
    def __init__(self, isbn=None, titulo=None):
        self.isbn = isbn
        self.titulo = titulo
        
        if isbn and titulo:
            mensaje = f"Libro con ISBN {isbn} y título '{titulo}' no encontrado"
        elif isbn:
            mensaje = f"Libro con ISBN {isbn} no encontrado"
        elif titulo:
            mensaje = f"Libro con título '{titulo}' no encontrado"
        else:
            mensaje = "Libro no encontrado"
            
        super().__init__(mensaje)

class LibroNoDisponibleError(LibroError):
    """El libro existe pero no está disponible para préstamo."""
    def __init__(self, libro, fecha_devolucion=None):
        self.libro = libro
        self.fecha_devolucion = fecha_devolucion
        
        mensaje = f"El libro '{libro}' no está disponible"
        if fecha_devolucion:
            mensaje += f". Estará disponible después de {fecha_devolucion}"
            
        super().__init__(mensaje)

# Excepciones relacionadas con usuarios
class UsuarioError(BibliotecaError):
    """Excepción base para errores relacionados con usuarios."""
    pass

class UsuarioNoEncontradoError(UsuarioError):
    """El usuario no está registrado en el sistema."""
    def __init__(self, id_usuario=None, nombre=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        
        if id_usuario:
            mensaje = f"Usuario con ID {id_usuario} no encontrado"
        elif nombre:
            mensaje = f"Usuario con nombre '{nombre}' no encontrado"
        else:
            mensaje = "Usuario no encontrado"
            
        super().__init__(mensaje)

class PrestamoLimiteExcedidoError(UsuarioError):
    """El usuario ha alcanzado su límite de préstamos."""
    def __init__(self, usuario, limite):
        self.usuario = usuario
        self.limite = limite
        mensaje = f"El usuario {usuario} ha alcanzado el límite de {limite} préstamos"
        super().__init__(mensaje)


class Biblioteca:
    def __init__(self):
        # Simulamos una base de datos simple
        self.libros = {
            "978-1234567": {"titulo": "Python Avanzado", "disponible": True},
            "978-7654321": {"titulo": "Algoritmos en Python", "disponible": False, 
                           "fecha_devolucion": "2023-12-15"}
        }
        self.usuarios = {
            101: {"nombre": "Ana García", "prestamos": 0, "limite": 3},
            102: {"nombre": "Carlos López", "prestamos": 3, "limite": 3}
        }
    
    def buscar_libro(self, isbn=None, titulo=None):
        if isbn and isbn in self.libros:
            return isbn, self.libros[isbn]
        
        if titulo:
            for isbn_libro, datos in self.libros.items():
                if datos["titulo"] == titulo:
                    return isbn_libro, datos
        
        raise LibroNoEncontradoError(isbn, titulo)
    
    def verificar_disponibilidad(self, isbn):
        isbn, libro = self.buscar_libro(isbn=isbn)
        
        if not libro["disponible"]:
            raise LibroNoDisponibleError(
                libro["titulo"], 
                libro.get("fecha_devolucion")
            )
        
        return True
    
    def buscar_usuario(self, id_usuario):
        if id_usuario not in self.usuarios:
            raise UsuarioNoEncontradoError(id_usuario)
        
        return self.usuarios[id_usuario]
    
    def prestar_libro(self, isbn, id_usuario):
        # Verificar que el libro existe y está disponible
        self.verificar_disponibilidad(isbn)
        
        # Verificar que el usuario existe
        usuario = self.buscar_usuario(id_usuario)
        
        # Verificar que el usuario no ha excedido su límite
        if usuario["prestamos"] >= usuario["limite"]:
            raise PrestamoLimiteExcedidoError(
                usuario["nombre"], 
                usuario["limite"]
            )
        
        # Realizar el préstamo
        self.libros[isbn]["disponible"] = False
        usuario["prestamos"] += 1
        
        return True


biblioteca = Biblioteca()

def realizar_prestamo():
    try:
        isbn = input("Introduce el ISBN del libro: ")
        id_usuario = int(input("Introduce el ID del usuario: "))
        
        biblioteca.prestar_libro(isbn, id_usuario)
        print("¡Préstamo realizado con éxito!")
        
    except LibroNoEncontradoError as e:
        print(f"Error: {e}")
        print("Verifica el ISBN o busca por título.")
        
    except LibroNoDisponibleError as e:
        print(f"Error: {e}")
        if e.fecha_devolucion:
            print(f"Puedes reservarlo para después de {e.fecha_devolucion}")
            
    except UsuarioNoEncontradoError as e:
        print(f"Error: {e}")
        print("El usuario debe registrarse antes de solicitar préstamos.")
        
    except PrestamoLimiteExcedidoError as e:
        print(f"Error: {e}")
        print("El usuario debe devolver algún libro antes de solicitar más préstamos.")
        
    except ValueError:
        print("Error: El ID de usuario debe ser un número.")
        
    except BibliotecaError as e:
        # Captura cualquier otra excepción de la biblioteca
        print(f"Error en el sistema de biblioteca: {e}")
