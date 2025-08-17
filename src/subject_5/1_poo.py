class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass  # Método que será implementado por las subclases

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

def hacer_sonar(animal):
    return animal.hacer_sonido()

perro = Perro("Fido")
gato = Gato("Whiskers")

print(hacer_sonar(perro))  # Imprime: Guau
print(hacer_sonar(gato))   # Imprime: Miau



# Ejemplo de duck typing
def procesar_secuencia(secuencia):
    return secuencia[0]  # Funciona con cualquier objeto que soporte indexación

# Funciona con diferentes tipos
print(procesar_secuencia([1, 2, 3]))       # Lista
print(procesar_secuencia((4, 5, 6)))       # Tupla
print(procesar_secuencia("Python"))        # String



# Algunos métodos especiales comunes incluyen:

# __init__: Inicializa un nuevo objeto
# __str__: Devuelve una representación legible del objeto
# __repr__: Devuelve una representación que idealmente podría usarse para recrear el objeto
# __len__: Define el comportamiento cuando se usa len(objeto)
# __eq__: Define cómo se comparan dos objetos con el operador ==




def agregar_metodo(cls):
    """Decorador que agrega un método a la clase."""
    def metodo_nuevo(self):
        return "Este método fue agregado por un decorador"
    
    cls.metodo_nuevo = metodo_nuevo
    return cls

@agregar_metodo
class MiClase:
    def metodo_original(self):
        return "Este es el método original"

obj = MiClase()
print(obj.metodo_original())  # Este es el método original
print(obj.metodo_nuevo())     # Este método fue agregado por un decorador









class PersonaOptimizada:
    __slots__ = ['nombre', 'edad']
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = PersonaOptimizada("Laura", 29)
p.nombre = "Laura García"  # Permitido
p.peso = 65  # Error: 'PersonaOptimizada' object has no attribute 'peso'













class Producto:
    """
    Representa un producto en un sistema de inventario.
    """
    # Atributo de clase
    iva = 0.21
    
    def __init__(self, codigo, nombre, precio):
        # Atributos de instancia
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def calcular_precio_final(self):
        """Calcula el precio con IVA incluido."""
        return self.precio * (1 + self.iva)
    
    def __str__(self):
        return f"{self.nombre} (${self.precio:.2f})"
    
    @classmethod
    def cambiar_iva(cls, nuevo_iva):
        """Cambia la tasa de IVA para todos los productos."""
        cls.iva = nuevo_iva

# Creamos algunos productos
laptop = Producto("P001", "Laptop HP", 850)
telefono = Producto("P002", "Smartphone XYZ", 450)

# Accedemos a atributos y métodos
print(laptop.nombre)  # Laptop HP
print(telefono.calcular_precio_final())  # 544.5

# Cambiamos el IVA para todos los productos
Producto.cambiar_iva(0.16)
print(laptop.calcular_precio_final())  # 986.0












class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
    
    def encender(self):
        self.encendido = True

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        # Llamamos al constructor de la clase base
        super().__init__(marca, modelo, año)
        # Añadimos atributos específicos
        self.puertas = puertas
        self.velocidad = 0

# Uso de la clase derivada
mi_auto = Automovil("Toyota", "Corolla", 2022, 4)
print(f"{mi_auto.marca} {mi_auto.modelo}")  # Toyota Corolla
mi_auto.encender()  # Método heredado
print(f"Encendido: {mi_auto.encendido}")  # Encendido: True











class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    
    @classmethod
    def desde_texto(cls, texto):
        """Constructor alternativo que crea una fecha desde un texto."""
        dia, mes, año = map(int, texto.split('/'))
        return cls(dia, mes, año)
    
    @classmethod
    def hoy(cls):
        """Constructor alternativo que crea una fecha con la fecha actual."""
        from datetime import date
        fecha_actual = date.today()
        return cls(fecha_actual.day, fecha_actual.month, fecha_actual.year)
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"

# Diferentes formas de crear objetos
fecha1 = Fecha(15, 6, 2023)  # Constructor normal
fecha2 = Fecha.desde_texto("25/12/2023")  # Constructor alternativo
fecha3 = Fecha.hoy()  # Constructor que usa la fecha actual

print(fecha1)  # 15/06/2023
print(fecha2)  # 25/12/2023













class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def radio(self):
        """Getter para el radio"""
        return self._radio
    
    @radio.setter
    def radio(self, valor):
        """Setter para el radio con validación"""
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor
    
    @property
    def area(self):
        """Propiedad calculada (solo lectura)"""
        import math
        return math.pi * self._radio ** 2
    
    @property
    def diametro(self):
        """Propiedad calculada (solo lectura)"""
        return self._radio * 2

# Uso de properties
circulo = Circulo(5)

# Acceso como si fueran atributos
print(circulo.radio)     # 5
print(circulo.area)      # 78.53981633974483
print(circulo.diametro)  # 10

# Modificación con validación
circulo.radio = 7
print(circulo.radio)     # 7
print(circulo.area)      # 153.93804002589985

# Intento de asignar un valor inválido
try:
    circulo.radio = -2
except ValueError as e:
    print(f"Error: {e}")  # Error: El radio debe ser positivo

# Intento de modificar una propiedad de solo lectura
try:
    circulo.area = 100
except AttributeError as e:
    print(f"Error: {e}")  # Error: can't set attribute 'area'










