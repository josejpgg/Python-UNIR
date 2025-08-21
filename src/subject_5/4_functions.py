class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    
    # Método de instancia
    def mostrar_fecha(self):
        return f"{self.dia}/{self.mes}/{self.año}"
    
    # Método de clase
    @classmethod
    def desde_cadena(cls, cadena_fecha):
        # Crea una instancia de Fecha a partir de una cadena (factory method)
        dia, mes, año = map(int, cadena_fecha.split('-'))
        return cls(dia, mes, año)
    
    # Otro método de clase
    @classmethod
    def hoy(cls):
        # Podríamos importar datetime aquí para obtener la fecha actual
        return cls(1, 1, 2023)  # Ejemplo simplificado

# Uso de métodos de clase
fecha1 = Fecha(15, 3, 2023)
fecha2 = Fecha.desde_cadena("25-12-2023")  # Llamada al método de clase
fecha3 = Fecha.hoy()  # Otro método de clase

print(fecha1.mostrar_fecha())  # 15/3/2023
print(fecha2.mostrar_fecha())  # 25/12/2023






# Métodos de instancia: Cuando necesites acceder o modificar atributos específicos de una instancia.
# Métodos de clase: Cuando necesites acceder o modificar atributos de la clase, o crear constructores alternativos.
# Métodos estáticos: Cuando necesites una función relacionada con la clase pero que no dependa del estado de la instancia ni de la clase.

class Producto:
    # Variable de clase
    iva = 0.21
    total_productos = 0
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Producto.total_productos += 1
    
    # Método de instancia
    def precio_con_iva(self):
        return self.precio * (1 + self.iva)
    
    # Método de clase
    @classmethod
    def cambiar_iva(cls, nuevo_iva):
        cls.iva = nuevo_iva
        return f"IVA actualizado a {cls.iva}"
    
    # Método estático
    @staticmethod
    def es_caro(precio):
        return precio > 100

# Uso de los diferentes tipos de métodos
producto1 = Producto("Laptop", 800)
producto2 = Producto("Mouse", 25)

# Método de instancia - necesita una instancia
print(producto1.precio_con_iva())  # 968.0

# Método de clase - se puede llamar desde la clase o instancia
print(Producto.cambiar_iva(0.10))  # IVA actualizado a 0.1
print(producto1.precio_con_iva())  # 880.0 (ahora con el nuevo IVA)

# Método estático - independiente del estado
print(Producto.es_caro(1500))  # True
print(producto1.es_caro(50))  # False





class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.paginas} páginas)"

# Uso del método __str__
libro = Libro("Don Quijote", "Miguel de Cervantes", 863)
print(libro)  # Don Quijote por Miguel de Cervantes (863 páginas)









# Una buena implementación de __repr__ debería, idealmente, generar código Python que al evaluarse cree un objeto idéntico:


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Punto en ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

# Uso de __str__ y __repr__
p = Punto(3, 4)
print(p)  # Usa __str__: "Punto en (3, 4)"
print(repr(p))  # Usa __repr__: "Punto(3, 4)"

puntos = [Punto(1, 2), Punto(3, 4)]
print(puntos)  # [Punto(1, 2), Punto(3, 4)] - Usa __repr__ para cada elemento












import datetime

class Reserva:
    def __init__(self, id, cliente, fecha):
        self.id = id
        self.cliente = cliente
        self.fecha = fecha
    
    def __str__(self):
        # Representación amigable para el usuario
        return f"Reserva #{self.id} - {self.cliente} para el {self.fecha.strftime('%d/%m/%Y')}"
    
    def __repr__(self):
        # Representación técnica para desarrolladores
        return f"Reserva(id={self.id}, cliente='{self.cliente}', fecha=datetime.date({self.fecha.year}, {self.fecha.month}, {self.fecha.day}))"

# Creamos una reserva
fecha = datetime.date(2023, 12, 25)
reserva = Reserva(101, "Juan Pérez", fecha)

# Diferentes contextos de uso
print(str(reserva))   # Reserva #101 - Juan Pérez para el 25/12/2023
print(repr(reserva))  # Reserva(id=101, cliente='Juan Pérez', fecha=datetime.date(2023, 12, 25))

# En una lista, se usa __repr__
reservas = [reserva]
print(reservas)  # [Reserva(id=101, cliente='Juan Pérez', fecha=datetime.date(2023, 12, 25))]










# El método __eq__ define el comportamiento del operador de igualdad (==) para objetos de nuestra clase. Sin este método, Python compara la identidad de los objetos (si son el mismo objeto en memoria), no sus valores.




class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
    
    def __eq__(self, other):
        # Verificamos que other sea una instancia de Carta
        if not isinstance(other, Carta):
            return False
        # Comparamos por valor y palo
        return self.valor == other.valor and self.palo == other.palo
    
    def __str__(self):
        return f"{self.valor} de {self.palo}"

# Creamos dos cartas con los mismos valores
carta1 = Carta("As", "Corazones")
carta2 = Carta("As", "Corazones")
carta3 = Carta("Rey", "Picas")

# Sin __eq__, estas comparaciones serían False
print(carta1 == carta2)  # True - mismos valores
print(carta1 == carta3)  # False - diferentes valores










class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    
    def __eq__(self, other):
        if not isinstance(other, Usuario):
            return NotImplemented
        return self.id == other.id
    
    def __hash__(self):
        # El hash debe ser consistente con la igualdad
        return hash(self.id)
    
    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"
    
    def __repr__(self):
        return f"Usuario({self.id}, '{self.nombre}')"

# Creamos usuarios
u1 = Usuario(1, "Ana")
u2 = Usuario(1, "Ana Modificada")  # Mismo ID
u3 = Usuario(2, "Ana")             # Mismo nombre, diferente ID

