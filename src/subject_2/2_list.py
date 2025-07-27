# Lista vacía
mi_lista = []

# Lista con elementos
numeros = [1, 2, 3, 4, 5]

# Lista con diferentes tipos de datos
mixta = [1, "Hola", 3.14, True]



frutas = ["manzana", "banana", "cereza", "durazno", "fresa"]

# Acceder al primer elemento (índice 0)
primera_fruta = frutas[0]  # "manzana"

# Acceder al tercer elemento (índice 2)
tercera_fruta = frutas[2]  # "cereza"



# Último elemento (índice -1)
ultima_fruta = frutas[-1]  # "fresa"

# Penúltimo elemento (índice -2)
penultima_fruta = frutas[-2]  # "durazno"





numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obtener elementos del índice 2 al 5 (sin incluir el 6)
sublista1 = numeros[2:6]  # [2, 3, 4, 5]

# Desde el inicio hasta el índice 4 (sin incluirlo)
sublista2 = numeros[:4]  # [0, 1, 2, 3]

# Desde el índice 7 hasta el final
sublista3 = numeros[7:]  # [7, 8, 9]

# Cada segundo elemento de toda la lista
sublista4 = numeros[::2]  # [0, 2, 4, 6, 8]

# Invertir una lista
invertida = numeros[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]




colores = ["rojo", "verde", "azul", "amarillo"]

# Modificar un elemento específico
colores[1] = "esmeralda"  # ["rojo", "esmeralda", "azul", "amarillo"]

# Modificar varios elementos con slicing
colores[2:4] = ["índigo", "violeta"]  # ["rojo", "esmeralda", "índigo", "violeta"]






letras = ["a", "b", "c", "d", "e"]

# Reemplazar 3 elementos con 1 solo
letras[1:4] = ["X"]  # ["a", "X", "e"]

# Reemplazar 1 elemento con 3
numeros = [1, 2, 3]
numeros[1:2] = [10, 20, 30]  # [1, 10, 20, 30, 3]







vocales = ["a", "e"]
vocales += ["i", "o", "u"]  # ["a", "e", "i", "o", "u"]

# Equivalente usando extend()
consonantes = ["b", "c", "d"]
consonantes.extend(["f", "g"])  # ["b", "c", "d", "f", "g"]






lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
combinada = lista1 + lista2  # [1, 2, 3, 4, 5, 6]
# Nota: lista1 y lista2 no se modifican





dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
dias[1:3] = []  # Elimina "Martes" y "Miércoles"
# dias ahora es ["Lunes", "Jueves", "Viernes"]







animales = ["perro", "gato", "conejo", "tortuga"]

# Verificar si un elemento está en la lista
tiene_gato = "gato" in animales  # True
tiene_leon = "león" in animales  # False

# Usar en condicionales
if "conejo" in animales:
    print("Hay un conejo en la lista")







# Lista de 2 dimensiones (matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a elementos de la matriz
elemento = matriz[1][2]  # 6 (fila 1, columna 2)

# Modificar un elemento
matriz[0][1] = 20  # Cambia el 2 por 20









# Método 1: usando el método copy()
lista1 = [1, 2, 3]
copia1 = lista1.copy()

# Método 2: usando slicing
copia2 = lista1[:]

# Método 3: usando list()
copia3 = list(lista1)

# Para listas anidadas (copia profunda)
import copy
anidada = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(anidada)








coordenadas = [10, 20, 30]
x, y, z = coordenadas

print(x)  # 10
print(y)  # 20
print(z)  # 30

# Con el operador * para capturar múltiples elementos
primero, *resto = [1, 2, 3, 4, 5]
print(primero)  # 1
print(resto)    # [2, 3, 4, 5]

*inicio, ultimo = [1, 2, 3, 4, 5]
print(inicio)   # [1, 2, 3, 4]
print(ultimo)   # 5






tecnologias = ["Python", "JavaScript", "HTML"]
tecnologias.append("CSS")
print(tecnologias)  # ["Python", "JavaScript", "HTML", "CSS"]


frutas = ["manzana", "pera"]
frutas.extend(["naranja", "uva"])
print(frutas)  # ["manzana", "pera", "naranja", "uva"]

# También funciona con cualquier iterable
letras = ["a", "b"]
letras.extend("cd")  # Extiende con los caracteres del string
print(letras)  # ["a", "b", "c", "d"]


lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

lista1.append([4, 5])  # Añade [4, 5] como un elemento
lista2.extend([4, 5])  # Añade 4 y 5 como elementos individuales

print(lista1)  # [1, 2, 3, [4, 5]]
print(lista2)  # [1, 2, 3, 4, 5]




colores = ["rojo", "verde", "azul"]
colores.insert(1, "amarillo")  # Inserta en el índice 1
print(colores)  # ["rojo", "amarillo", "verde", "azul"]






lenguajes = ["Python", "Java", "C++", "JavaScript"]
eliminado = lenguajes.pop()  # Elimina y devuelve el último elemento
print(eliminado)  # "JavaScript"
print(lenguajes)  # ["Python", "Java", "C++"]



numeros = [10, 20, 30, 40, 50]
eliminado = numeros.pop(2)  # Elimina y devuelve el elemento en el índice 2
print(eliminado)  # 30
print(numeros)  # [10, 20, 40, 50]



