from collections import namedtuple

# Sintaxis básica: namedtuple(nombre_tipo, [lista_de_campos])
Punto = namedtuple('Punto', ['x', 'y'])

# Creamos una instancia
p = Punto(10, 20)



# Usando una cadena con espacios
Persona = namedtuple('Persona', 'nombre edad profesion')

# Usando una cadena con comas
Direccion = namedtuple('Direccion', 'calle,numero,ciudad,codigo_postal')




Punto = namedtuple('Punto', ['x', 'y'])
p = Punto(10, 20)

# Acceso por nombre (como atributo)
print(p.x)  # 10
print(p.y)  # 20

# Acceso por índice (como tupla normal)
print(p[0])  # 10
print(p[1])  # 20

# Desempaquetado como tupla normal
x, y = p
print(x, y)  # 10 20






Empleado = namedtuple('Empleado', 'nombre departamento salario')
e = Empleado('Ana', 'Desarrollo', 45000)

# Convertir a diccionario
print(e._asdict())  # {'nombre': 'Ana', 'departamento': 'Desarrollo', 'salario': 45000}

# Ver los nombres de los campos
print(e._fields)  # ('nombre', 'departamento', 'salario')

# Crear una nueva instancia reemplazando valores
e2 = e._replace(salario=50000)
print(e2)  # Empleado(nombre='Ana', departamento='Desarrollo', salario=50000)












# Usando defaults para asignar valores predeterminados
Configuracion = namedtuple('Configuracion', ['host', 'puerto', 'usuario', 'timeout'])
config_default = Configuracion._make(['localhost', 8080, 'admin', 30])

# En Python 3.7+ podemos usar defaults directamente
Configuracion = namedtuple('Configuracion', 'host puerto usuario timeout', defaults=['localhost', 8080, 'admin', 30])
config = Configuracion()
print(config)  # Configuracion(host='localhost', puerto=8080, usuario='admin', timeout=30)

# También podemos sobrescribir algunos valores
config_custom = Configuracion(puerto=9090, timeout=60)
print(config_custom)  # Configuracion(host='localhost', puerto=9090, usuario='admin', timeout=60)












import datetime

# Representando datos estructurados
Transaccion = namedtuple('Transaccion', 'id fecha monto descripcion')

# Creando instancias
t1 = Transaccion(1, datetime.date(2023, 5, 15), 150.75, "Compra de libros")
t2 = Transaccion(2, datetime.date(2023, 5, 16), 49.99, "Suscripción mensual")

# Procesando datos de manera clara
def calcular_total(transacciones):
    return sum(t.monto for t in transacciones)

total = calcular_total([t1, t2])
print(f"Total gastado: {total}")  # Total gastado: 200.74







# Comparación con un diccionario
punto_dict = {'x': 10, 'y': 20}
print(punto_dict['x'])  # Requiere sintaxis de diccionario

# Comparación con namedtuple
Punto = namedtuple('Punto', ['x', 'y'])
punto = Punto(10, 20)
print(punto.x)  # Sintaxis más clara y concisa













from typing import NamedTuple

class Punto1(NamedTuple):
    x: int
    y: int
    etiqueta: str = "Sin etiqueta"  # Valor por defecto
    
p = Punto1(10, 20)
print(p)  # Punto(x=10, y=20, etiqueta='Sin etiqueta')

# Con anotaciones de tipo, el IDE puede ofrecer mejor autocompletado
# y detectar errores de tipo en tiempo de desarrollo










from collections import Counter

c1 = Counter(a=3, b=1, c=2)
c2 = Counter(a=1, b=2, d=3)

# Suma (unión con suma de conteos)
print(c1 + c2)  # Counter({'a': 4, 'd': 3, 'b': 3, 'c': 2})

# Resta (mantiene solo conteos positivos)
print(c1 - c2)  # Counter({'a': 2, 'c': 2})

# Intersección (mínimo de conteos)
print(c1 & c2)  # Counter({'a': 1, 'b': 1})

# Unión (máximo de conteos)
print(c1 | c2)  # Counter({'a': 3, 'd': 3, 'c': 2, 'b': 2})










import re

texto = """Python es un lenguaje de programación interpretado cuya filosofía 
hace hincapié en la legibilidad de su código. Es un lenguaje multiparadigma."""

# Convertir a minúsculas y dividir en palabras
palabras = re.findall(r'\w+', texto.lower())
frecuencia = Counter(palabras)

print(frecuencia.most_common(5))
# [('es', 2), ('un', 2), ('lenguaje', 2), ('python', 1), ('de', 1)]









from collections import deque

# Crear una deque vacía
d = deque()

