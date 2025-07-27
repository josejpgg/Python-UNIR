mi_diccionario = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid"
}



# Valores hash de diferentes tipos de datos
print(hash("python"))  # String -7215292171999272582
print(hash(42))        # Entero 42
print(hash(3.14))      # Flotante 322818021289917443
print(hash(True))      # Booleano 1
print(hash((1, 2, 3))) # Tupla 529344067295497451






texto = "hola mundo hola python"
frecuencias = {}

for palabra in texto.split():
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1
        
print(frecuencias)  # {'hola': 2, 'mundo': 1, 'python': 1}












# Caché para la secuencia de Fibonacci
cache_fibonacci = {}

def fibonacci(n):
    # Si ya calculamos este valor, lo devolvemos directamente
    if n in cache_fibonacci:
        return cache_fibonacci[n]
    
    # Calculamos el valor para n
    if n <= 1:
        resultado = n
    else:
        resultado = fibonacci(n-1) + fibonacci(n-2)
    
    # Guardamos en caché antes de devolver
    cache_fibonacci[n] = resultado
    return resultado

# Ahora las llamadas repetidas son instantáneas
print(fibonacci(30))  # Rápido incluso para valores grandes





# Diccionario con elementos iniciales
estudiante = {"nombre": "Carlos", "edad": 22, "carrera": "Informática"}

# Diccionario vacío
configuracion = {}







# A partir de pares clave-valor
opciones = dict(color="azul", tamaño="mediano", disponible=True)

# A partir de una lista de tuplas (clave, valor)
coordenadas = dict([("x", 10), ("y", 20), ("z", 30)])









# Crear un diccionario con múltiples claves y el mismo valor
usuarios = dict.fromkeys(["admin", "editor", "invitado"], False)
print(usuarios)  # {'admin': False, 'editor': False, 'invitado': False}

# Si omitimos el segundo parámetro, el valor predeterminado es None
campos = dict.fromkeys(["nombre", "email", "teléfono"])
print(campos)  # {'nombre': None, 'email': None, 'teléfono': None}




producto = {"id": 1001, "nombre": "Teclado", "precio": 45.99}


# Acceder con get() - devuelve None si la clave no existe
print(producto.get("precio"))  # 45.99
print(producto.get("color"))   # None

# Podemos especificar un valor predeterminado si la clave no existe
print(producto.get("color", "No especificado"))  # No especificado






usuario = {"nombre": "Ana", "email": "ana@ejemplo.com"}

# Añadir un nuevo par clave-valor
usuario["rol"] = "administrador"

# Modificar un valor existente
usuario["email"] = "ana.lopez@ejemplo.com"

print(usuario)  
# {'nombre': 'Ana', 'email': 'ana.lopez@ejemplo.com', 'rol': 'administrador'}



perfil = {"usuario": "jsmith", "activo": True}

# Actualizar con otro diccionario
datos_adicionales = {"nombre": "John Smith", "edad": 35}
perfil.update(datos_adicionales)

# También podemos usar argumentos con nombre
perfil.update(ubicacion="Madrid", departamento="Desarrollo")

print(perfil)
# {'usuario': 'jsmith', 'activo': True, 'nombre': 'John Smith', 'edad': 35, 'ubicacion': 'Madrid', 'departamento': 'Desarrollo'}



inventario = {"manzanas": 50, "peras": 30, "uvas": 45, "naranjas": 20}

# Eliminar un elemento específico con del
del inventario["peras"]

# Eliminar y obtener el valor con pop()
cantidad_uvas = inventario.pop("uvas")
print(f"Se eliminaron {cantidad_uvas} uvas del inventario")

# Eliminar y obtener el último elemento añadido (Python 3.7+)
ultimo_elemento = inventario.popitem()
print(f"Se eliminó: {ultimo_elemento}")

print(inventario)  # {'manzanas': 50}


carrito = {"producto1": 2, "producto2": 1}
carrito.clear()  # Elimina todos los elementos
print(carrito)  # {}







# En Python 3.9+ podemos usar el operador |
defaults = {"tema": "claro", "idioma": "es"}
preferencias_usuario = {"tema": "oscuro"}
configuracion = defaults | preferencias_usuario
print(configuracion)  # {'tema': 'oscuro', 'idioma': 'es'}

# También funciona con |=
defaults |= {"notificaciones": True}
print(defaults)  # {'tema': 'claro', 'idioma': 'es', 'notificaciones': True}




# Asignar un valor solo si la clave no existe
opciones = {"debug": True}
opciones.setdefault("timeout", 30)  # Añade la clave si no existe
opciones.setdefault("debug", False)  # No modifica el valor existente

print(opciones)  # {'debug': True, 'timeout': 30}





original = {"a": 1, "b": 2}

# Copia superficial
copia1 = original.copy()
copia2 = dict(original)

# Modificar la copia no afecta al original
copia1["c"] = 3
print(original)  # {'a': 1, 'b': 2}
print(copia1)    # {'a': 1, 'b': 2, 'c': 3}






empleado = {
    "datos_personales": {
        "nombre": "Laura",
        "apellido": "Gómez",
        "edad": 29
    },
    "habilidades": ["Python", "SQL", "JavaScript"]
}

