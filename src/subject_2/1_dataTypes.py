# Valores que evalúan a False
print(bool(0))            # Entero cero
print(bool(0.0))          # Flotante cero
print(bool(""))           # Cadena vacía
print(bool([]))           # Lista vacía
print(bool({}))           # Diccionario vacío
print(bool(None))         # Valor None

# Todo lo demás evalúa a True
print(bool(1))            # Salida: True
print(bool(-5))           # Salida: True
print(bool("Hola"))       # Salida: True

nombre = "María"
edad = 29
# Usando f-strings (Python 3.6+)
presentación = f"Me llamo {nombre} y tengo {edad} años"
print(presentación)          # Salida: Me llamo María y tengo 29 años

# Expresiones en f-strings
print(f"El año que viene tendré {edad + 1} años")  # Salida: El año que viene tendré 30 años

# Literales numéricos con guiones bajos (Python 3.6+)
millón = 1_000_000
print(millón)                # Salida: 1000000

# Prefijos para sistemas numéricos
binario = 0b1010             # Binario (base 2)
octal = 0o12                 # Octal (base 8)
hexadecimal = 0xFF           # Hexadecimal (base 16)

# Prefijos para cadenas
unicode = u"äöü"             # Cadena Unicode (redundante en Python 3)
raw = r"C:\nueva\carpeta"    # Cadena raw (no procesa escapes como \n)
formato = f"{2 + 2} = 4"     # f-string (Python 3.6+)



texto = "Python es un lenguaje de programación versátil"

# Búsqueda
print(texto.find("lenguaje"))      # 13 (posición donde comienza)
print(texto.find("Java"))          # -1 (no encontrado)
print(texto.index("Python"))       # 0 (como find pero lanza error si no encuentra)
print(texto.count("a"))            # 4 (número de ocurrencias)

# Reemplazo
print(texto.replace("Python", "JavaScript"))  # Reemplaza todas las ocurrencias
print(texto.replace("a", "A", 2))  # Reemplaza solo las 2 primeras ocurrencias



texto = "  python es genial  "

# Manipulación de espacios
print(texto.strip())               # "python es genial" (elimina espacios inicio/fin)
print(texto.lstrip())              # "python es genial  " (elimina espacios inicio)
print(texto.rstrip())              # "  python es genial" (elimina espacios final)

# Manipulación de caso
print(texto.upper())               # "  PYTHON ES GENIAL  "
print(texto.lower())               # "  python es genial  "
print(texto.capitalize())          # "  python es genial  " (primera letra a mayúscula)
print(texto.title())               # "  Python Es Genial  " (primera letra de cada palabra)
print(texto.swapcase())            # "  PYTHON ES GENIAL  " (invierte mayúsculas/minúsculas)

# Alineación y relleno
nombre = "Ana"
print(nombre.ljust(10, '-'))       # "Ana-------" (alinea a izquierda)
print(nombre.rjust(10, '-'))       # "-------Ana" (alinea a derecha)
print(nombre.center(10, '-'))      # "---Ana----" (centra)
print(nombre.zfill(5))             # "00Ana" (rellena con ceros a la izquierda)





texto = "Python,Java,C++,JavaScript"

# División
lenguajes = texto.split(",")       # ['Python', 'Java', 'C++', 'JavaScript']
print(lenguajes)

líneas = "Línea 1\nLínea 2\nLínea 3"
print(líneas.splitlines())         # ['Línea 1', 'Línea 2', 'Línea 3']

# Unión
print(",".join(lenguajes))         # "Python,Java,C++,JavaScript"
print("\n".join(lenguajes))        # Cada lenguaje en una línea





# Método format()
plantilla = "Hola, me llamo {nombre} y tengo {edad} años"
print(plantilla.format(nombre="Carlos", edad=30))

# Especificadores de formato
print("{:.2f}".format(3.14159))    # "3.14" (2 decimales)
print("{:>10}".format("texto"))    # "     texto" (alineación derecha, ancho 10)
print("{:^10}".format("texto"))    # "   texto  " (centrado, ancho 10)
print("{:,}".format(1000000))      # "1,000,000" (separador de miles)

# f-strings (Python 3.6+)
nombre = "Laura"
edad = 28
print(f"Hola, me llamo {nombre} y tengo {edad} años")
print(f"El año que viene tendré {edad + 1} años")
print(f"Pi con 2 decimales: {3.14159:.2f}")





