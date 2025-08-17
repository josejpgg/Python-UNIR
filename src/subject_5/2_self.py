class Contador:
    # Atributo de clase - compartido por todas las instancias
    total_contadores = 0
    
    def __init__(self, valor_inicial=0):
        # Atributos de instancia - únicos para cada objeto
        self.valor = valor_inicial
        # Accedemos al atributo de clase mediante la clase
        Contador.total_contadores += 1
    
    def incrementar(self):
        self.valor += 1
        
    def obtener_valor(self):
        return self.valor
    
    @classmethod
    def obtener_total(cls):
        return cls.total_contadores

contador1 = Contador()
contador2 = Contador(10)

contador1.incrementar()
contador1.incrementar()
contador2.incrementar()

print(contador1.obtener_valor())  # Muestra: 2
print(contador2.obtener_valor())  # Muestra: 11
print(Contador.obtener_total())   # Muestra: 2








class Matematicas:
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @classmethod
    def valor_pi(cls):
        return 3.1416

# Llamadas sin crear instancias
resultado = Matematicas.sumar(5, 3)  # Devuelve: 8
pi = Matematicas.valor_pi()          # Devuelve: 3.1416












class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, otro_punto):
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)

# __init__ se llama al crear el objeto
p1 = Punto(3, 4)  # Argumentos 3 y 4 para x e y

# __str__ se llama implícitamente al convertir a string
print(p1)  # Imprime: (3, 4)

# __add__ se llama implícitamente con el operador +
p2 = Punto(2, 1)
p3 = p1 + p2  # Equivale a p1.__add__(p2)
print(p3)  # Imprime: (5, 5)











class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        # Creamos un nuevo vector sumando las coordenadas
        return Vector2D(self.x + otro.x, self.y + otro.y)
    
    def __sub__(self, otro):
        return Vector2D(self.x - otro.x, self.y - otro.y)
    
    def __mul__(self, escalar):
        # Multiplicación por un escalar
        return Vector2D(self.x * escalar, self.y * escalar)
    
    def __eq__(self, otro):
        # Comparación de igualdad
        return self.x == otro.x and self.y == otro.y
    
    def __str__(self):
        # Representación como string
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        # Representación para desarrolladores
        return f"Vector2D({self.x}, {self.y})"












