# mi_paquete/__init__.py

# Importar elementos específicos de los submódulos para hacerlos 
# directamente accesibles desde el paquete
from .modulo1 import funcion_util
from .modulo2 import ClaseImportante

# Definir qué se expone con "from mi_paquete import *"
__all__ = ['funcion_util', 'ClaseImportante']

# Variables del paquete
VERSION = '1.0.0'







# Jupyter Notebook
import importlib
import mi_modulo

# Modificamos mi_modulo.py externamente...

# Recargamos el módulo para ver los cambios
importlib.reload(mi_modulo)








# Errores de permisos: Si no tienes permisos de administrador, usa el flag --user:
pip install --user nombre-del-paquete









# Generar un archivo de requisitos con versiones exactas
pip freeze > requirements.txt






# Importación condicional

try:
    import ujson as json  # Intenta usar la versión rápida
except ImportError:
    import json  # Si no está disponible, usa la estándar

try:
    from PIL import Image
except ImportError:
    print("La biblioteca Pillow no está instalada")
    # Manejo alternativo o salida del programa














# Importación dinámica con importlib

import importlib

def cargar_plugin(nombre_plugin):
    try:
        modulo = importlib.import_module(f"plugins.{nombre_plugin}")
        return modulo.Plugin()
    except (ImportError, AttributeError) as e:
        print(f"Error al cargar el plugin {nombre_plugin}: {e}")
        return None











