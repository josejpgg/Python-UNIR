# enumerate()

frutas = ["manzana", "banana", "cereza", "durazno"]

# Sin enumerate tendríamos que hacer esto:
for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}")

# Con enumerate es más elegante:
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")





# Comenzando desde 1 en lugar de 0
for indice, fruta in enumerate(frutas, start=1):
    print(f"Fruta #{indice}: {fruta}")






# zip()

nombres = ["Ana", "Carlos", "Elena"]
edades = [28, 32, 25]
ciudades = ["Madrid", "Barcelona", "Valencia"]

# Combinamos las tres listas
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")







# Si necesitamos que zip() continúe hasta agotar el iterable más largo, podemos usar zip_longest() del módulo itertools:

from itertools import zip_longest

numeros = [1, 2, 3, 4, 5]
letras = ['a', 'b', 'c']

# El parámetro fillvalue especifica qué usar para los valores faltantes
for num, letra in zip_longest(numeros, letras, fillvalue='?'):
    print(f"{num}-{letra}")
# Imprime: 1-a, 2-b, 3-c, 4-?, 5-?







claves = ['nombre', 'edad', 'profesión']
valores = ['Laura', 29, 'Ingeniera']

# Crear un diccionario combinando claves y valores
persona = dict(zip(claves, valores))
print(persona)  # {'nombre': 'Laura', 'edad': 29, 'profesión': 'Ingeniera'}







productos = ["Laptop", "Teléfono", "Tablet"]
precios = [1200, 800, 350]
stock = [5, 25, 10]

# Recorrer tres listas con índice
for i, (producto, precio, cantidad) in enumerate(zip(productos, precios, stock), 1):
    print(f"Ítem #{i}: {producto} - ${precio} ({cantidad} unidades disponibles)")










matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transponer la matriz
transpuesta = list(zip(*matriz))
print(transpuesta)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]













# Crear un iterador zip sin consumir memoria
nombres = ["Ana", "Carlos", "Elena"]
edades = [28, 32, 25]

# Esto no crea una lista en memoria, solo un iterador
combinados = zip(nombres, edades)

# Los valores se generan solo cuando se iteran
for nombre, edad in combinados:
    print(f"{nombre}: {edad}")

# Si necesitamos una lista, podemos convertirlo explícitamente
lista_combinada = list(zip(nombres, edades))









# map()

# map(función, iterable, [iterable2, iterable3, ...])


# Convertir cada número a su cuadrado
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x**2, numeros)

# map devuelve un objeto iterable, no una lista
print(cuadrados)  # <map object at 0x7f8b6d5b9a90>

# Convertir a lista para ver los resultados
lista_cuadrados = list(cuadrados)
print(lista_cuadrados)  # [1, 4, 9, 16, 25]








# Usando una función incorporada
numeros_texto = ["1", "2", "3", "4", "5"]
numeros = list(map(int, numeros_texto))
print(numeros)  # [1, 2, 3, 4, 5]

# Usando una función definida previamente
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

temperaturas_c = [0, 10, 20, 30, 40]
temperaturas_f = list(map(celsius_a_fahrenheit, temperaturas_c))
print(temperaturas_f)  # [32.0, 50.0, 68.0, 86.0, 104.0]














# Sumar elementos correspondientes de dos listas
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]
sumas = list(map(lambda x, y: x + y, lista1, lista2))
print(sumas)  # [11, 22, 33, 44]

# Combinar elementos de tres listas
nombres = ["Ana", "Carlos", "Elena"]
apellidos = ["García", "López", "Martínez"]
edades = [28, 35, 42]

# Crear cadenas formateadas con datos de las tres listas
resultados = list(map(
    lambda nombre, apellido, edad: f"{nombre} {apellido}, {edad} años",
    nombres, apellidos, edades
))
print(resultados)
# ['Ana García, 28 años', 'Carlos López, 35 años', 'Elena Martínez, 42 años']











# Convertir valores de un diccionario a mayúsculas
datos = {"nombre": "juan", "ciudad": "madrid", "profesion": "ingeniero"}
datos_mayusculas = dict(zip(
    datos.keys(),
    map(lambda x: x.upper(), datos.values())
))
print(datos_mayusculas)  # {'nombre': 'JUAN', 'ciudad': 'MADRID', 'profesion': 'INGENIERO'}











# Lista de diccionarios con datos de productos
productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Teléfono", "precio": 800, "stock": 25},
    {"nombre": "Tablet", "precio": 350, "stock": 10}
]

