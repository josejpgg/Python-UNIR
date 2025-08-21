class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        return f"{self.marca} {self.modelo} encendido"
    
    def apagar(self):
        self.encendido = False
        return f"{self.marca} {self.modelo} apagado"
    
    def describir(self):
        return f"Vehículo {self.marca} {self.modelo} del año {self.año}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        # Llamamos al constructor de la clase padre
        super().__init__(marca, modelo, año)
        # Añadimos atributos específicos
        self.puertas = puertas
        self.velocidad = 0
    
    def acelerar(self, incremento):
        self.velocidad += incremento
        return f"Acelerando a {self.velocidad} km/h"
    
    # Modificamos un método heredado
    def describir(self):
        return f"Automóvil {self.marca} {self.modelo} ({self.año}) con {self.puertas} puertas"


# Verificar si una clase es subclase de otra
print(issubclass(Automovil, Vehiculo))  # True

# Verificar si un objeto es instancia de una clase
mi_auto = Automovil("Honda", "Civic", 2023, 4)
print(isinstance(mi_auto, Automovil))  # True
print(isinstance(mi_auto, Vehiculo))  # True - También es instancia de la clase base











class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.conocimientos = []
    
    def estudiar(self, tema):
        self.conocimientos.append(tema)
        return f"{self.nombre} está estudiando {tema}"

class EstudianteGraduado(Estudiante):
    def __init__(self, nombre, edad, titulo):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.titulo = titulo  # Añadimos un nuevo atributo
    
    def estudiar(self, tema):
        # Extendemos el método estudiar
        mensaje_base = super().estudiar(tema)  # Llamamos al método de la clase base
        return f"{mensaje_base} a nivel avanzado para su investigación de {self.titulo}"

graduado = EstudianteGraduado("María", 24, "Inteligencia Artificial")
print(graduado.estudiar("Redes Neuronales"))
# María está estudiando Redes Neuronales a nivel avanzado para su investigación de Inteligencia Artificial











from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    def describir(self):
        return f"Área: {self.area()}, Perímetro: {self.perimetro()}"

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

# No podemos instanciar la clase abstracta
# figura = FiguraGeometrica()  # Esto generaría un error

# Pero sí podemos instanciar la clase derivada
rectangulo = Rectangulo(5, 3)
print(rectangulo.area())       # 15
print(rectangulo.perimetro())  # 16
print(rectangulo.describir())  # Área: 15, Perímetro: 16













# MRO
# MRO (Method Resolution Order) determina el orden en que se buscan los métodos en las clases base.

class A:
    def metodo(self):
        print("A.metodo")

class B(A):
    def metodo(self):
        print("B.metodo")
        super().metodo()

class C(A):
    def metodo(self):
        print("C.metodo")
        super().metodo()

class D(B, C):
    def metodo(self):
        print("D.metodo")
        super().metodo()

d = D()
d.metodo()
# Salida:
# D.metodo
# B.metodo
# C.metodo
# A.metodo



# Verificación del MRO en tiempo de desarrollo

def mostrar_mro(clase):
    print(f"MRO de {clase.__name__}:")
    for i, c in enumerate(clase.__mro__):
        print(f"  {i+1}. {c.__name__}")

class Animal: pass
class Mamifero(Animal): pass
class Ave(Animal): pass
class Murcielago(Mamifero, Ave): pass

mostrar_mro(Murcielago)
# MRO de Murcielago:
#   1. Murcielago
#   2. Mamifero
#   3. Ave
#   4. Animal
#   5. object













# Ejemplo práctico: Sistema de interfaces gráficas

class Widget:
    def __init__(self, x=0, y=0, visible=True):
        self.x = x
        self.y = y
        self.visible = visible
    
    def dibujar(self):
        if self.visible:
            return f"Dibujando widget en ({self.x}, {self.y})"
        return ""

class Clickable:
    def __init__(self, on_click=None, **kwargs):
        super().__init__(**kwargs)
        self.on_click = on_click or (lambda: None)
    
    def click(self):
        return self.on_click()

class Draggable:
    def __init__(self, dragging=False, **kwargs):
        super().__init__(**kwargs)
        self.dragging = dragging
    
    def iniciar_arrastre(self):
        self.dragging = True
        return "Iniciando arrastre"
    
    def finalizar_arrastre(self):
        self.dragging = False
        return "Finalizando arrastre"

class Boton(Widget, Clickable):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.texto = texto
    
    def dibujar(self):
        base = super().dibujar()
        if base:
            return f"{base} - Botón: {self.texto}"
        return ""

class IconoArrastrable(Widget, Clickable, Draggable):
    def __init__(self, icono, **kwargs):
        super().__init__(**kwargs)
        self.icono = icono
    
    def dibujar(self):
        base = super().dibujar()
        if base:
            estado = "arrastrándose" if self.dragging else "estático"
            return f"{base} - Icono: {self.icono} ({estado})"
        return ""

def accion_boton():
    return "Botón pulsado!"

boton = Boton(
    texto="Aceptar",
    x=100, 
    y=200,
    on_click=accion_boton
)

icono = IconoArrastrable(
    icono="📁",
    x=50,
    y=50
)

print(boton.dibujar())        # Dibujando widget en (100, 200) - Botón: Aceptar
print(boton.click())          # Botón pulsado!

print(icono.dibujar())        # Dibujando widget en (50, 50) - Icono: 📁 (estático)
print(icono.iniciar_arrastre())
print(icono.dibujar())        # Dibujando widget en (50, 50) - Icono: 📁 (arrastrándose)

