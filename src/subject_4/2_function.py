def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base: La longitud de la base del rectángulo.
        altura: La altura del rectángulo.
        
    Returns:
        El área del rectángulo.
    """
    return base * altura








print(calcular_area_rectangulo.__doc__)
# O también:
help(calcular_area_rectangulo)










def operacion_matematica(x, y):
    def sumar():
        return x + y
        
    def multiplicar():
        return x * y
    
    # Podemos usar las funciones anidadas
    suma = sumar()
    producto = multiplicar()
    
    return f"Suma: {suma}, Producto: {producto}"











def crear_contador():
    """
    Crea y devuelve una función contador que
    incrementa su valor en cada llamada.
    
    Returns:
        Una función que actúa como contador.
    """
    contador = 0
    
    def incrementar():
        """Incrementa y devuelve el valor del contador."""
        nonlocal contador
        contador += 1
        return contador
        
    return incrementar

# Crear un contador
mi_contador = crear_contador()

# Usar el contador
print(mi_contador())  # Imprime: 1
print(mi_contador())  # Imprime: 2
print(mi_contador())  # Imprime: 3








def sumar_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Podemos pasar cualquier cantidad de argumentos
print(sumar_numeros(1, 2))  # 3
print(sumar_numeros(1, 2, 3, 4, 5))  # 15
print(sumar_numeros())  # 0








def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Podemos pasar cualquier cantidad de argumentos con nombre
mostrar_informacion(nombre="Python", version=3.13, lanzamiento=2024)
# Imprime:
# nombre: Python
# version: 3.13
# lanzamiento: 2024










class Configuracion:
  DEBUG = True
  MAX_USUARIOS = 100
  RUTA_BASE = "/var/www/app"

# Uso:
if Configuracion.DEBUG:
  print("Modo depuración activado")