# Calcular el valor total de inventario para cada producto
valores_inventario = list(map(
    lambda producto: {
        "nombre": producto["nombre"],
        "valor_total": producto["precio"] * producto["stock"]
    },
    productos
))
print(valores_inventario)
# [{'nombre': 'Laptop', 'valor_total': 6000}, 
#  {'nombre': 'Teléfono', 'valor_total': 20000}, 
#  {'nombre': 'Tablet', 'valor_total': 3500}]











# Limpiar y validar datos de entrada
datos_usuario = [" Ana ", "carlos@email.com ", " 28 ", "Madrid "]

# Eliminar espacios y normalizar
datos_limpios = list(map(lambda x: x.strip(), datos_usuario))
print(datos_limpios)  # ['Ana', 'carlos@email.com', '28', 'Madrid']

# Validar tipos de datos
def validar_entero(valor):
    try:
        return int(valor)
    except ValueError:
        return None

entradas = ["42", "abc", "7.5", "100"]
numeros_validados = list(map(validar_entero, entradas))
print(numeros_validados)  # [42, None, None, 100]














numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x**2, numeros)

# Primera iteración
for cuadrado in cuadrados:
    print(cuadrado, end=" ")  # 1 4 9 16 25

print()

# Segunda iteración - no produce resultados porque el iterador ya se consumió
for cuadrado in cuadrados:
    print(cuadrado, end=" ")  # No imprime nada

# Solución: crear un nuevo objeto map o convertir a lista
cuadrados = list(map(lambda x: x**2, numeros))
for cuadrado in cuadrados:
    print(cuadrado, end=" ")  # 1 4 9 16 25










# filter()

# filter(función, iterable)



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda x: x % 2 == 0, numeros)

print(pares)  # <filter object at 0x7f8b6d5b9a90>

# Convertir a lista para ver los resultados
lista_pares = list(pares)
print(lista_pares)  # [2, 4, 6, 8, 10]











