# Contador en un bucle
total = 0
for numero in range(1, 6):
    total += numero
    print(f"Sumando {numero}: total actual = {total}")
print(f"Suma final: {total}")  # 15




# Construcción de una lista de cuadrados
cuadrados = []
for i in range(1, 6):
    cuadrados.append(i ** 2)
    
# Alternativa con +=
cuadrados_alt = []
for i in range(1, 6):
    cuadrados_alt += [i ** 2]
    
print(f"cuadrados: {cuadrados}")
print(f"cuadrados_alt: {cuadrados_alt}")





# Construcción de una cadena formateada
reporte = ""
datos = [("Manzanas", 5), ("Naranjas", 3), ("Plátanos", 2)]

for fruta, cantidad in datos:
    reporte += f"{fruta}: {cantidad} unidades\n"
    
print(reporte)







# Ejemplo de rendimiento con cadenas largas
import time

# Método 1: Concatenación repetida
inicio = time.time()
resultado1 = ""
for i in range(10000):
    resultado1 = resultado1 + str(i)
tiempo1 = time.time() - inicio

# Método 2: Operador +=
inicio = time.time()
resultado2 = ""
for i in range(10000):
    resultado2 += str(i)
tiempo2 = time.time() - inicio

print(f"Tiempo con concatenación normal: {tiempo1:.6f} segundos")
print(f"Tiempo con operador +=: {tiempo2:.6f} segundos")






# Método 3: join (más eficiente para muchas concatenaciones)
inicio = time.time()
partes = []
for i in range(10000):
    partes.append(str(i))
resultado3 = "".join(partes)
tiempo3 = time.time() - inicio

print(f"Tiempo con join: {tiempo3:.6f} segundos")













# Ejemplos de operadores de comparación
a = 10
b = 5
c = 10

print(f"a == c: {a == c}")  # True
print(f"a != b: {a != b}")  # True
print(f"a > b: {a > b}")    # True
print(f"a < b: {a < b}")    # False
print(f"a >= c: {a >= c}")  # True
print(f"b <= a: {b <= a}")  # True











# Encadenamiento de operadores de comparación
x = 15

# Verifica si x está entre 10 y 20
resultado = 10 < x < 20
print(f"¿x está entre 10 y 20?: {resultado}")  # True

# Equivalente a: (5 <= x) and (x <= 25)
resultado = 5 <= x <= 25
print(f"¿x está entre 5 y 25?: {resultado}")  # True














# Comparación de números
print(f"5 < 5.5: {5 < 5.5}")  # True

# Comparación de cadenas (orden lexicográfico)
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # True
print(f"'Python' < 'python': {'Python' < 'python'}")  # True (mayúsculas antes que minúsculas)

# Comparación de listas (elemento por elemento)
print(f"[1, 2] < [1, 3]: {[1, 2] < [1, 3]}")  # True
print(f"[1, 2, 3] < [1, 2]: {[1, 2, 3] < [1, 2]}")  # False











# Ejemplos de operadores lógicos
x = 8
y = 12

# Operador and
resultado = x > 5 and y < 15
print(f"x > 5 and y < 15: {resultado}")  # True

# Operador or
resultado = x > 10 or y > 10
print(f"x > 10 or y > 10: {resultado}")  # True

# Operador not
resultado = not (x > 10)
print(f"not (x > 10): {resultado}")  # True












# Demostración de evaluación de cortocircuito

def func1():
    print("Evaluando func1()")
    return False

def func2():
    print("Evaluando func2()")
    return True

# Con and, func2() no se evalúa
print("\nUsando and:")
resultado = func1() and func2()
print(f"Resultado: {resultado}")

# Con or, func2() sí se evalúa
print("\nUsando or:")
resultado = func1() or func2()
print(f"Resultado: {resultado}")












# Uso práctico de la evaluación de cortocircuito
lista = []

# Evita IndexError verificando primero si la lista tiene elementos
if len(lista) > 0 and lista[0] == "Python":
    print("El primer elemento es Python")
else:
    print("La lista está vacía o el primer elemento no es Python")













# Ejemplos de valores truthy y falsy
elementos = []
nombre = ""
numero = 0
objeto = None

# Verificación de valores no vacíos
if not elementos:
    print("La lista está vacía")

if nombre:
    print("El nombre no está vacío")
else:
    print("El nombre está vacío")

# Verificación compacta con or para valores por defecto
valor = numero or 10
print(f"Valor (con or): {valor}")  # 10, porque 0 es falsy

# Verificación de None
resultado = objeto or "Valor por defecto"
print(f"Resultado: {resultado}")  # "Valor por defecto"












# Diferencia entre == e is
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # True (mismo contenido)
print(f"a is b: {a is b}")  # False (diferentes objetos)
print(f"a is c: {a is c}")  # True (mismo objeto)

# Uso común con None
valor = None
print(f"valor is None: {valor is None}")  # True












edad = int(input("Introduce tu edad: "))
tiene_permiso = input("¿Tienes permiso parental? (s/n): ").lower() == 's'

if (13 <= edad < 18 and tiene_permiso) or edad >= 18:
    print("Puedes acceder al contenido")
else:
    print("Acceso denegado")












a = 60  # 0011 1100 en binario
b = 13  # 0000 1101 en binario

