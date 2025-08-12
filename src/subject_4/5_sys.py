import sys

# Imprime todos los argumentos de línea de comandos
print(f"Todos los argumentos: {sys.argv}")

# El primer elemento (índice 0) siempre es el nombre del script
print(f"Nombre del script: {sys.argv[0]}")

# Acceder a argumentos adicionales (si existen)
if len(sys.argv) > 1:
    print(f"Primer argumento: {sys.argv[1]}")








# Escribir en la salida estándar
sys.stdout.write("Este es un mensaje normal\n")

# Escribir en el error estándar
sys.stderr.write("Este es un mensaje de error\n")












import sys

# Versión de Python
print(f"Versión de Python: {sys.version}")
print(f"Información de versión: {sys.version_info}")

# Plataforma
print(f"Plataforma: {sys.platform}")

# Ruta de búsqueda de módulos
print("Rutas de búsqueda de módulos:")
for ruta in sys.path:
    print(f"  - {ruta}")







import logging


# Configurar el nivel básico de logging a INFO
logging.basicConfig(level=logging.INFO)

logging.debug("Este es un mensaje de depuración")  # No se mostrará
logging.info("Programa iniciado correctamente")    # Se mostrará
logging.warning("Archivo de configuración no encontrado, usando valores predeterminados")
logging.error("No se pudo procesar el archivo de datos")
logging.critical("Error crítico: base de datos no disponible")


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
	# filename='app.log',
    # filemode='w'  # 'w' para sobrescribir, 'a' para añadir
)

logging.info("Aplicación iniciada")

# 2023-07-15 14:30:45,123 - INFO - Aplicación iniciada




# Configuración para mostrar logs en consola y archivo simultáneamente

import logging

# Crear un logger
logger = logging.getLogger('mi_aplicacion')
logger.setLevel(logging.DEBUG)

# Crear manejador para archivo
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Crear manejador para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # En consola solo mostramos INFO o superior

# Definir formato
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Añadir los manejadores al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Usar el logger
logger.debug("Este mensaje solo aparece en el archivo")
logger.info("Este mensaje aparece en archivo y consola")
logger.warning("¡Cuidado! Algo no está bien")
logger.error("Se ha producido un error")





# Rotación de archivos de log

import logging
from logging.handlers import RotatingFileHandler

# Configurar logger
logger = logging.getLogger('mi_aplicacion')
logger.setLevel(logging.DEBUG)

# Crear manejador con rotación
# Máximo 5 archivos de backup, cada uno de máximo 2MB
handler = RotatingFileHandler(
    'app.log', 
    maxBytes=2*1024*1024,  # 2MB
    backupCount=5
)
handler.setLevel(logging.DEBUG)

# Configurar formato
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Añadir manejador al logger
logger.addHandler(handler)

# Ejemplo de uso
logger.debug("Mensaje de depuración")




# Rotación por tiempo

import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('mi_aplicacion')
logger.setLevel(logging.DEBUG)

# Rotar el archivo cada día a medianoche, conservando 30 días
handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',
    interval=1,
    backupCount=30
)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(handler)





# Ejemplo práctico: logging en una aplicación

import logging
import time

def configurar_logging():
    """Configura el sistema de logging para la aplicación."""
    # Crear logger
    logger = logging.getLogger('procesador_datos')
    logger.setLevel(logging.DEBUG)
    
    # Evitar duplicación de handlers si la función se llama múltiples veces
    if not logger.handlers:
        # Handler para consola
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console_format = logging.Formatter('%(levelname)s: %(message)s')
        console.setFormatter(console_format)
        
        # Handler para archivo
        file_handler = logging.FileHandler('procesamiento.log')
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)
        
        # Añadir handlers al logger
        logger.addHandler(console)
        logger.addHandler(file_handler)
    
    return logger

def procesar_datos(datos):
    """Procesa una lista de datos y devuelve los resultados."""
    logger = logging.getLogger('procesador_datos')
    
    logger.info(f"Iniciando procesamiento de {len(datos)} elementos")
    resultados = []
    
    for i, item in enumerate(datos):
        try:
            logger.debug(f"Procesando item {i}: {item}")
            
            # Simular procesamiento
            time.sleep(0.1)
            
            if item < 0:
                logger.warning(f"Valor negativo encontrado: {item}")
            
            resultado = item * 2
            resultados.append(resultado)
            
        except Exception as e:
            logger.error(f"Error procesando item {i}: {e}", exc_info=True)
    
    logger.info("Procesamiento completado")
    return resultados

# Uso de la aplicación
if __name__ == "__main__":
    logger = configurar_logging()
    logger.info("Aplicación iniciada")
    
    try:
        datos = [1, 2, -3, 4, "5"]
        resultados = procesar_datos(datos)
        logger.info(f"Resultados: {resultados}")
    except Exception as e:
        logger.critical(f"Error fatal en la aplicación: {e}", exc_info=True)
    
    logger.info("Aplicación finalizada")












import os

# Acceder a una variable de entorno específica
home_directory = os.environ.get('HOME')  # En Windows sería 'USERPROFILE'
print(f"Tu directorio home es: {home_directory}")

# Acceder con manejo de valores por defecto
python_path = os.environ.get('PYTHONPATH', 'No está definida')
print(f"PYTHONPATH: {python_path}")


# Listar todas las variables de entorno
print("Variables de entorno disponibles:")
for key, value in os.environ.items():
    print(f"  {key} = {value}")









