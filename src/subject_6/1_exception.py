# ZeroDivisionError: Ocurre al intentar dividir por cero
# TypeError: Cuando una operación se aplica a un objeto de tipo inapropiado
# ValueError: Cuando una función recibe un argumento del tipo correcto pero con un valor inapropiado
# FileNotFoundError: Al intentar acceder a un archivo que no existe
# IndexError: Al intentar acceder a un índice fuera del rango de una secuencia
# KeyError: Al intentar acceder a una clave que no existe en un diccionario








# Enfoque ineficiente
def es_par(numero):
    try:
        return numero % 2 == 0
    except:
        return False






# Enfoque eficiente
def es_par(numero):
    if isinstance(numero, (int, float)):
        return numero % 2 == 0
    return False







def funcion_c():
    # Esta función genera una excepción
    return 10 / 0

def funcion_b():
    # Esta función llama a funcion_c pero no maneja excepciones
    return funcion_c() + 1

def funcion_a():
    # Esta función maneja la excepción propagada desde funcion_b y funcion_c
    try:
        resultado = funcion_b()
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Error: División por cero detectada")

# Llamada a la función principal
funcion_a()  # Imprime: Error: División por cero detectada









def convertir_a_numero(valor, valor_predeterminado=0):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return valor_predeterminado

# Ejemplos
datos = ["10", "20.5", "treinta", None, []]
numeros = [convertir_a_numero(x) for x in datos]
print(numeros)  # [10.0, 20.5, 0, 0, 0]










# Buenas prácticas al usar try-except
# Ser específico: Captura solo las excepciones que esperas y sabes cómo manejar.
# Mantén los bloques try lo más pequeños posible: Incluye solo el código que realmente podría generar la excepción.
# No silencies excepciones sin una buena razón:
# Evita usar excepciones para flujo de control normal cuando existen alternativas más claras:









try:
    # Código que podría generar una excepción
    # Aquí normalmente se adquieren recursos
except TipoExcepcion:
    # Código que se ejecuta si ocurre una excepción
finally:
    # Código que se ejecuta SIEMPRE, haya o no excepción
    # Aquí normalmente se liberan recursos















import sqlite3

conexion = None
cursor = None
try:
    conexion = sqlite3.connect("mi_base_datos.db")
    cursor = conexion.cursor()
    
    cursor.execute("SELECT nombre FROM usuarios WHERE id = ?", (1,))
    usuario = cursor.fetchone()
    
    if usuario:
        print(f"Usuario encontrado: {usuario[0]}")
    else:
        print("Usuario no encontrado")
        
except sqlite3.Error as error:
    print(f"Error en la base de datos: {error}")
finally:
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()
        print("Conexión a la base de datos cerrada")













# Comparación con el patrón with
# Sin with (usando finally)
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    print(contenido)
finally:
    archivo.close()

# Con with (más elegante y seguro)
try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe")
















try:
    archivo = open("config.txt", "r")
    configuracion = archivo.read()
except FileNotFoundError:
    print("Archivo de configuración no encontrado, usando valores predeterminados")
    configuracion = "config_predeterminada"
else:
    # Este bloque se ejecuta si no hay excepciones
    print("Configuración cargada correctamente")
    # Podemos procesar la configuración aquí
finally:
    # Este bloque se ejecuta siempre
    if 'archivo' in locals() and archivo:
        archivo.close()
        print("Archivo cerrado")
    
    print("Inicializando sistema con la configuración disponible")

# El bloque try intenta abrir y leer un archivo
# El bloque except maneja el caso en que el archivo no existe
# El bloque else se ejecuta solo si la lectura del archivo tiene éxito
# El bloque finally se ejecuta en todos los casos, cerrando el archivo si fue abierto


















