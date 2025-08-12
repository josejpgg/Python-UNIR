def funcion(param_normal, *args):
    # Código de la función
    pass






def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Podemos llamar a la función con cualquier cantidad de argumentos
print(sumar(1, 2))           # 3
print(sumar(1, 2, 3, 4, 5))  # 15
print(sumar())               # 0 (no hay argumentos)








def describir_persona(nombre, edad, *habilidades):
    mensaje = f"{nombre} tiene {edad} años y sus habilidades son:"
    
    if not habilidades:
        return mensaje + " ninguna habilidad registrada."
    
    lista_habilidades = ", ".join(habilidades)
    return mensaje + f" {lista_habilidades}."

# Usando la función con diferentes cantidades de argumentos
print(describir_persona("Ana", 28, "Python", "SQL", "JavaScript"))
# Ana tiene 28 años y sus habilidades son: Python, SQL, JavaScript.

print(describir_persona("Carlos", 35))
# Carlos tiene 35 años y sus habilidades son: ninguna habilidad registrada.








def multiplicar(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

# Lista de números
valores = [2, 3, 4, 5]

# Desempaquetando la lista como argumentos individuales
print(multiplicar(*valores))  # 120 (2*3*4*5)

# También funciona con tuplas
mas_valores = (10, 20)
print(multiplicar(*mas_valores))  # 200 (10*20)










def log_llamada(funcion):
    def wrapper(*args):
        print(f"Llamando a {funcion.__name__} con {len(args)} argumentos")
        resultado = funcion(*args)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@log_llamada
def sumar_cuadrados(*numeros):
    return sum(x**2 for x in numeros)

sumar_cuadrados(1, 2, 3)
# Llamando a sumar_cuadrados con 3 argumentos
# Resultado: 14











def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Podemos pasar cualquier cantidad de argumentos con nombre
mostrar_informacion(nombre="Ana", edad=28, ciudad="Madrid")
# nombre: Ana
# edad: 28
# ciudad: Madrid

# O incluso ninguno
mostrar_informacion()
# (no muestra nada)









def crear_conexion_bd(**opciones):
    # Valores por defecto
    config = {
        "host": "localhost",
        "puerto": 3306,
        "usuario": "admin",
        "contraseña": "",
        "base_datos": "app",
        "timeout": 30,
        "autocommit": True
    }
    
    # Actualizar con opciones proporcionadas
    config.update(opciones)
    
    print(f"Conectando a {config['base_datos']} en {config['host']}:{config['puerto']}")
    # Aquí iría el código real de conexión...
    
    return f"Conexión establecida con {config['base_datos']}"

# Diferentes formas de usar la función
crear_conexion_bd(host="db.servidor.com", usuario="root", contraseña="secreto")
# Conectando a app en db.servidor.com:3306











def formatear_datos(datos, **opciones_formato):
    formato = {
        "precision": 2,
        "separador": ",",
        "prefijo": "",
        "sufijo": "",
        "mostrar_unidades": False
    }
    formato.update(opciones_formato)
    
    resultado = formato["prefijo"]
    
    if isinstance(datos, (int, float)):
        resultado += f"{datos:.{formato['precision']}f}"
    elif isinstance(datos, list):
        resultado += formato["separador"].join(str(item) for item in datos)
    else:
        resultado += str(datos)
    
    if formato["mostrar_unidades"] and "unidades" in opciones_formato:
        resultado += f" {opciones_formato['unidades']}"
    
    resultado += formato["sufijo"]
    return resultado

# Ejemplos de uso
print(formatear_datos(123.456789))  # 123.46
print(formatear_datos(123.456789, precision=4, prefijo="$"))  # $123.4568
print(formatear_datos([1, 2, 3], separador=" | "))  # 1 | 2 | 3
print(formatear_datos(42.5, mostrar_unidades=True, unidades="kg", precision=1))  # 42.5 kg













def funcion(
    # 1. Parámetros posicionales obligatorios
    param_obligatorio,
    
    # 2. Parámetros posicionales variables (*args)
    *args,
    
    # 3. Parámetros con nombre obligatorios (solo Python 3.8+)
    param_solo_nombre,
    
    # 4. Parámetros con valores por defecto
    param_opcional=valor_defecto,
    
    # 5. Parámetros con nombre variables (**kwargs)
    **kwargs
):
    # Cuerpo de la función
    pass














def analizar_datos(dataset, *metricas, normalizar=False, **opciones_grafico):
    """
    Analiza un conjunto de datos y genera gráficos.
    
    Args:
        dataset: El conjunto de datos a analizar (obligatorio).
        *metricas: Métricas a calcular (ej: "media", "mediana", "desviacion").
        normalizar: Si es True, normaliza los datos antes del análisis.
        **opciones_grafico: Opciones para personalizar los gráficos generados.
    
    Returns:
        Un diccionario con los resultados del análisis.
    """
    # Implementación...










