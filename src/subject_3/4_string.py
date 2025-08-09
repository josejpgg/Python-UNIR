texto_con_espacios = "   Python   "

print(f"Con espacios: '{texto_con_espacios}'")
print(f"strip(): '{texto_con_espacios.strip()}'")
print(f"lstrip(): '{texto_con_espacios.lstrip()}'")
print(f"rstrip(): '{texto_con_espacios.rstrip()}'")






texto = "###Python###"
print(texto.strip('#'))    # Python
print(texto.lstrip('#'))   # Python###
print(texto.rstrip('#'))   # ###Python










texto = "Python"

print(texto.center(20))        # '       Python       '
print(texto.center(20, '-'))   # '-------Python-------'
print(texto.ljust(20, '*'))    # 'Python**************'
print(texto.rjust(20, '*'))    # '**************Python'
print("42".zfill(5))           # '00042'







pi = 3.14159265359
print(f"Pi redondeado a 3 decimales: {pi:.3f}")  # Pi redondeado a 3 decimales: 3.142








from string import Template

plantilla = Template("Hola, $nombre. Bienvenido a $plataforma.")
mensaje = plantilla.substitute(nombre="Miguel", plataforma="Python")
print(mensaje)  # Hola, Miguel. Bienvenido a Python.








# Ejemplo de informe con f-strings
nombre = "Proyecto Alpha"
progreso = 75.5
fecha = "2023-04-15"

informe = f"""
INFORME DE ESTADO
================
Proyecto: {nombre}
Progreso: {progreso:.1f}%
Fecha: {fecha}
Estado: {"Completado" if progreso == 100 else "En progreso"}
"""
print(informe)














texto = "Python"
print(texto[0])  # P
print(texto[1])  # y
print(texto[5])  # n








texto = "Python es divertido"

# Tomar caracteres alternos (paso 2)
print(texto[::2])     # Pto sdvrio

# Invertir una cadena (paso -1)
print(texto[::-1])    # oditrevid se nohtyP

# Cada tercer carácter desde el índice 0 al 10
print(texto[0:10:3])  # Pne






url = "https://www.ejemplo.com/productos/categoria?id=123"

# Extraer el protocolo
protocolo = url[:url.find("://")]
print(f"Protocolo: {protocolo}")  # Protocolo: https

# Extraer el dominio
inicio_dominio = url.find("://") + 3
fin_dominio = url.find("/", inicio_dominio)
dominio = url[inicio_dominio:fin_dominio]
print(f"Dominio: {dominio}")      # Dominio: www.ejemplo.com

# Extraer la ruta
inicio_ruta = fin_dominio
fin_ruta = url.find("?", inicio_ruta)
ruta = url[inicio_ruta:fin_ruta] if fin_ruta != -1 else url[inicio_ruta:]
print(f"Ruta: {ruta}")            # Ruta: /productos/categoria










nombre_archivo = "documento_importante.pdf"

# Extraer el nombre sin extensión
punto = nombre_archivo.rfind(".")
nombre_base = nombre_archivo[:punto]
print(f"Nombre base: {nombre_base}")  # Nombre base: documento_importante

# Extraer la extensión
extension = nombre_archivo[punto+1:]
print(f"Extensión: {extension}")      # Extensión: pdf

# Crear un nombre de archivo para una copia de seguridad
backup = f"{nombre_base}_backup.{extension}"
print(f"Archivo de respaldo: {backup}")  # Archivo de respaldo: documento_importante_backup.pdf






telefono = "912345678"

# Formatear como (91) 234-5678
if len(telefono) == 9:
    formateado = f"({telefono[:2]}) {telefono[2:5]}-{telefono[5:]}"
    print(formateado)  # (91) 234-5678







texto = "Python es un lenguaje de programación Python"

# Buscar la última ocurrencia
posicion = texto.rfind("Python")
print(f"Última ocurrencia: índice {posicion}")  # Última ocurrencia: índice 35

# Buscar hacia atrás desde una posición específica
posicion = texto.rfind("Python", 0, 30)
print(f"Última antes del índice 30: {posicion}")  # Última antes del índice 30: 0









texto = "Python es un lenguaje de programación"

try:
    posicion = texto.index("lenguaje")
    print(f"Encontrado en: {posicion}")  # Encontrado en: 11
    
    posicion = texto.index("Java")  # Esto generará una excepción
except ValueError as e:
    print(f"Error: {e}")  # Error: substring not found