# Acceder a valores anidados
print(empleado["datos_personales"]["nombre"])  # Laura

# Modificar valores anidados
empleado["datos_personales"]["edad"] = 30

# Añadir elementos a una lista dentro del diccionario
empleado["habilidades"].append("Docker")
print(empleado["habilidades"])  # ['Python', 'SQL', 'JavaScript', 'Docker']







estudiantes = [
    {"nombre": "Ana", "curso": "Python"},
    {"nombre": "Luis", "curso": "JavaScript"},
    {"nombre": "Carlos", "curso": "Python"},
    {"nombre": "María", "curso": "Java"}
]

# Agrupar estudiantes por curso
por_curso = {}
for estudiante in estudiantes:
    curso = estudiante["curso"]
    if curso not in por_curso:
        por_curso[curso] = []
    por_curso[curso].append(estudiante["nombre"])

print(por_curso)
# {'Python': ['Ana', 'Carlos'], 'JavaScript': ['Luis'], 'Java': ['María']}







# Convertir una lista de tuplas en un diccionario
datos = [("nombre", "Tablet Pro"), ("precio", 299.99), ("stock", 15)]
producto = dict(datos)
print(producto)  # {'nombre': 'Tablet Pro', 'precio': 299.99, 'stock': 15}




producto = {"id": 100, "nombre": "Monitor", "precio": 150}

# Iterar sobre las claves (comportamiento predeterminado)
for clave in producto:
    print(clave)

# Iterar sobre los valores
for valor in producto.values():
    print(valor)

# Iterar sobre pares clave-valor
for clave, valor in producto.items():
    print(f"{clave}: {valor}")






# Diccionario base
producto = {"nombre": "Laptop", "precio": 899.99}

# Actualizar con otro diccionario
producto.update({"precio": 799.99, "stock": 10, "modelo": "X1"})
print(producto)  
# {'nombre': 'Laptop', 'precio': 799.99, 'stock': 10, 'modelo': 'X1'}







empleado = {
    "nombre": "Carlos",
    "puesto": "Desarrollador",
    "departamento": "Tecnología",
    "antigüedad": 3
}

# Iterar sobre pares clave-valor
for clave, valor in empleado.items():
    print(f"{clave}: {valor}")

# Salida:
# nombre: Carlos
# puesto: Desarrollador
# departamento: Tecnología
# antigüedad: 3




configuracion = {
    "idioma": "es",
    "tema": "oscuro",
    "notificaciones": True,
    "autoguardado": 5
}

# Obtener todas las claves
claves = configuracion.keys()
print(list(claves))  # ['idioma', 'tema', 'notificaciones', 'autoguardado']





formulario_requerido = {"nombre", "email", "teléfono"}
datos_enviados = {"nombre": "Laura", "email": "laura@ejemplo.com", "ciudad": "Valencia"}

# Verificar campos faltantes
campos_faltantes = formulario_requerido - set(datos_enviados.keys())

if campos_faltantes:
    print(f"Faltan los siguientes campos: {', '.join(campos_faltantes)}")
else:
    print("Todos los campos requeridos están presentes")

# Salida: Faltan los siguientes campos: teléfono










calificaciones = {
    "Matemáticas": 85,
    "Historia": 92,
    "Ciencias": 78,
    "Literatura": 90
}

# Obtener todos los valores
notas = calificaciones.values()
print(list(notas))  # [85, 92, 78, 90]

# Calcular el promedio
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")  # Promedio: 86.25







ventas_por_producto = {
    "producto_a": 120,
    "producto_b": 85,
    "producto_c": 250,
    "producto_d": 35
}

# Análisis básico de ventas
total_ventas = sum(ventas_por_producto.values())
venta_maxima = max(ventas_por_producto.values())
venta_minima = min(ventas_por_producto.values())

print(f"Total de ventas: {total_ventas}")
print(f"Venta más alta: {venta_maxima}")
print(f"Venta más baja: {venta_minima}")

# Encontrar productos con ventas superiores a 100
productos_exitosos = [producto for producto, ventas in ventas_por_producto.items() 
                     if ventas > 100]
print(f"Productos con más de 100 ventas: {productos_exitosos}")







# Datos de una tienda online
productos = {
    "SKU001": {"nombre": "Teclado", "precio": 45.99, "stock": 10},
    "SKU002": {"nombre": "Monitor", "precio": 199.99, "stock": 5},
    "SKU003": {"nombre": "Mouse", "precio": 25.50, "stock": 15},
    "SKU004": {"nombre": "Auriculares", "precio": 89.99, "stock": 8}
}

# 1. Encontrar productos con poco stock (menos de 10 unidades)
poco_stock = {
    codigo: info["nombre"] 
    for codigo, info in productos.items() 
    if info["stock"] < 10
}
print("Productos con poco stock:", poco_stock)

# 2. Calcular el valor total del inventario
valor_inventario = sum(
    info["precio"] * info["stock"] 
    for info in productos.values()
)
print(f"Valor total del inventario: ${valor_inventario:.2f}")

# 3. Actualizar precios con un descuento del 10%
for producto in productos.values():
    producto.update({"precio": producto["precio"] * 0.9})

# Verificar los nuevos precios
for codigo, info in productos.items():
    print(f"{info['nombre']}: ${info['precio']:.2f}")