# Codificación
texto = "Hola, mundo"
bytes_utf8 = texto.encode('utf-8')
print(bytes_utf8)                  # b'Hola, mundo'

# Decodificación
texto_recuperado = bytes_utf8.decode('utf-8')
print(texto_recuperado)            # "Hola, mundo"

# Manejo de caracteres especiales
texto_con_acentos = "café"
bytes_latin1 = texto_con_acentos.encode('latin-1')
print(bytes_latin1)                # b'caf\xe9'








# Parámetros adicionales para int()
binario_a_int = int("1010", 2)     # 10 (convierte desde binario)
hex_a_int = int("1A", 16)          # 26 (convierte desde hexadecimal)

# Parámetros para float()
notación_científica = float("1e-3") # 0.001 (notación científica)

# Parámetros para str()
personalizado = str([1, 2, 3])     # "[1, 2, 3]" (convierte cualquier objeto a su representación)








# Entero a flotante en operaciones mixtas
resultado = 5 + 3.14               # 8.14 (int se convierte a float)

# Número a booleano en contextos condicionales
if 42:
    print("Los números distintos de 0 son True")  # Se imprime

# Número a cadena en concatenación (requiere conversión explícita)
try:
    mensaje = "Tengo " + 25 + " años"  # Error: no se puede concatenar str e int
except TypeError as e:
    print(f"Error: {e}")  # Error: can only concatenate str (not "int") to str

# Forma correcta
mensaje = "Tengo " + str(25) + " años"  # "Tengo 25 años"
# O mejor aún, usando f-strings
edad = 25
mensaje = f"Tengo {edad} años"     # "Tengo 25 años"








valor = 42

# Verificación básica de tipo
print(isinstance(valor, int))      # True
print(isinstance(valor, float))    # False
print(isinstance(valor, (int, float)))  # True (comprueba si es alguno de los tipos)

# Verificación con herencia
print(isinstance(True, int))       # True (bool hereda de int)
print(isinstance(3.14, (int, float)))  # True (es float)

# Verificación con tipos personalizados
class MiClase:
    pass

obj = MiClase()
print(isinstance(obj, MiClase))    # True




def duplicar(valor):
    """Duplica un valor numérico o repite una cadena."""
    if isinstance(valor, (int, float)):
        return valor * 2
    elif isinstance(valor, str):
        return valor * 2
    else:
        raise TypeError("Solo se aceptan números o cadenas")

print(duplicar(5))         # 10
print(duplicar(3.14))      # 6.28
print(duplicar("abc"))     # "abcabc"








# Obtener el tipo de un objeto
print(type(42))            # <class 'int'>
print(type(3.14))          # <class 'float'>
print(type("Hola"))        # <class 'str'>
print(type(True))          # <class 'bool'>

# Comparación con tipos
print(type(42) is int)     # True
print(type(True) is int)   # False (a diferencia de isinstance())
print(type(True) is bool)  # True







# Diferencia con herencia
print(isinstance(True, int))  # True (bool hereda de int)
print(type(True) is int)      # False (el tipo exacto es bool, no int)

# Ejemplo con clases personalizadas
class Padre:
    pass

class Hijo(Padre):
    pass

obj = Hijo()
print(isinstance(obj, Padre))  # True (obj es instancia de Hijo, que hereda de Padre)
print(type(obj) is Padre)      # False (el tipo exacto es Hijo)










# Función que acepta diferentes tipos de entrada
def procesar_entrada(valor):
    if isinstance(valor, str):
        # Intentar convertir a número si es posible
        if valor.isdigit():
            return int(valor)
        try:
            return float(valor)
        except ValueError:
            return valor.upper()  # Si no es número, convertir a mayúsculas
    elif isinstance(valor, (int, float)):
        return valor * 2
    else:
        return None

print(procesar_entrada("42"))      # 42 (int)
print(procesar_entrada("3.14"))    # 3.14 (float)
print(procesar_entrada("hola"))    # "HOLA" (str en mayúsculas)
print(procesar_entrada(10))        # 20 (int duplicado)






