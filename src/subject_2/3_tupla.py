# Creamos una tupla
coordenadas = (10, 20)

# Esto generará un error
# TypeError: 'tuple' object does not support item assignment
# coordenadas[0] = 15





import sys

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (1, 2, 3, 4, 5)

# Comparación de tamaño en bytes
print(f"Tamaño de la lista: {sys.getsizeof(mi_lista)} bytes") # 104 bytes
print(f"Tamaño de la tupla: {sys.getsizeof(mi_tupla)} bytes") # 80 bytes





import timeit

# Medición de tiempo para crear una lista vs una tupla
tiempo_lista = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tiempo_tupla = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print(f"Tiempo para crear 1,000,000 de listas: {tiempo_lista:.6f} segundos")
print(f"Tiempo para crear 1,000,000 de tuplas: {tiempo_tupla:.6f} segundos")





def obtener_dimensiones_imagen(ruta_imagen):
    # Código para procesar la imagen
    # ...
    return (1920, 1080)  # Ancho, alto

# Desempaquetado directo del retorno
ancho, alto = obtener_dimensiones_imagen("foto.jpg")
print(f"La imagen tiene {ancho}x{alto} píxeles")








# Tupla que contiene una lista
datos = (1, 2, [3, 4])

# No podemos cambiar la estructura de la tupla
# datos[0] = 5  # Esto generaría error

# Pero podemos modificar el contenido de la lista dentro de la tupla
datos[2].append(5)
print(datos)  # Imprime: (1, 2, [3, 4, 5])









# Tupla con elementos
colores = ("rojo", "verde", "azul")

# Tupla vacía
tupla_vacia = ()


# Tupla creada solo con comas
puntos = 10, 20, 30
print(type(puntos))  # <class 'tuple'>


# Incorrecto - Python lo interpreta como un entero entre paréntesis
no_es_tupla = (42)
print(type(no_es_tupla))  # <class 'int'>

# Correcto - La coma indica que es una tupla
tupla_singleton = (42,)
print(type(tupla_singleton))  # <class 'tuple'>

# También funciona sin paréntesis
otra_singleton = 42,
print(type(otra_singleton))  # <class 'tuple'>


# Desde una lista
numeros = tuple([1, 2, 3, 4])

# Desde una cadena
letras = tuple("Python")
print(letras)  # ('P', 'y', 't', 'h', 'o', 'n')

# Desde un rango
secuencia = tuple(range(5))
print(secuencia)  # (0, 1, 2, 3, 4)

# Matriz como tupla de tuplas
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Tupla heterogénea
datos_mixtos = (42, "Python", True, 3.14)



dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# Acceso al primer elemento (índice 0)
primer_dia = dias[0]
print(primer_dia)  # Lunes

# Acceso al tercer elemento (índice 2)
tercer_dia = dias[2]
print(tercer_dia)  # Miércoles


dias_laborables = dias[0:5]  # Desde el índice 0 hasta el 4 (sin incluir el 5)
print(dias_laborables)  # ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes')

# Forma abreviada para el mismo resultado
dias_laborables = dias[:5]

# Fin de semana
fin_de_semana = dias[5:7]  # o simplemente dias[5:]
print(fin_de_semana)  # ('Sábado', 'Domingo')

# Slicing con paso
dias_alternos = dias[::2]  # Toma elementos saltando de 2 en 2
print(dias_alternos)  # ('Lunes', 'Miércoles', 'Viernes', 'Domingo')

# Slicing inverso
dias_inverso = dias[::-1]  # Invierte el orden de la tupla
print(dias_inverso)  # ('Domingo', 'Sábado', 'Viernes', 'Jueves', 'Miércoles', 'Martes', 'Lunes')






frutas = ("manzana", "naranja", "plátano", "uva")

# Verificar si un elemento existe
tiene_naranja = "naranja" in frutas
print(tiene_naranja)  # True

tiene_pera = "pera" in frutas
print(tiene_pera)  # False

# Uso en condicionales
fruta_buscar = "plátano"
if fruta_buscar in frutas:
    print(f"Tenemos {fruta_buscar} en stock")
else:
    print(f"No tenemos {fruta_buscar} en stock")









# Iteración básica
colores = ("rojo", "verde", "azul", "amarillo")
for color in colores:
    print(f"Color: {color}")