# Usando una lista como pila (LIFO: Last In, First Out)
pila = []
pila.append(1)  # Añadir al final
pila.append(2)
pila.append(3)
print(pila)  # [1, 2, 3]

ultimo = pila.pop()  # Sacar del final
print(ultimo)  # 3
print(pila)  # [1, 2]

# Usando una lista como cola (FIFO: First In, First Out)
cola = []
cola.append("primero")
cola.append("segundo")
cola.append("tercero")

primero = cola.pop(0)  # Sacar del principio
print(primero)  # "primero"
print(cola)  # ["segundo", "tercero"]




animales = ["perro", "gato", "conejo", "gato", "tortuga"]
animales.remove("gato")  # Elimina la primera ocurrencia de "gato"
print(animales)  # ["perro", "conejo", "gato", "tortuga"]





numeros = [1, 2, 3, 4, 5]
numeros.clear()
print(numeros)  # []





vocales = ["a", "e", "i", "o", "u", "i"]
indice = vocales.index("i")
print(indice)  # 2 (primera ocurrencia de "i")


# Buscar "i" a partir del índice 3
indice = vocales.index("i", 3)
print(indice)  # 5 (segunda ocurrencia de "i")

# Buscar "e" entre los índices 0 y 2
indice = vocales.index("e", 0, 2)
print(indice)  # 1



texto = list("programación")
frecuencia_a = texto.count("a")
print(frecuencia_a)  # 2







# Ordenar por longitud de palabra
palabras = ["python", "es", "un", "lenguaje", "genial"]
palabras.sort(key=len)
print(palabras)  # ["es", "un", "python", "genial", "lenguaje"]

# Ordenar ignorando mayúsculas/minúsculas
nombres = ["Ana", "carlos", "Berta", "david"]
nombres.sort(key=str.lower)
print(nombres)  # ["Ana", "Berta", "carlos", "david"]






letras = ["a", "b", "c", "d"]
letras.reverse()
print(letras)  # ["d", "c", "b", "a"]






# Eliminar duplicados manteniendo el orden
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sin_duplicados = []
for num in numeros:
    if num not in sin_duplicados:
        sin_duplicados.append(num)
print(sin_duplicados)  # [3, 1, 4, 5, 9, 2, 6]

# Filtrar y transformar elementos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num * 2)
print(pares)  # [4, 8, 12, 16, 20]







matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder al elemento en la segunda fila, tercera columna
elemento = matriz[1][2]  # Resultado: 6

# Acceder a la primera fila completa
primera_fila = matriz[0]  # Resultado: [1, 2, 3]

# Acceder al último elemento de la última fila
ultimo = matriz[-1][-1]  # Resultado: 9








matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Recorrer e imprimir cada elemento
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Elemento en posición [{i}][{j}]: {matriz[i][j]}")

# Alternativa más pythónica usando enumerate
for i, fila in enumerate(matriz):
    for j, elemento in enumerate(fila):
        print(f"Elemento en posición [{i}][{j}]: {elemento}")





# Crear una matriz m×n
def crear_matriz(m, n, valor_inicial=0):
    return [[valor_inicial for _ in range(n)] for _ in range(m)]

# Matriz 2×3 con valor inicial 1
matriz_2x3 = crear_matriz(2, 3, 1)
print(matriz_2x3)  # [[1, 1, 1], [1, 1, 1]]



def sumar_matrices(matriz_a, matriz_b):
    # Verificar que las matrices tengan las mismas dimensiones
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    
    # Crear matriz resultado con las mismas dimensiones
    filas = len(matriz_a)
    columnas = len(matriz_a[0])
    resultado = crear_matriz(filas, columnas)
    
    # Sumar elementos correspondientes
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]
    
    return resultado

# Ejemplo de uso
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
c = sumar_matrices(a, b)
print(c)  # [[6, 8], [10, 12]]






def transponer(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear matriz transpuesta (columnas × filas)
    transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
    
    # Intercambiar filas por columnas
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    
    return transpuesta

# Ejemplo
matriz = [[1, 2, 3], [4, 5, 6]]
transpuesta = transponer(matriz)
print(transpuesta)  # [[1, 4], [2, 5], [3, 6]]









# Matriz 3D (2×2×3)
cubo = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]

# Acceder a elementos
print(cubo[0][1][2])  # 6 (primer "plano", segunda fila, tercer elemento)

# Recorrer un cubo
for i, plano in enumerate(cubo):
    print(f"Plano {i}:")
    for fila in plano:
        print(fila)
    print()








# Datos de ventas por región y trimestre
ventas = [
    ["Norte", 100, 120, 90, 110],
    ["Sur", 80, 95, 100, 120],
    ["Este", 110, 105, 95, 130],
    ["Oeste", 90, 100, 115, 125]
]

# Calcular el total de ventas por región
for region in ventas:
    nombre = region[0]
    total = sum(region[1:])
    print(f"Región {nombre}: {total} unidades")

# Calcular el total de ventas por trimestre
for i in range(1, 5):
    total_trimestre = sum(region[i] for region in ventas)
    print(f"Trimestre {i}: {total_trimestre} unidades")












