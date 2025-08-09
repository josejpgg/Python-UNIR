
edad = 15

if edad >= 18:
    # Implementaremos esto más tarde
    pass
else:
    print("Acceso denegado")





# Asignar un valor predeterminado si la variable está vacía
nombre = ""
nombre_mostrar = nombre or "Invitado"  # Si nombre es vacío, usa "Invitado"

# Elegir el primer valor no vacío de una lista
primer_valor = "" or 0 or [] or "Hola" or 42  # primer_valor será "Hola"

# Ejecutar una función solo si una condición es verdadera
debug = True
debug and print("Información de depuración")  # Solo imprime si debug es True






# Mostrar diferentes mensajes según la condición
nombre = "Ana"
print(f"Hola {nombre}" if nombre else "Hola invitado")

# Ordenar una lista de forma ascendente o descendente
numeros = [5, 2, 8, 1]
orden_ascendente = True
numeros_ordenados = sorted(numeros, reverse=False if orden_ascendente else True)







# Operador ternario anidado
edad = 25
mensaje = "menor" if edad < 18 else ("adulto joven" if edad < 30 else "adulto")









# match expresion:
# 	case patrón1:
# 		# Código si expresión coincide con patrón1
# 	case patrón2:
# 		# Código si expresión coincide con patrón2
# 	case patrón3:
# 		# Código si expresión coincide con patrón3
# 	case _:
# 		# Código por defecto si no hay coincidencias