# Visualización en binario para mejor comprensión
print(f"a en binario: {bin(a)}")
print(f"b en binario: {bin(b)}")

# AND bit a bit: 1 si ambos bits son 1, 0 en caso contrario
resultado = a & b  # 0000 1100 (12 en decimal)
print(f"a & b: {resultado} ({bin(resultado)})")

# OR bit a bit: 1 si al menos uno de los bits es 1, 0 en caso contrario
resultado = a | b  # 0011 1101 (61 en decimal)
print(f"a | b: {resultado} ({bin(resultado)})")

# XOR bit a bit: 1 si los bits son diferentes, 0 si son iguales
resultado = a ^ b  # 0011 0001 (49 en decimal)
print(f"a ^ b: {resultado} ({bin(resultado)})")

# NOT bit a bit: invierte todos los bits
resultado = ~a  # -61 en decimal (debido a la representación de complemento a dos)
print(f"~a: {resultado} ({bin(resultado)})")







c = 8  # 0000 1000 en binario

# Desplazamiento a la izquierda: multiplica por 2^n
resultado = c << 2  # 0010 0000 (32 en decimal)
print(f"c << 2: {resultado} ({bin(resultado)})")  # Equivale a c * (2^2)

# Desplazamiento a la derecha: divide por 2^n
resultado = c >> 1  # 0000 0100 (4 en decimal)
print(f"c >> 1: {resultado} ({bin(resultado)})")  # Equivale a c // (2^1)









# Definición de flags usando constantes bit a bit
LEER    = 0b0001  # 1
ESCRIBIR = 0b0010  # 2
EJECUTAR = 0b0100  # 4
ELIMINAR = 0b1000  # 8

# Asignar permisos combinando flags
permisos_usuario = LEER | ESCRIBIR  # 0011 (3)

# Verificar permisos
puede_leer = permisos_usuario & LEER > 0
puede_ejecutar = permisos_usuario & EJECUTAR > 0

print(f"¿Puede leer?: {puede_leer}")        # True
print(f"¿Puede ejecutar?: {puede_ejecutar}")  # False

# Agregar un permiso
permisos_usuario |= EJECUTAR  # Ahora es 0111 (7)
print(f"Permisos actualizados: {bin(permisos_usuario)}")

# Quitar un permiso
permisos_usuario &= ~ESCRIBIR  # Quita el permiso de escritura
print(f"Después de quitar ESCRIBIR: {bin(permisos_usuario)}")











# Representar un tablero de ajedrez (8x8) usando solo 64 bits
tablero = 0

# Colocar una pieza en la posición (2, 3)
posicion = 2 * 8 + 3
tablero |= (1 << posicion)

# Verificar si hay una pieza en (2, 3)
hay_pieza = (tablero & (1 << posicion)) > 0
print(f"¿Hay pieza en (2,3)?: {hay_pieza}")  # True

# Verificar si hay una pieza en (4, 5)
otra_posicion = 4 * 8 + 5
hay_pieza = (tablero & (1 << otra_posicion)) > 0
print(f"¿Hay pieza en (4,5)?: {hay_pieza}")  # False







# Multiplicar por 2 usando desplazamiento
numero = 42
resultado = numero << 1
print(f"{numero} * 2 = {resultado}")  # 84

# Dividir por 4 usando desplazamiento
numero = 64
resultado = numero >> 2
print(f"{numero} // 4 = {resultado}")  # 16

# Verificar si un número es par (el bit menos significativo es 0)
es_par = (numero & 1) == 0
print(f"¿{numero} es par?: {es_par}")  # True











# Intercambio de valores usando XOR
x = 10
y = 25

print(f"Antes: x = {x}, y = {y}")

x = x ^ y
y = x ^ y
x = x ^ y

print(f"Después: x = {25}, y = {10}")











# Verificar si un bit específico está activado en un conjunto de flags
def tiene_permiso2(permisos, permiso_requerido):
    return permisos & permiso_requerido > 0

# Definir permisos como constantes bit a bit
LEER = 0b0001
ESCRIBIR = 0b0010
EJECUTAR = 0b0100

# Lista de usuarios con sus permisos
usuarios = {
    "admin": LEER | ESCRIBIR | EJECUTAR,  # 7
    "editor": LEER | ESCRIBIR,            # 3
    "visitante": LEER                     # 1
}

# Verificar si un usuario tiene cierto permiso
def verificar_usuario(nombre, permiso):
    return nombre in usuarios and tiene_permiso2(usuarios[nombre], permiso)

print(f"¿Admin puede ejecutar?: {verificar_usuario('admin', EJECUTAR)}")  # True
print(f"¿Editor puede ejecutar?: {verificar_usuario('editor', EJECUTAR)}")  # False
print(f"¿Invitado puede leer?: {verificar_usuario('invitado', LEER)}")  # False (no existe)









from enum import Flag

class Permisos(Flag):
    NINGUNO = 0
    LEER = 1          # 0b0001
    ESCRIBIR = 2      # 0b0010
    EJECUTAR = 4      # 0b0100
    TODOS = LEER.value | ESCRIBIR.value | EJECUTAR.value
 
# Uso más legible
permisos_usuario = Permisos.LEER | Permisos.ESCRIBIR
if Permisos.LEER in permisos_usuario:
    print("Tiene permiso de lectura")