def es_primo(n):
    """Verifica si un número es primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Filtrar números primos de una lista
numeros = range(1, 20)
primos = list(filter(es_primo, numeros))
print(primos)  # [2, 3, 5, 7, 11, 13, 17, 19]












# Filtrar valores falsy (None, 0, "", [], {}, etc.)
valores_mixtos = [0, 1, "", "texto", [], [1, 2], None, True, False, {}]
valores_verdaderos = list(filter(None, valores_mixtos))
print(valores_verdaderos)  # [1, 'texto', [1, 2], True]










# Lista de productos
productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Teléfono", "precio": 800, "stock": 0},
    {"nombre": "Tablet", "precio": 350, "stock": 10},
    {"nombre": "Auriculares", "precio": 150, "stock": 0},
    {"nombre": "Monitor", "precio": 400, "stock": 3}
]

# Filtrar productos en stock
en_stock = list(filter(lambda p: p["stock"] > 0, productos))
print("Productos en stock:")
for producto in en_stock:
    print(f"- {producto['nombre']} (${producto['precio']})")

# Filtrar productos premium (precio > 500)
premium = list(filter(lambda p: p["precio"] > 500, productos))
print("\nProductos premium:")
for producto in premium:
    print(f"- {producto['nombre']} (${producto['precio']})")










import re

# Lista de correos electrónicos
correos = [
    "usuario@ejemplo.com",
    "nombre.apellido@empresa.es",
    "contacto@sitio.co.uk",
    "no-es-un-correo",
    "otro@dominio",
    "correo@valido.org"
]

# Patrón simple para validar correos electrónicos
patron = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

# Filtrar correos válidos
correos_validos = list(filter(
    lambda c: patron.match(c) is not None,
    correos
))
print(correos_validos)
# ['usuario@ejemplo.com', 'nombre.apellido@empresa.es', 'contacto@sitio.co.uk', 'correo@valido.org']













from itertools import count

# Generar números primos usando filter con una secuencia infinita
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Crear un iterador de números primos
# count() genera números infinitamente, filter selecciona solo los primos
primos = filter(es_primo, count(1))

# Obtener los primeros 10 números primos
primeros_primos = []
for _ in range(10):
    primeros_primos.append(next(primos))

print(primeros_primos)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]




















# reduce()
from functools import reduce
# reduce(función, iterable[, inicial])






from functools import reduce

# Sumar todos los números de una lista
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda acum, num: acum + num, numeros)
print(suma)  # 15

# Se toma el primer elemento (1) como valor inicial del acumulador
# Se aplica la función al acumulador y al segundo elemento: 1 + 2 = 3
# El resultado (3) se convierte en el nuevo acumulador
# Se aplica la función al acumulador y al tercer elemento: 3 + 3 = 6
# El proceso continúa hasta procesar todos los elementos
# El valor final del acumulador (15) es el resultado de reduce()


# Sumar todos los números partiendo de 10
suma_desde_10 = reduce(lambda acum, num: acum + num, numeros, 10)
print(suma_desde_10)  # 25 (10 + 1 + 2 + 3 + 4 + 5)










from functools import reduce
import operator  # Módulo con operadores como funciones

numeros = [1, 2, 3, 4, 5]

# Suma (equivalente a sum())
suma = reduce(operator.add, numeros)
print(f"Suma: {suma}")  # 15

# Producto (equivalente a math.prod() en Python 3.8+)
producto = reduce(operator.mul, numeros)
print(f"Producto: {producto}")  # 120

# Máximo (equivalente a max())
maximo = reduce(lambda a, b: a if a > b else b, numeros)
print(f"Máximo: {maximo}")  # 5

# Mínimo (equivalente a min())
minimo = reduce(lambda a, b: a if a < b else b, numeros)
print(f"Mínimo: {minimo}")  # 1













# Concatenar listas
listas = [[1, 2], [3, 4], [5, 6]]
lista_plana = reduce(lambda x, y: x + y, listas)
print(lista_plana)  # [1, 2, 3, 4, 5, 6]

# Concatenar cadenas
palabras = ["Python", "es", "un", "lenguaje", "genial"]
frase = reduce(lambda x, y: x + " " + y, palabras)
print(frase)  # "Python es un lenguaje genial"









# Definir algunas funciones simples
def duplicar(x):
    return x * 2

def sumar_cinco(x):
    return x + 5

def cuadrado(x):
    return x ** 2

# Componer funciones con reduce
funciones = [duplicar, sumar_cinco, cuadrado]
valor_inicial = 3

# Aplicar cada función en secuencia: cuadrado(sumar_cinco(duplicar(3)))
resultado = reduce(lambda valor, funcion: funcion(valor), funciones, valor_inicial)
print(resultado)  # 121 = (3*2 + 5)^2 = 11^2 = 121









# Datos de ventas mensuales por producto
ventas = [
    {"producto": "Laptop", "cantidad": 5, "precio": 1200},
    {"producto": "Teléfono", "cantidad": 10, "precio": 800},
    {"producto": "Tablet", "cantidad": 7, "precio": 350},
    {"producto": "Auriculares", "cantidad": 15, "precio": 150},
    {"producto": "Monitor", "cantidad": 3, "precio": 400}
]

# Calcular el valor total de ventas
total_ventas = reduce(
    lambda acum, item: acum + (item["cantidad"] * item["precio"]),
    ventas,
    0
)
print(f"Total de ventas: ${total_ventas}")  # $17050

# Encontrar el producto más vendido
producto_mas_vendido = reduce(
    lambda max_prod, item: item if item["cantidad"] > max_prod["cantidad"] else max_prod,
    ventas[1:],  # Empezamos desde el segundo elemento
    ventas[0]    # El primer elemento es el valor inicial
)
print(f"Producto más vendido: {producto_mas_vendido['producto']} ({producto_mas_vendido['cantidad']} unidades)")
# Auriculares (15 unidades)

















from functools import reduce
import re

# Texto de ejemplo
texto = """
Python es un lenguaje de programación interpretado cuya filosofía hace 
hincapié en la legibilidad de su código. Se trata de un lenguaje de programación 
multiparadigma, ya que soporta orientación a objetos, programación imperativa y, 
en menor medida, programación funcional. Es un lenguaje interpretado, dinámico 
y multiplataforma.
"""

# Limpiar y dividir el texto en palabras
palabras = re.findall(r'\b\w+\b', texto.lower())

# Contar frecuencia de cada palabra
frecuencia_palabras = reduce(
    lambda acum, palabra: {
        **acum,
        palabra: acum.get(palabra, 0) + 1
    },
    palabras,
    {}
)

# Encontrar las 5 palabras más frecuentes
palabras_ordenadas = sorted(
    frecuencia_palabras.items(),
    key=lambda x: x[1],
    reverse=True
)[:5]

print("Las 5 palabras más frecuentes:")
for palabra, frecuencia in palabras_ordenadas:
    print(f"- '{palabra}': {frecuencia} veces")
