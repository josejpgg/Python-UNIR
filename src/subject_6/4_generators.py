def contador_simple():
    print("Iniciando contador")
    yield 1
    print("Continuando después del primer yield")
    yield 2
    print("Continuando después del segundo yield")
    yield 3
    print("Generador terminado")



gen = contador_simple()
print(type(gen))  # <class 'generator'>


for valor in contador_simple():
    print(f"Valor: {valor}")

# Salida:
# Iniciando contador
# Valor: 1
# Continuando después del primer yield
# Valor: 2
# Continuando después del segundo yield
# Valor: 3
# Generador terminado

















def leer_archivo_grande(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            yield linea.strip()

# Procesar un archivo gigante sin problemas de memoria
for linea in leer_archivo_grande("datos_enormes.txt"):
    # Procesar cada línea
    pass











def filtrar_pares(numeros):
    for num in numeros:
        if num % 2 == 0:
            yield num

def multiplicar_por_tres(numeros):
    for num in numeros:
        yield num * 3

# Crear un pipeline de procesamiento
numeros = range(10)
numeros_pares = filtrar_pares(numeros)
resultado = multiplicar_por_tres(numeros_pares)

print(list(resultado))  # [0, 6, 12, 18, 24]









def eco():
    valor = None
    while True:
        # yield devuelve un valor Y recibe el próximo valor enviado
        valor_recibido = yield valor
        print(f"Recibido: {valor_recibido}")
        valor = valor_recibido

generador = eco()
next(generador)  # Inicializar el generador (avanza hasta el primer yield)

for mensaje in ["Hola", "Mundo", "Python"]:
    respuesta = generador.send(mensaje)
    print(f"Respuesta: {respuesta}")

# Salida:
# Recibido: Hola
# Respuesta: Hola
# Recibido: Mundo
# Respuesta: Mundo
# Recibido: Python
# Respuesta: Python













# Lista: todos los elementos se calculan y almacenan inmediatamente
lista_cuadrados = [x**2 for x in range(1000000)]  # Ocupa memoria para 1 millón de elementos

# Generador: los elementos se calculan solo cuando se solicitan
generador_cuadrados = (x**2 for x in range(1000000))  # Ocupa memoria mínima














# Procesamiento de un archivo grande línea por línea
def procesar_archivo_grande(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        # Procesamos una línea a la vez, sin cargar todo el archivo
        for linea in archivo:  # El archivo es un iterador/generador implícito
            yield linea.upper()

# Uso eficiente de memoria incluso con archivos de varios GB
for linea_procesada in procesar_archivo_grande("datos_masivos.txt"):
    # Trabajamos con cada línea individualmente
    print(linea_procesada[:50])  # Mostramos solo los primeros 50 caracteres














# Enfoque con listas: cada paso crea una lista completa en memoria
def pipeline_con_listas(datos):
    paso1 = [x * 2 for x in datos]          # Primera lista completa
    paso2 = [x + 5 for x in paso1]          # Segunda lista completa
    paso3 = [x for x in paso2 if x % 3 == 0]  # Tercera lista completa
    return paso3

# Enfoque con generadores: cada elemento fluye a través del pipeline
def pipeline_con_generadores(datos):
    paso1 = (x * 2 for x in datos)          # Solo generador, no datos
    paso2 = (x + 5 for x in paso1)          # Solo generador, no datos
    paso3 = (x for x in paso2 if x % 3 == 0)  # Solo generador, no datos
    return paso3

# Con datos grandes, la diferencia es crucial
datos_grandes = range(10000000)  # 10 millones de elementos

# Esto consumiría mucha memoria y tiempo
# resultado_listas = pipeline_con_listas(datos_grandes)

# Esto es instantáneo y usa memoria mínima
resultado_generadores = pipeline_con_generadores(datos_grandes)

# Los cálculos solo ocurren cuando iteramos sobre el resultado
for valor in resultado_generadores:
    print(valor)
    if valor > 100:  # Solo procesamos los primeros valores
        break
















# Ejemplo: Análisis de datos de sensores IoT
def analizar_datos_sensores(archivo_datos):
    with open(archivo_datos, 'r') as f:
        # Saltamos la cabecera
        next(f)
        for linea in f:
            # Parseamos cada línea
            timestamp, sensor_id, temperatura, humedad = linea.strip().split(',')
            
            # Convertimos tipos
            timestamp = int(timestamp)
            temperatura = float(temperatura)
            humedad = float(humedad)
            
            # Filtramos lecturas anómalas
            if temperatura > -50 and temperatura < 100:
                # Devolvemos solo los datos relevantes procesados
                yield {
                    'hora': timestamp // 3600,
                    'sensor': sensor_id,
                    'temp_celsius': temperatura,
                    'alerta': temperatura > 40
                }

# Procesamos terabytes de datos de sensores eficientemente
for lectura in analizar_datos_sensores("sensores_2023.csv"):
    if lectura['alerta']:
        # enviar_notificacion(lectura['sensor'], lectura['temp_celsius'])
        print("")











def cuenta_regresiva(n):
    while n > 0:
        yield n
        n -= 1

# Creamos un objeto generador
gen = cuenta_regresiva(5)

# Obtenemos valores manualmente con next()
print(next(gen))  # 5
print(next(gen))  # 4
print(next(gen))  # 3















def manual_for(iterable):
    """Implementación manual de un bucle for."""
    iterator = iter(iterable)  # Obtiene el iterador
    
    while True:
        try:
            # Intenta obtener el siguiente valor
            value = next(iterator)
            print(value)
        except StopIteration:
            # Termina cuando no hay más elementos
            break

# Usando nuestra función con un generador
manual_for(cuenta_regresiva(3))
# Salida:
# 3
# 2
# 1















def saltar_primeros(generador, n):
    """Salta los primeros n elementos de un generador."""
    # Consumimos los primeros n elementos
    for _ in range(n):
        try:
            next(generador)
        except StopIteration:
            # Si el generador se agota, devolvemos un generador vacío
            return
    
    # Devolvemos el resto del generador
    yield from generador

# Ejemplo: saltar los primeros 2 elementos
numeros = (x for x in range(5))
for num in saltar_primeros(numeros, 2):
    print(num)  # Imprime: 2, 3, 4












# Solo los cuadrados de números pares
pares_cuadrados = (x**2 for x in range(10) if x % 2 == 0)

# Equivalente con función generadora
def pares_cuadrados_func():
    for x in range(10):
        if x % 2 == 0:
            yield x**2








# Contar líneas que contienen una palabra específica
def contar_coincidencias(archivo, palabra):
    with open(archivo, 'r') as f:
        return sum(1 for linea in f if palabra in linea)

# Uso
total = contar_coincidencias('datos.txt', 'Python')
print(f"La palabra 'Python' aparece en {total} líneas")











def filtrar_y_transformar(datos, filtro_func, transform_func):
    """
    Aplica filtrado y transformación a un conjunto de datos.
    """
    # Usamos una expresión generadora dentro de una función generadora
    for item in (transform_func(x) for x in datos if filtro_func(x)):
        yield item

# Funciones de filtro y transformación
es_par = lambda x: x % 2 == 0
cuadrado = lambda x: x**2

# Uso
numeros = range(10)
resultado = filtrar_y_transformar(numeros, es_par, cuadrado)
print(list(resultado))  # [0, 4, 16, 36, 64]













