# Crear un programa que extraiga información específica de una cadena de texto


# Crea una función llamada extraer_info que reciba como parámetro una cadena
# de texto representando un correo electrónico con el formato nombre@dominio.extension
# La función debe devolver un diccionario con tres claves:

# nombre_usuario: la parte del correo antes del símbolo @
# dominio: la parte entre @ y el último punto
# extension: la parte después del último punto
# Por ejemplo, si la entrada es "usuario@ejemplo.com", la función debe devolver:

# {
#     "nombre_usuario": "usuario",
#     "dominio": "ejemplo",
#     "extension": "com"
# }
# Si la cadena no contiene el símbolo @ o no tiene extensión (un punto después del @),
# la función debe devolver un diccionario vacío.

# Utiliza los métodos de cadenas y técnicas de slicing que has aprendido para resolver
# este ejercicio.

def extraer_info(email: str) -> dict:
    if "@" not in email or "." not in email:
        return {}
    name = email.split("@")[0]
    domain_init = email.find("@") + 1
    domain_end = email.rfind(".")
    domain = email[domain_init:domain_end]
    extension = email[domain_end + 1:]
    return {
        "nombre_usuario": name,
        "dominio": domain,
        "extension": extension
    }

print(extraer_info("usuario@ejemplo.com"))
