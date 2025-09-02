# [expresion for elemento in iterable]



# Crear una matriz de 3x3 con valores iniciales en 0
matriz = [[0 for _ in range(3)] for _ in range(3)]
print(matriz)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Crear una matriz de identidad 3x3
identidad = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(identidad)  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]





# Set comprehensions

# {expresion for elemento in iterable}

# Método tradicional
cuadrados_set = set()
for numero in range(1, 6):
    cuadrados_set.add(numero ** 2)
print(cuadrados_set)  # {1, 4, 9, 16, 25}

# Usando set comprehension
cuadrados_set = {numero ** 2 for numero in range(1, 6)}
print(cuadrados_set)  # {1, 4, 9, 16, 25}







# Dictionary comprehensions

# {clave: valor for elemento in iterable}

# Método tradicional
cuadrados_dict = {}
for numero in range(1, 6):
    cuadrados_dict[numero] = numero ** 2
print(cuadrados_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Usando dictionary comprehension
cuadrados_dict = {numero: numero ** 2 for numero in range(1, 6)}
print(cuadrados_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}






# Convertir valores a mayúsculas
frutas = {"a": "apple", "b": "banana", "c": "cherry"}
frutas_mayusculas = {clave: valor.upper() for clave, valor in frutas.items()}
print(frutas_mayusculas)  # {'a': 'APPLE', 'b': 'BANANA', 'c': 'CHERRY'}

# Intercambiar claves y valores
frutas_invertidas = {valor: clave for clave, valor in frutas.items()}
print(frutas_invertidas)  # {'apple': 'a', 'banana': 'b', 'cherry': 'c'}







# Crear diccionario a partir de dos listas
nombres = ["Ana", "Juan", "María"]
edades = [25, 31, 28]
personas = {nombre: edad for nombre, edad in zip(nombres, edades)}
print(personas)  # {'Ana': 25, 'Juan': 31, 'María': 28}

# Crear conjunto de tuplas a partir de un diccionario
personas = {"Ana": 25, "Juan": 31, "María": 28}
personas_tuplas = {(nombre, edad) for nombre, edad in personas.items()}
print(personas_tuplas)  # {('Ana', 25), ('Juan', 31), ('María', 28)}








# Procesamiento de datos

# Procesar datos de estudiantes
estudiantes = [
    {"nombre": "Ana", "calificacion": 85},
    {"nombre": "Juan", "calificacion": 92},
    {"nombre": "María", "calificacion": 78}
]

# Crear diccionario nombre -> calificación
calificaciones = {est["nombre"]: est["calificacion"] for est in estudiantes}
print(calificaciones)  # {'Ana': 85, 'Juan': 92, 'María': 78}

# Crear conjunto de estudiantes aprobados (calificación >= 80)
aprobados = {est["nombre"] for est in estudiantes if est["calificacion"] >= 80}
print(aprobados)  # {'Ana', 'Juan'}







# Creación de estructuras multidimensionales

# Crear una matriz de 3x4
matriz = [[j + i*4 for j in range(1, 5)] for i in range(3)]
print(matriz)  # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# Crear una matriz de identidad de tamaño n
n = 4
identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print(identidad)  # [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]






# Procesamiento de datos tabulares

# Extraer información específica de una tabla de datos
tabla = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Juan", "edad": 31, "ciudad": "Barcelona"},
    {"nombre": "María", "edad": 28, "ciudad": "Madrid"},
    {"nombre": "Carlos", "edad": 22, "ciudad": "Valencia"}
]

# Nombres de personas mayores de 25 años agrupados por ciudad
por_ciudad = {
    ciudad: [persona["nombre"] for persona in tabla if persona["ciudad"] == ciudad and persona["edad"] > 25]
    for ciudad in {p["ciudad"] for p in tabla}
}
print(por_ciudad)  # {'Madrid': ['Ana', 'María'], 'Barcelona': ['Juan'], 'Valencia': []}
