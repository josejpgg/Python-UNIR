# Crea un script en Python que utilice el módulo os para listar todos los archivos (no directorios) en el directorio actual, ordenados por tamaño (de mayor a menor). Para cada archivo, muestra su nombre y tamaño en bytes.

# El script debe:

# Obtener la lista de todos los elementos en el directorio actual
# Filtrar solo los archivos (no directorios)
# Obtener el tamaño de cada archivo usando las funciones apropiadas
# Ordenar la lista de archivos por tamaño de forma descendente
# Mostrar el nombre y tamaño de cada archivo
# Puedes empezar importando el módulo os y utilizando os.listdir() para obtener los elementos del directorio actual.

import os

list_files = os.listdir('.')
list_files = [file for file in list_files if os.path.isfile(file)]
list_files_size = [(file, os.path.getsize(file)) for file in list_files]
list_sorted = sorted(list_files_size, key=lambda x: x[1], reverse=True)
for file, size in list_sorted:
	print(f"{file}: {size} bytes")

# Better alternative
for entry in os.scandir(path='.'):
	print(f"{entry.name}: {entry.stat().st_size} bytes")
