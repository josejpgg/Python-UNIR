# Lambda sin argumentos que siempre devuelve Hola mundo
saludo = lambda: "Hola mundo"
print(saludo())  # Imprime: Hola mundo




# Lambda que recibe un número y devuelve su cuadrado
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime: 25






# Lambda con un argumento por defecto
incrementar = lambda x, incremento=1: x + incremento
print(incrementar(5))      # Imprime: 6 (usa el valor por defecto)
print(incrementar(5, 2))   # Imprime: 7 (usa el valor proporcionado)






# Lambda que determina si un número es par o impar
es_par = lambda x: "Par" if x % 2 == 0 else "Impar"
print(es_par(4))  # Imprime: Par
print(es_par(7))  # Imprime: Impar






# Filtrar números pares de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Imprime: [2, 4, 6, 8, 10]

# Aplicar una operación a cada elemento de una lista
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Imprime: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]











# Esto NO es válido en una lambda:
# lambda x: 
#     resultado = x * 2
#     return resultado

# En su lugar, usaríamos una función normal:
def duplicar(x):
    resultado = x * 2
    return resultado









# Ordenar una lista de números por su valor absoluto
numeros = [5, -2, 8, -1, 9, -3]
ordenados_por_abs = sorted(numeros, key=lambda x: abs(x))
print(ordenados_por_abs)  # Imprime: [-1, -2, -3, 5, 8, 9]









# Ordenar cadenas por longitud en lugar de alfabéticamente
palabras = ["python", "es", "un", "lenguaje", "de", "programación"]
ordenadas_por_longitud = sorted(palabras, key=lambda palabra: len(palabra))
print(ordenadas_por_longitud)  # Imprime: ['es', 'un', 'de', 'python', 'lenguaje', 'programación']







# Ordenar números de mayor a menor
numeros = [5, 2, 8, 1, 9, 3]
descendente = sorted(numeros, reverse=True)
print(descendente)  # Imprime: [9, 8, 5, 3, 2, 1]

# Ordenar palabras de la más larga a la más corta
palabras = ["python", "es", "genial"]
por_longitud_desc = sorted(palabras, key=lambda p: len(p), reverse=True)
print(por_longitud_desc)  # Imprime: ['python', 'genial', 'es']












# Lista de diccionarios que representan personas
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Berta", "edad": 20},
    {"nombre": "Daniel", "edad": 25}
]

# Ordenar por edad
ordenadas_por_edad = sorted(personas, key=lambda persona: persona["edad"])
print("Ordenadas por edad:")
for p in ordenadas_por_edad:
    print(f"{p['nombre']}: {p['edad']} años")
# Imprime personas ordenadas por edad (Berta, Ana, Daniel, Carlos)

# Ordenar por nombre
ordenadas_por_nombre = sorted(personas, key=lambda persona: persona["nombre"])
print("\nOrdenadas por nombre:")
for p in ordenadas_por_nombre:
    print(f"{p['nombre']}: {p['edad']} años")
# Imprime personas ordenadas alfabéticamente por nombre












class Estudiante:
    def __init__(self, nombre, nota, curso):
        self.nombre = nombre
        self.nota = nota
        self.curso = curso
    
    def __repr__(self):
        return f"{self.nombre} ({self.curso}): {self.nota}"

estudiantes = [
    Estudiante("Ana", 8.5, "Python"),
    Estudiante("Luis", 7.0, "JavaScript"),
    Estudiante("Elena", 9.2, "Python"),
    Estudiante("Carlos", 6.8, "JavaScript")
]

# Ordenar por nota (de mayor a menor)
por_nota = sorted(estudiantes, key=lambda e: e.nota, reverse=True)
print("Ordenados por nota:")
for e in por_nota:
    print(e)

# Ordenar primero por curso y luego por nota
por_curso_y_nota = sorted(estudiantes, key=lambda e: (e.curso, -e.nota))
print("\nOrdenados por curso y nota (descendente):")
for e in por_curso_y_nota:
    print(e)









# Lambda demasiado compleja (difícil de leer)
transformar = lambda datos: {k: [i*2 if i > 0 else 0 for i in v] for k, v in datos.items() if len(v) > 2}

# Mejor como función tradicional
def transformar_datos(datos):
    resultado = {}
    for k, v in datos.items():
        if len(v) > 2:
            resultado[k] = [i*2 if i > 0 else 0 for i in v]
    return resultado
