# Crear una deque con elementos iniciales
numeros = deque([1, 2, 3, 4, 5])
texto = deque("Python")
print(numeros)  # deque([1, 2, 3, 4, 5])
print(texto)    # deque(['P', 'y', 't', 'h', 'o', 'n'])



d = deque([1, 2, 3])

# Añadir elementos al final (como append en listas)
d.append(4)
print(d)  # deque([1, 2, 3, 4])

# Añadir elementos al principio (operación eficiente)
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3, 4])

# Eliminar y devolver el último elemento
ultimo = d.pop()
print(ultimo)  # 4
print(d)       # deque([0, 1, 2, 3])

# Eliminar y devolver el primer elemento
primero = d.popleft()
print(primero)  # 0
print(d)        # deque([1, 2, 3])




import time

# Comparación de rendimiento: insertar al principio
n = 100000

# Con lista
inicio = time.time()
lista = []
for i in range(n):
    lista.insert(0, i)  # O(n) - cada vez más lento
tiempo_lista = time.time() - inicio

# Con deque
inicio = time.time()
d = deque()
for i in range(n):
    d.appendleft(i)  # O(1) - tiempo constante
tiempo_deque = time.time() - inicio

print(f"Tiempo con lista: {tiempo_lista:.4f} segundos")
print(f"Tiempo con deque: {tiempo_deque:.4f} segundos")
print(f"deque es aproximadamente {tiempo_lista/tiempo_deque:.1f}x más rápido")








d = deque([1, 2, 3, 4, 5])

# Extender con múltiples elementos
d.extend([6, 7, 8])
print(d)  # deque([1, 2, 3, 4, 5, 6, 7, 8])

# Extender por la izquierda
d.extendleft([0, -1, -2])  # Nota: se añaden en orden inverso
print(d)  # deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

# Rotar elementos (desplazar a la derecha)
d.rotate(2)
print(d)  # deque([7, 8, -2, -1, 0, 1, 2, 3, 4, 5, 6])

# Rotar elementos a la izquierda (con número negativo)
d.rotate(-3)
print(d)  # deque([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, -2])

# Eliminar la primera ocurrencia de un valor
d.remove(5)
print(d)  # deque([-1, 0, 1, 2, 3, 4, 6, 7, 8, -2])

# Contar ocurrencias
print(d.count(1))  # 1

# Limpiar la deque
d.clear()
print(d)  # deque([])













# Crear una deque con tamaño máximo
historial = deque(maxlen=3)

# Al añadir elementos más allá del límite, se eliminan los más antiguos
historial.append("página 1")
historial.append("página 2")
historial.append("página 3")
print(historial)  # deque(['página 1', 'página 2', 'página 3'], maxlen=3)

historial.append("página 4")
print(historial)  # deque(['página 2', 'página 3', 'página 4'], maxlen=3)

# El tamaño máximo no puede modificarse después de la creación
print(historial.maxlen)  # 3








# Historial de navegación

class Navegador:
    def __init__(self, max_historial=10):
        self.historial = deque(maxlen=max_historial)
        self.pagina_actual = None
        
    def navegar(self, url):
        if self.pagina_actual:
            self.historial.append(self.pagina_actual)
        self.pagina_actual = url
        print(f"Navegando a: {url}")
        
    def retroceder(self):
        if not self.historial:
            print("No hay páginas anteriores")
            return
        
        self.pagina_actual, anterior = self.historial.pop(), self.pagina_actual
        print(f"Volviendo a: {self.pagina_actual}")
        
# Ejemplo de uso
navegador = Navegador()
navegador.navegar("google.com")
navegador.navegar("wikipedia.org")
navegador.navegar("python.org")
navegador.retroceder()  # Vuelve a wikipedia.org


# Implementación de una cola FIFO (First In, First Out)

from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
        
    def encolar(self, elemento):
        self.elementos.append(elemento)
        
    def desencolar(self):
        if not self.elementos:
            raise IndexError("La cola está vacía")
        return self.elementos.popleft()
        
    def esta_vacia(self):
        return len(self.elementos) == 0
        
    def tamano(self):
        return len(self.elementos)
        
# Ejemplo: sistema de procesamiento de tareas
cola_tareas = Cola()
cola_tareas.encolar("Tarea 1")
cola_tareas.encolar("Tarea 2")
cola_tareas.encolar("Tarea 3")

while not cola_tareas.esta_vacia():
    tarea = cola_tareas.desencolar()
    print(f"Procesando: {tarea}")



import sys

# Comparación de uso de memoria
lista = list(range(1000))
d = deque(range(1000))

print(f"Memoria de lista: {sys.getsizeof(lista)} bytes")
print(f"Memoria de deque: {sys.getsizeof(d)} bytes")