class ConexionBD:
    def __init__(self, configuracion):
        self.configuracion = configuracion
        self.conexion = None
    
    def __enter__(self):
        print(f"Conectando a la base de datos: {self.configuracion}")
        self.conexion = "conexión_simulada"  # En un caso real, aquí conectaríamos
        return self.conexion
    
    def __exit__(self, tipo_exc, valor_exc, traceback_exc):
        print("Cerrando conexión a la base de datos")
        if self.conexion:
            # En un caso real, aquí cerraríamos la conexión
            self.conexion = None
        
        # Podemos decidir si suprimir la excepción o no
        # Retornar True la suprime, False (o None) la propaga
        return False

# Uso con with
try:
    with ConexionBD("mysql://localhost/midb") as conexion:
        print(f"Ejecutando consulta en {conexion}")
        # Si ocurre una excepción aquí, __exit__ se llamará automáticamente
except Exception as e:
    print(f"Error manejado: {e}")


















class ValorNegativoError(Exception):
    """Se lanza cuando un valor que debería ser positivo es negativo."""
    
    def __init__(self, valor, mensaje="No se permiten valores negativos"):
        self.valor = valor
        self.mensaje = mensaje
        super().__init__(self.mensaje)
    
    def __str__(self):
        return f"{self.mensaje}: {self.valor}"


def calcular_raiz_cuadrada(numero):
    if numero < 0:
        raise ValorNegativoError(numero, "No se puede calcular la raíz cuadrada de un número negativo")
    return numero ** 0.5

# Uso de la función
try:
    resultado = calcular_raiz_cuadrada(-5)
except ValorNegativoError as e:
    print(f"Error: {e}")
    # Podemos acceder a los atributos específicos
    print(f"El valor problemático fue: {e.valor}")

















# Excepción base para toda la aplicación
class ErrorAplicacion(Exception):
    """Clase base para todas las excepciones de la aplicación."""
    pass

# Excepciones para diferentes módulos o categorías
class ErrorBaseDatos(ErrorAplicacion):
    """Errores relacionados con la base de datos."""
    pass

class ErrorValidacion(ErrorAplicacion):
    """Errores de validación de datos."""
    pass

# Excepciones específicas
class ConexionPerdidaError(ErrorBaseDatos):
    """La conexión con la base de datos se ha perdido."""
    def __init__(self, host=None, mensaje="Conexión perdida con la base de datos"):
        self.host = host
        self.mensaje = mensaje
        super().__init__(f"{mensaje} {host}" if host else mensaje)

class DatoInvalidoError(ErrorValidacion):
    """El dato proporcionado no cumple con los requisitos."""
    def __init__(self, campo, valor, mensaje=None):
        self.campo = campo
        self.valor = valor
        self.mensaje = mensaje or f"Valor inválido para el campo '{campo}'"
        super().__init__(f"{self.mensaje}: {valor}")

ç
def procesar_datos(datos):
    try:
        validar_datos(datos)
        guardar_en_bd(datos)
        return True
    except ConexionPerdidaError as e:
        print(f"Error de conexión: {e}")
        # Intentar reconectar
        return False
    except DatoInvalidoError as e:
        print(f"Error de validación: {e.mensaje}")
        print(f"Campo: {e.campo}, Valor: {e.valor}")
        return False
    except ErrorAplicacion as e:
        # Captura cualquier otra excepción de la aplicación
        print(f"Error general de la aplicación: {e}")
        return False















class ArchivoConfiguracionError(FileNotFoundError):
    """Error específico para archivos de configuración faltantes."""
    
    def __init__(self, nombre_archivo, mensaje=None):
        self.nombre_archivo = nombre_archivo
        mensaje_completo = mensaje or f"Archivo de configuración no encontrado: {nombre_archivo}"
        super().__init__(mensaje_completo)
        
    def generar_config_predeterminada(self):
        """Método para generar una configuración predeterminada."""
        print(f"Generando configuración predeterminada en {self.nombre_archivo}")
        # Código para crear el archivo con valores predeterminados


def cargar_configuracion(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        # Convertimos la excepción estándar en nuestra excepción personalizada
        error = ArchivoConfiguracionError(ruta_archivo)
        # Podemos usar métodos específicos de nuestra excepción
        error.generar_config_predeterminada()
        raise error


















