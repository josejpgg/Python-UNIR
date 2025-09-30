import pandas as pd

# Creando una Serie con datos de texto
nombres = pd.Series(['Ana García', 'Juan Pérez', 'María Rodríguez', 'Carlos López'])

# Accediendo al accesorio .str
nombres_mayusculas = nombres.str.upper()
print(nombres_mayusculas)









# Convertir a mayúsculas
nombres.str.upper()

# Convertir a minúsculas
nombres.str.lower()

# Capitalizar (primera letra en mayúscula)
nombres.str.capitalize()

# Convertir a formato título (primera letra de cada palabra en mayúscula)
nombres.str.title()

# Extraer los primeros 4 caracteres
print(nombres.str[:4])

# Eliminar espacios en blanco al inicio y final
nombres.str.strip()

# Eliminar espacios a la izquierda o derecha
nombres.str.lstrip()  # izquierda
nombres.str.rstrip()  # derecha









# Verificar si las cadenas contienen un patrón específico
contiene_ana = nombres.str.contains('Ana')
print(contiene_ana)

# Contar ocurrencias de un patrón
ocurrencias_a = nombres.str.count('a')
print(ocurrencias_a)

# Verificar si las cadenas comienzan con un patrón
comienza_con_m = nombres.str.startswith('M')
print(comienza_con_m)

# Verificar si las cadenas terminan con un patrón
termina_con_ez = nombres.str.endswith('ez')
print(termina_con_ez)












# Creando un DataFrame con datos de productos
datos = {
    'producto': ['Laptop HP 15"', 'Monitor Samsung 24"', 'Teclado mecánico RGB', 'Mouse inalámbrico'],
    'categoria': ['Portátiles', 'Monitores', 'Periféricos', 'Periféricos'],
    'precio': [799.99, 249.50, 89.99, 35.50]
}

df = pd.DataFrame(datos)
print(df)


# Ejemplo de encadenamiento de operaciones
resultado = df['producto'].str.lower().str.replace('"', '').str.split(' ').str[0:2].str.join('_')
print(resultado)

















# Creación directa de una Serie categórica
categorias = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'], dtype='category')
print(categorias)

# Convertir una columna existente a tipo categórico
df = pd.DataFrame({
    'ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Madrid', 'Valencia', 'Barcelona'],
    'temperatura': [32, 29, 35, 30, 31, 28]
})

df['ciudad'] = df['ciudad'].astype('category')
print(df.dtypes)





# Acceder a las categorías
print("Categorías disponibles:", df['ciudad'].cat.categories)

# Obtener códigos internos
print("Códigos internos:", df['ciudad'].cat.codes)

# Verificar si las categorías están ordenadas
print("¿Categorías ordenadas?:", df['ciudad'].cat.ordered)







# Añadir nuevas categorías
df['ciudad'] = df['ciudad'].cat.add_categories(['Bilbao', 'Málaga'])
print(df['ciudad'].cat.categories)

# Eliminar categorías no utilizadas
df['ciudad'] = df['ciudad'].cat.remove_unused_categories()
print(df['ciudad'].cat.categories)

# Renombrar categorías
df['ciudad'] = df['ciudad'].cat.rename_categories({'Madrid': 'MAD', 'Barcelona': 'BCN', 
                                                  'Sevilla': 'SVQ', 'Valencia': 'VLC'})
print(df['ciudad'])



















# Creamos un DataFrame de ejemplo con datos textuales
datos = pd.DataFrame({
    'texto': [
        'El precio es $1,500.00',
        'Contacto: info@empresa.com',
        'Teléfono: 91-234-5678',
        'Código: ABC-123-XYZ',
        'Fecha: 2023-05-15'
    ]
})



# Buscar filas que contienen direcciones de correo electrónico
tiene_email = datos['texto'].str.contains(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
print("Filas con emails:")
print(datos[tiene_email])

# Buscar filas que contienen precios en dólares
tiene_precio = datos['texto'].str.contains(r'\$\d+(?:,\d+)*(?:\.\d+)?')
print("\nFilas con precios:")
print(datos[tiene_precio])









# Identificar filas que comienzan con "El" o "La"
comienza_articulo = datos['texto'].str.match(r'(El|La)\s')
print("Comienza con artículo:")
print(datos[comienza_articulo])





# Extraer todos los números de cada texto
numeros = datos['texto'].str.findall(r'\d+')
print("Números encontrados:")
print(numeros)

# Extraer palabras que comienzan con mayúscula
palabras_mayuscula = datos['texto'].str.findall(r'\b[A-Z][a-z]+\b')
print("\nPalabras con mayúscula inicial:")
print(palabras_mayuscula)




# Reemplazar formatos de precio
texto_modificado = datos['texto'].str.replace(r'\$(\d+),(\d+)\.(\d+)', r'\1\2.\3 USD', regex=True)
print("Precios reformateados:")
print(texto_modificado)

# Ocultar información sensible (emails)
anonimizado = datos['texto'].str.replace(r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', 
                                        r'***@\2', regex=True)
print("\nEmails anonimizados:")
print(anonimizado)











