import math




# Constantes matemáticas fundamentales
print(f"Pi (π): {math.pi}")  # 3.141592653589793
print(f"Euler (e): {math.e}")  # 2.718281828459045
print(f"Tau (τ): {math.tau}")  # 6.283185307179586 (2π)
print(f"Infinito: {math.inf}")  # Infinito positivo
print(f"NaN (Not a Number): {math.nan}")  # Valor no numérico





# Ángulo en radianes (π/4 = 45 grados)
angulo = math.pi / 4

# Funciones trigonométricas básicas (trabajan con radianes)
print(f"Seno de π/4: {math.sin(angulo)}")  # 0.7071067811865475
print(f"Coseno de π/4: {math.cos(angulo)}")  # 0.7071067811865476
print(f"Tangente de π/4: {math.tan(angulo)}")  # 0.9999999999999999









# Valor absoluto
print(f"Valor absoluto de -5: {math.fabs(-5)}")  # 5.0

# Factorial
n = 5
print(f"Factorial de {n}: {math.factorial(n)}")  # 120

# Máximo común divisor (MCD)
a, b = 24, 36
print(f"MCD de {a} y {b}: {math.gcd(a, b)}")  # 12

# Mínimo común múltiplo (MCM) - Disponible desde Python 3.9
if hasattr(math, 'lcm'):  # Verificamos si está disponible
    print(f"MCM de {a} y {b}: {math.lcm(a, b)}")  # 72

# Raíz cuadrada
x = 16
print(f"Raíz cuadrada de {x}: {math.sqrt(x)}")  # 4.0

# Distancia euclidiana
x1, y1 = 0, 0
x2, y2 = 3, 4
distancia = math.dist((x1, y1), (x2, y2))  # Disponible desde Python 3.8
print(f"Distancia entre puntos: {distancia}")  # 5.0





# Para cálculos que requieren alta precisión, especialmente con números 
# muy grandes o muy pequeños, considera usar el módulo decimal o fractions de Python.








import random

# Generar un número aleatorio entre 0.0 y 1.0
numero_aleatorio = random.random()
print(f"Número aleatorio: {numero_aleatorio}")  # Por ejemplo: 0.7234529875098452











# Alternativa más directa para generar un flotante en un rango específico
numero_aleatorio = random.uniform(5.0, 10.0)
print(f"Número aleatorio entre 5.0 y 10.0: {numero_aleatorio}")











import matplotlib.pyplot as plt

def estimar_pi(num_puntos):
    """Estima el valor de π usando el método de Monte Carlo."""
    puntos_dentro = 0
    puntos_x = []
    puntos_y = []
    colores = []
    
    for _ in range(num_puntos):
        # Generar coordenadas aleatorias entre -1 y 1
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        
        puntos_x.append(x)
        puntos_y.append(y)
        
        # Comprobar si el punto está dentro del círculo unitario
        if x**2 + y**2 <= 1:
            puntos_dentro += 1
            colores.append('blue')
        else:
            colores.append('red')
    
    # La proporción de puntos dentro del círculo nos da π/4
    pi_estimado = 4 * puntos_dentro / num_puntos
    
    # Visualización (opcional)
    plt.figure(figsize=(6, 6))
    plt.scatter(puntos_x, puntos_y, c=colores, alpha=0.5, s=10)
    plt.axis('equal')
    plt.title(f'Estimación de π: {pi_estimado:.6f}')
    plt.show()
    
    return pi_estimado

# Estimar π con 10,000 puntos
estimacion = estimar_pi(10000)
print(f"Valor estimado de π: {estimacion}")
print(f"Valor real de π: {3.141592653589793}")




















import string

def generar_contrasena(longitud=12, incluir_mayusculas=True, 
                       incluir_numeros=True, incluir_simbolos=True):
    """Genera una contraseña aleatoria con los criterios especificados."""
    # Definir los conjuntos de caracteres
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase if incluir_mayusculas else ""
    numeros = string.digits if incluir_numeros else ""
    simbolos = string.punctuation if incluir_simbolos else ""
    
    # Combinar todos los caracteres disponibles
    todos_caracteres = minusculas + mayusculas + numeros + simbolos
    
    # Asegurar que al menos un carácter de cada tipo requerido esté presente
    caracteres_requeridos = []
    if minusculas:
        caracteres_requeridos.append(random.choice(minusculas))
    if mayusculas:
        caracteres_requeridos.append(random.choice(mayusculas))
    if numeros:
        caracteres_requeridos.append(random.choice(numeros))
    if simbolos:
        caracteres_requeridos.append(random.choice(simbolos))
    
    # Completar el resto de la contraseña
    longitud_restante = longitud - len(caracteres_requeridos)
    if longitud_restante > 0:
        caracteres_aleatorios = [random.choice(todos_caracteres) for _ in range(longitud_restante)]
    else:
        caracteres_aleatorios = []
    
    # Combinar y mezclar todos los caracteres
    todos_los_caracteres = caracteres_requeridos + caracteres_aleatorios
    random.shuffle(todos_los_caracteres)
    
    # Convertir la lista de caracteres a una cadena
    contrasena = ''.join(todos_los_caracteres)
    return contrasena

# Generar diferentes tipos de contraseñas
contrasena_segura = generar_contrasena(15)
contrasena_sin_simbolos = generar_contrasena(10, incluir_simbolos=False)
contrasena_solo_letras = generar_contrasena(8, incluir_numeros=False, incluir_simbolos=False)

print(f"Contraseña segura: {contrasena_segura}")
print(f"Contraseña sin símbolos: {contrasena_sin_simbolos}")
print(f"Contraseña solo con letras: {contrasena_solo_letras}")












import random

# Establecer una semilla específica
random.seed(42)

# Generar algunos números aleatorios
print(random.random())  # 0.6394267984578837
print(random.random())  # 0.025010755222666936
print(random.random())  # 0.27502931836911926

# Si reiniciamos con la misma semilla, obtendremos la misma secuencia
random.seed(42)
print(random.random())  # 0.6394267984578837 (igual que el primer número)
print(random.random())  # 0.025010755222666936 (igual que el segundo número)