# Uso en diccionarios
usuarios_datos = {
    u1: "Datos de Ana",
    u3: "Datos de otra Ana"
}

# Como u1 y u2 son "iguales" (mismo ID), comparten la misma entrada
print(usuarios_datos[u1])  # "Datos de Ana"
print(usuarios_datos[u2])  # "Datos de Ana" (mismo que u1)









import json

class Configuracion:
    def __init__(self, tema, idioma, notificaciones=True):
        self.tema = tema
        self.idioma = idioma
        self.notificaciones = notificaciones
    
    def __repr__(self):
        return f"Configuracion('{self.tema}', '{self.idioma}', {self.notificaciones})"
    
    def to_dict(self):
        return {
            'tema': self.tema,
            'idioma': self.idioma,
            'notificaciones': self.notificaciones
        }
    
    @classmethod
    def from_dict(cls, datos):
        return cls(datos['tema'], datos['idioma'], datos['notificaciones'])

# Serialización
config = Configuracion("oscuro", "es", True)
json_data = json.dumps(config.to_dict())

# Deserialización
config_dict = json.loads(json_data)
config_recuperada = Configuracion.from_dict(config_dict)

print(repr(config_recuperada))  # Configuracion('oscuro', 'es', True)













# Mantén __str__ simple y legible para usuarios finales
# Haz que __repr__ sea informativo y completo para desarrolladores
# Implementa __eq__ y __hash__ juntos si necesitas comparaciones de igualdad
# Verifica el tipo en __eq__ para evitar comparaciones inválidas
# Usa los atributos relevantes para la identidad del objeto en __eq__ y __hash__

class Persona:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def __repr__(self):
        return f"Persona('{self.dni}', '{self.nombre}', '{self.apellido}')"
    
    def __eq__(self, other):
        if not isinstance(other, Persona):
            return NotImplemented
        return self.dni == other.dni
    
    def __hash__(self):
        return hash(self.dni)










class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio  # Atributo protegido
    
    @property
    def precio(self):
        """Getter para el precio"""
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        """Setter para el precio con validación"""
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

# Uso de propiedades
producto = Producto("Laptop", 1200)
print(producto.precio)  # 1200 - Parece un atributo pero llama al getter

producto.precio = 1300  # Parece una asignación pero llama al setter
print(producto.precio)  # 1300

# Esto lanzaría una excepción:
# producto.precio = -100










class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor
    
    @property
    def area(self):
        """Propiedad de solo lectura que calcula el área"""
        return 3.14159 * self._radio ** 2
    
    @property
    def perimetro(self):
        """Otra propiedad de solo lectura"""
        return 2 * 3.14159 * self._radio

# Uso de propiedades de solo lectura
circulo = Circulo(5)
print(circulo.area)      # 78.53975 - Calculado bajo demanda
print(circulo.perimetro) # 31.4159

# Esto lanzaría un AttributeError:
# circulo.area = 100












class Usuario:
    def __init__(self, nombre, apellido, email):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
    
    @property
    def nombre_completo(self):
        """Combina nombre y apellido"""
        return f"{self._nombre} {self._apellido}"
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, nuevo_email):
        # Validación básica de formato de email
        if '@' not in nuevo_email or '.' not in nuevo_email:
            raise ValueError("Formato de email inválido")
        
        # Podríamos añadir lógica adicional:
        # - Verificar dominio
        # - Normalizar a minúsculas
        # - Registrar el cambio en un log
        self._email = nuevo_email.lower()
        print(f"Email actualizado a: {self._email}")

# Uso con lógica compleja
usuario = Usuario("Juan", "Pérez", "juan@ejemplo.com")
print(usuario.nombre_completo)  # Juan Pérez

usuario.email = "JUAN.PEREZ@EMPRESA.COM"  # Se normaliza a minúsculas
print(usuario.email)  # juan.perez@empresa.com

# Esto lanzaría una excepción:
# usuario.email = "correo_invalido"










class Analisis:
    def __init__(self, datos):
        self._datos = datos
        self._estadisticas = None  # Caché para resultados calculados
    
    @property
    def estadisticas(self):
        """Calcula estadísticas solo cuando se necesitan"""
        if self._estadisticas is None:
            print("Calculando estadísticas (operación costosa)...")
            # Simulamos un cálculo costoso
            import time
            time.sleep(1)
            
            # Calculamos varias estadísticas
            self._estadisticas = {
                'suma': sum(self._datos),
                'promedio': sum(self._datos) / len(self._datos),
                'maximo': max(self._datos),
                'minimo': min(self._datos)
            }
        
        return self._estadisticas
    
    def actualizar_datos(self, nuevos_datos):
        """Al cambiar los datos, invalidamos la caché"""
        self._datos = nuevos_datos
        self._estadisticas = None  # Invalidamos la caché

# Uso de propiedades con caché
analisis = Analisis([1, 2, 3, 4, 5])

# La primera vez calcula
print(analisis.estadisticas)  # Muestra "Calculando estadísticas..."
# {'suma': 15, 'promedio': 3.0, 'maximo': 5, 'minimo': 1}

# La segunda vez usa la caché
print(analisis.estadisticas)  # No muestra el mensaje, usa el valor en caché

# Al actualizar los datos, se invalida la caché
analisis.actualizar_datos([10, 20, 30])
print(analisis.estadisticas)  # Vuelve a calcular con los nuevos datos







class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Público
        self._edad = edad     # Privado con getter/setter
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor
    
    # Mal: mezcla estilos de acceso
    def get_nombre(self):  # No hagas esto si ya usas propiedades
        return self.nombre
