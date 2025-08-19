
class Empleado:
    # Variables de clase
    empresa = "TechCorp"
    contador_empleados = 0
    salario_base = 30000
    
    def __init__(self, nombre):
        self.nombre = nombre




class Ejemplo:
    x = 10  # Variable de clase
    
    def cambiar(self):
        self.x = 20  # Crea una variable de instancia 'x' que sombrea la de clase

e1 = Ejemplo()
e2 = Ejemplo()

print(e1.x)  # 10 (accede a la variable de clase)
e1.cambiar()
print(e1.x)  # 20 (ahora accede a la variable de instancia)
print(e2.x)  # 10 (sigue accediendo a la variable de clase)
print(Ejemplo.x)  # 10 (la variable de clase no ha cambiado)







class Contador:
    _valor = 0
    
    @classmethod
    def incrementar(cls):
        cls._valor += 1
        return cls._valor
    
    @classmethod
    def obtener_valor(cls):
        return cls._valor

# Uso sin crear instancias
print(Contador.incrementar())  # 1
print(Contador.incrementar())  # 2
print(Contador.obtener_valor())  # 2