# Establecer una nueva variable de entorno
os.environ['MI_VARIABLE'] = 'mi_valor'
print(f"MI_VARIABLE: {os.environ.get('MI_VARIABLE')}")

# Modificar una variable existente
os.environ['PATH'] = f"{os.environ.get('PATH')}:/nueva/ruta"











def obtener_configuracion_db():
    """Obtiene la configuración de la base de datos según el entorno."""
    entorno = os.environ.get('APP_ENV', 'desarrollo')
    
    if entorno == 'produccion':
        return {
            'host': os.environ.get('DB_HOST', 'localhost'),
            'puerto': int(os.environ.get('DB_PORT', '5432')),
            'usuario': os.environ.get('DB_USER', 'admin'),
            'contraseña': os.environ.get('DB_PASSWORD', ''),
            'nombre': os.environ.get('DB_NAME', 'app_prod')
        }
    else:  # desarrollo o pruebas
        return {
            'host': 'localhost',
            'puerto': 5432,
            'usuario': 'dev_user',
            'contraseña': 'dev_password',
            'nombre': 'app_dev'
        }

# Uso
config = obtener_configuracion_db()
print(f"Configuración de BD: {config}")











# Crear un directorio
try:
    os.mkdir('nuevo_directorio')
    print("Directorio creado con éxito")
except FileExistsError:
    print("El directorio ya existe")

# Crear directorios anidados (equivalente a mkdir -p)
try:
    os.makedirs('directorio/subdirectorio/otro_nivel', exist_ok=True)
    print("Estructura de directorios creada")
except PermissionError:
    print("No tienes permisos para crear estos directorios")

# Eliminar un directorio vacío
try:
    os.rmdir('nuevo_directorio')
    print("Directorio eliminado")
except FileNotFoundError:
    print("El directorio no existe")
except OSError:
    print("El directorio no está vacío o no tienes permisos")











# crear una estructura de directorios para un proyecto

def crear_estructura_proyecto(nombre_proyecto):
    """Crea una estructura básica de directorios para un proyecto Python."""
    directorios = [
        nombre_proyecto,
        f"{nombre_proyecto}/src",
        f"{nombre_proyecto}/tests",
        f"{nombre_proyecto}/docs",
        f"{nombre_proyecto}/data"
    ]
    
    for directorio in directorios:
        try:
            os.makedirs(directorio, exist_ok=True)
            print(f"Creado: {directorio}")
        except Exception as e:
            print(f"Error al crear {directorio}: {e}")
    
    # Crear archivos básicos
    archivos = {
        f"{nombre_proyecto}/README.md": "# {}\n\nDescripción del proyecto.".format(nombre_proyecto),
        f"{nombre_proyecto}/requirements.txt": "# Dependencias\npython>=3.8\n",
        f"{nombre_proyecto}/src/__init__.py": "",
        f"{nombre_proyecto}/tests/__init__.py": ""
    }
    
    for ruta, contenido in archivos.items():
        try:
            with open(ruta, 'w') as f:
                f.write(contenido)
            print(f"Creado: {ruta}")
        except Exception as e:
            print(f"Error al crear {ruta}: {e}")

# Uso
crear_estructura_proyecto("mi_proyecto_python")










# Nombre del sistema operativo
print(f"Sistema operativo: {os.name}")  # 'posix' para Unix/Linux/Mac, 'nt' para Windows

# Separador de rutas del sistema
print(f"Separador de rutas: '{os.sep}'")  # '/' en Unix/Linux/Mac, '\' en Windows

# Separador de rutas en variables de entorno
print(f"Separador de PATH: '{os.pathsep}'")  # ':' en Unix/Linux/Mac, ';' en Windows

# Salto de línea del sistema
print(f"Salto de línea: '{os.linesep}'")  # '\n' en Unix/Linux/Mac, '\r\n' en Windows








from pathlib import Path

# Ruta al directorio actual
ruta_actual = Path.cwd()
print(f"Directorio actual: {ruta_actual}")

# Ruta al directorio home del usuario
ruta_home = Path.home()
print(f"Directorio home: {ruta_home}")

# Crear una ruta a partir de una cadena
ruta_archivo = Path('documentos/archivo.txt')
print(f"Ruta de archivo: {ruta_archivo}")

# Crear una ruta a partir de componentes
ruta_componentes = Path('proyectos', 'python', 'script.py')
print(f"Ruta por componentes: {ruta_componentes}")










# Unir rutas usando el operador /
ruta_base = Path('/home/usuario')
ruta_completa = ruta_base / 'documentos' / 'archivo.txt'
print(f"Ruta completa: {ruta_completa}")

# Obtener el directorio padre
directorio_padre = ruta_completa.parent
print(f"Directorio padre: {directorio_padre}")

# Obtener varios niveles de directorios padres
abuelo = ruta_completa.parent.parent
print(f"Directorio abuelo: {abuelo}")

# Cambiar el nombre o extensión
nueva_extension = ruta_completa.with_suffix('.pdf')
print(f"Con nueva extensión: {nueva_extension}")

nuevo_nombre = ruta_completa.with_name('nuevo_archivo.txt')
print(f"Con nuevo nombre: {nuevo_nombre}")

# Resolver rutas relativas
ruta_relativa = Path('documentos/../proyectos/./script.py')
ruta_resuelta = ruta_relativa.resolve()
print(f"Ruta resuelta: {ruta_resuelta}")