# Iteración con índice usando enumerate()
for indice, color in enumerate(colores):
    print(f"Posición {indice}: {color}")








# De lista a tupla
lista_numeros = [10, 20, 30, 40]
tupla_numeros = tuple(lista_numeros)

# De tupla a lista
colores_tupla = ("rojo", "verde", "azul")
colores_lista = list(colores_tupla)
colores_lista.append("amarillo")  # Ahora podemos modificarla







patron = (1, 2) * 3
print(patron)  # (1, 2, 1, 2, 1, 2)





tupla_a = (1, 2, 3)
tupla_b = (1, 2, 4)
tupla_c = (1, 2, 3)

print(tupla_a == tupla_c)  # True
print(tupla_a < tupla_b)   # True (compara el primer elemento diferente: 3 < 4)




tupla_a = (1, 2, 3)
tupla_b = (1, 2, 4)
tupla_c = (1, 2, 3)

print(tupla_a == tupla_c)  # True
print(tupla_a < tupla_b)   # True (compara el primer elemento)










# Ejemplo para probar en VS Code
def analizar_datos(valores):
    minimo = min(valores)
    maximo = max(valores)
    promedio = sum(valores) / len(valores)
    return (minimo, maximo, promedio)

# Llamada a la función y desempaquetado
datos = (4, 7, 2, 9, 5, 1, 8)
min_val, max_val, prom = analizar_datos(datos)

print(f"Mínimo: {min_val}, Máximo: {max_val}, Promedio: {prom:.2f}")









# Tupla con información de un producto
producto = ("Laptop", 1299.99, "Electrónica")

# Desempaquetado básico
nombre, precio, categoria = producto

print(nombre)     # Laptop
print(precio)     # 1299.99
print(categoria)  # Electrónica




coordenadas = (10, 20, 30)  # Tupla con 3 elementos

# Esto generará un error: ValueError: too many values to unpack
# x, y = coordenadas

# Esto también generará un error: ValueError: not enough values to unpack
# x, y, z, w = coordenadas








# Tupla con resultados de una competencia
resultados = ("Ana", "Carlos", "Berta", "David", "Elena")

# Desempaquetado con operador asterisco
ganador, segundo, *resto = resultados

print(f"Oro: {ganador}")    # Oro: Ana
print(f"Plata: {segundo}")  # Plata: Carlos
print(f"Otros: {resto}")    # Otros: ['Berta', 'David', 'Elena']







# Al inicio
*primeros, ultimo = resultados
print(primeros)  # ['Ana', 'Carlos', 'Berta', 'David']
print(ultimo)    # Elena

# En medio
primero, *intermedios, ultimo = resultados
print(primero)      # Ana
print(intermedios)  # ['Carlos', 'Berta', 'David']
print(ultimo)       # Elena





dupla = (1, 2)
a, *b = dupla
print(b)  # [2]

solo_uno = (42,)
primero, *resto = solo_uno
print(resto)  # [] (lista vacía)





# Información de estudiante con datos anidados
estudiante = ("María López", (9.5, 8.7, 9.2), "Informática")

# Desempaquetado con estructura anidada
nombre, (nota1, nota2, nota3), carrera = estudiante

print(nombre)   # María López
print(nota1)    # 9.5
print(nota2)    # 8.7
print(nota3)    # 9.2
print(carrera)  # Informática







calificaciones = {"Matemáticas": 95, "Historia": 88, "Programación": 100}

# Desempaquetado de clave-valor
for asignatura, nota in calificaciones.items():
    print(f"{asignatura}: {nota}")










def estadisticas(numeros):
    """Calcula estadísticas básicas de una secuencia de números."""
    return min(numeros), max(numeros), sum(numeros)/len(numeros)

datos = [4, 7, 2, 9, 5, 1, 8]
minimo, maximo, promedio = estadisticas(datos)

print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Promedio: {promedio:.2f}")










# Solo nos interesa el valor máximo
_, maximo, _ = estadisticas(datos)
print(f"El valor máximo es: {maximo}")

# Ignorar múltiples valores con el operador asterisco
primero, *_, ultimo = range(1, 10)
print(f"Primero: {primero}, Último: {ultimo}")  # Primero: 1, Último: 9