def calcular_área_rectángulo(base, altura):
    # Verificar que los parámetros son numéricos
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Base y altura deben ser valores numéricos")
    
    # Verificar que son positivos
    if base <= 0 or altura <= 0:
        raise ValueError("Base y altura deben ser valores positivos")
    
    return base * altura

# Uso correcto
print(calcular_área_rectángulo(5, 3))      # 15

# Uso incorrecto
try:
    calcular_área_rectángulo("5", 3)
except TypeError as e:
    print(f"Error: {e}")  # Error: Base y altura deben ser valores numéricos




# Verificación de relaciones de herencia
print(issubclass(bool, int))       # True (bool hereda de int)
print(issubclass(float, int))      # False (float no hereda de int)
print(issubclass(bool, bool))      # True (una clase es subclase de sí misma)

# Con clases personalizadas
class Animal:
    pass

class Perro(Animal):
    pass

class Gato(Animal):
    pass

print(issubclass(Perro, Animal))   # True
print(issubclass(Gato, Perro))     # False



x = 42
y = 42
z = x

print(id(x))  # Por ejemplo: 140715689587792
print(id(y))  # Podría ser el mismo o diferente, dependiendo de la implementación
print(id(z))  # Mismo id que x, ya que z apunta al mismo objeto




# Con objetos inmutables
x = 10
y = x

print(id(x) == id(y))  # True, ambos apuntan al mismo objeto

x += 5  # Esto crea un nuevo objeto, no modifica el existente
print(x)  # 15
print(y)  # 10 - 'y' sigue apuntando al objeto original

print(id(x) == id(y))  # False, ahora apuntan a objetos diferentes







# Con objetos mutables
lista_a = [1, 2, 3]
lista_b = lista_a

print(id(lista_a) == id(lista_b))  # True, ambos apuntan al mismo objeto

lista_a.append(4)  # Modifica el objeto existente
print(lista_a)  # [1, 2, 3, 4]
print(lista_b)  # [1, 2, 3, 4] - 'lista_b' refleja los cambios

print(id(lista_a) == id(lista_b))  # True, siguen apuntando al mismo objeto



# Copia superficial (shallow copy)
original = [1, 2, [3, 4]]
copia1 = original.copy()  # Método específico de listas
copia2 = original[:]      # Slicing (rebanado)
copia3 = list(original)   # Constructor de lista

# Todas son copias independientes del objeto original
copia1.append(5)
print(original)  # [1, 2, [3, 4]] - No se ve afectado

# PERO: los objetos anidados siguen siendo compartidos
copia1[2].append(5)
print(original)  # [1, 2, [3, 4, 5]] - ¡El objeto anidado sí se ve afectado!


import copy

original = [1, 2, [3, 4]]
copia_profunda = copy.deepcopy(original)

# Ahora los objetos anidados también son independientes
copia_profunda[2].append(5)
print(original)      # [1, 2, [3, 4]] - No se ve afectado
print(copia_profunda)  # [1, 2, [3, 4, 5]]


def modificar_lista(lista):
    lista.append(4)  # Modifica el objeto original
    
def reemplazar_lista(lista):
    lista = [7, 8, 9]  # Crea una nueva referencia local, no afecta al original
    
mi_lista = [1, 2, 3]

modificar_lista(mi_lista)
print(mi_lista)  # [1, 2, 3, 4] - La lista original se modificó

reemplazar_lista(mi_lista)
print(mi_lista)  # [1, 2, 3, 4] - La lista original no cambió





x = [1, 2, 3]  # Se crea un objeto lista
x = "hola"     # La lista original ya no tiene referencias
               # y eventualmente será eliminada por el recolector de basura


import sys

a = [1, 2, 3]
b = a
c = a

# El +1 es porque getrefcount() crea una referencia temporal adicional
print(sys.getrefcount(a))  # 4 (a, b, c, más la referencia temporal)




# Potencialmente peligroso
def añadir_elemento(elemento, lista=[]):  # ¡La lista por defecto se crea una sola vez!
    lista.append(elemento)
    return lista

print(añadir_elemento(1))  # [1]
print(añadir_elemento(2))  # [1, 2] - ¡La lista se comparte entre llamadas!

# Mejor alternativa
def añadir_elemento_seguro(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista








a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True - Mismo valor
print(a is b)  # False - Objetos diferentes
print(a is c)  # True - Mismo objeto














