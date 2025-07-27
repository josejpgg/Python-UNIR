# Creando un conjunto con elementos duplicados
numeros = {1, 2, 3, 2, 1, 4, 5, 4}
print(numeros)  # Salida: {1, 2, 3, 4, 5}






frutas = {"manzana", "naranja", "plátano"}
print("manzana" in frutas)  # True
print("pera" not in frutas)  # True







a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

# Verificar si a es subconjunto de b
print(a.issubset(b))  # True
print(a <= b)         # True (operador alternativo)

# Verificar si b es superconjunto de a
print(b.issuperset(a))  # True
print(b >= a)           # True (operador alternativo)

# Subconjunto propio (a es subconjunto de b pero no son iguales)
print(a < b)  # True







a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

print(a.isdisjoint(b))  # True (no tienen elementos en común)
print(a.isdisjoint(c))  # False (comparten el elemento 3)







colores = {"rojo", "verde", "azul", "amarillo"}
print(len(colores))  # 4







# Idempotencia: A ∪ A = A y A ∩ A = A
# Conmutatividad: A ∪ B = B ∪ A y A ∩ B = B ∩ A
# Asociatividad: (A ∪ B) ∪ C = A ∪ (B ∪ C) y (A ∩ B) ∩ C = A ∩ (B ∩ C)
# Distributividad: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)







# Conjunto vacío (¡NO usar {} para esto!)
conjunto_vacio = set()
print(type(conjunto_vacio))  # <class 'set'>

# Esto crearía un diccionario, no un conjunto:
diccionario_vacio = {}
print(type(diccionario_vacio))  # <class 'dict'>







# Crear conjunto a partir de una lista
numeros_lista = [1, 2, 3, 2, 1, 4]
numeros_conjunto = set(numeros_lista)
print(numeros_conjunto)  # {1, 2, 3, 4}

# Crear conjunto a partir de una cadena
letras = set("mississippi")
print(letras)  # {'m', 'i', 's', 'p'}







frutas = {"manzana", "naranja"}
frutas.add("plátano")
print(frutas)  # {'manzana', 'naranja', 'plátano'}

# Añadir un elemento que ya existe no tiene efecto
frutas.add("manzana")
print(frutas)  # {'manzana', 'naranja', 'plátano'}








frutas = {"manzana", "naranja"}
frutas.update(["plátano", "kiwi", "mango"])
print(frutas)  # {'manzana', 'naranja', 'plátano', 'kiwi', 'mango'}

# También podemos actualizar con varios iterables a la vez
frutas.update(("fresa", "cereza"), {"uva", "melón"})
print(frutas)  # {'manzana', 'naranja', 'plátano', 'kiwi', 'mango', 'fresa', 'cereza', 'uva', 'melón'}







numeros = {1, 2, 3, 4, 5}
numeros.remove(3)
print(numeros)  # {1, 2, 4, 5}

# Esto lanzaría un KeyError
# numeros.remove(10)













numeros = {1, 2, 3, 4, 5}
numeros.discard(3)
print(numeros)  # {1, 2, 4, 5}

# No genera error si el elemento no existe
numeros.discard(10)
print(numeros)  # {1, 2, 4, 5}






numeros = {0, 1, 2, 3, 4, 5}
elemento = numeros.pop()
print(f"Primer Elemento eliminado: {elemento}")
print(f"Conjunto resultante: {numeros}")







original = {1, 2, 3}
copia = original.copy()

# Modificar la copia no afecta al original
copia.add(4)
print(original)  # {1, 2, 3}
print(copia)     # {1, 2, 3, 4}








# Conjunto a lista
numeros = {1, 2, 3, 4, 5}
lista_numeros = list(numeros)
print(lista_numeros)  # [1, 2, 3, 4, 5] (el orden puede variar)

# Conjunto a tupla
tupla_numeros = tuple(numeros)
print(tupla_numeros)  # (1, 2, 3, 4, 5) (el orden puede variar)











animales = {"perro", "gato", "pájaro", "pez"}
print(len(animales))  # 4








lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

# Elementos únicos en lista1 (no presentes en lista2)
unicos_lista1 = set(lista1) - set(lista2)
print(unicos_lista1)  # {1, 2, 3}







def tienen_elementos_comunes(lista1, lista2):
    return not set(lista1).isdisjoint(set(lista2))

print(tienen_elementos_comunes([1, 2, 3], [3, 4, 5]))  # True
print(tienen_elementos_comunes([1, 2, 3], [4, 5, 6]))  # False









# Definimos dos conjuntos
estudiantes_python = {"Ana", "Carlos", "Elena", "David"}
estudiantes_java = {"Elena", "David", "Fernando", "Gabriela"}

# Unión usando el método union()
todos_estudiantes = estudiantes_python.union(estudiantes_java)
print(todos_estudiantes)  # {'Ana', 'Carlos', 'Elena', 'David', 'Fernando', 'Gabriela'}

# Unión usando el operador |
todos_estudiantes = estudiantes_python | estudiantes_java
print(todos_estudiantes)  # {'Ana', 'Carlos', 'Elena', 'David', 'Fernando', 'Gabriela'}








estudiantes_javascript = {"Héctor", "Irene", "Ana"}

# Unión de tres conjuntos
todos = estudiantes_python | estudiantes_java | estudiantes_javascript
print(todos)  # {'Ana', 'Carlos', 'Elena', 'David', 'Fernando', 'Gabriela', 'Héctor', 'Irene'}

# También funciona con el método union() pasando múltiples argumentos
todos = estudiantes_python.union(estudiantes_java, estudiantes_javascript)











# Usando los conjuntos anteriores
# Estudiantes que toman ambos cursos (Python y Java)
estudiantes_ambos = estudiantes_python.intersection(estudiantes_java)
print(estudiantes_ambos)  # {'Elena', 'David'}

# Usando el operador &
estudiantes_ambos = estudiantes_python & estudiantes_java
print(estudiantes_ambos)  # {'Elena', 'David'}












# Estudiantes que solo toman Python (no Java)
solo_python = estudiantes_python.difference(estudiantes_java)
print(solo_python)  # {'Ana', 'Carlos'}

# Usando el operador -
solo_python = estudiantes_python - estudiantes_java
print(solo_python)  # {'Ana', 'Carlos'}

# Estudiantes que solo toman Java (no Python)
solo_java = estudiantes_java - estudiantes_python
print(solo_java)  # {'Fernando', 'Gabriela'}









# Estudiantes que toman Python o Java, pero no ambos
exclusivos = estudiantes_python.symmetric_difference(estudiantes_java)
print(exclusivos)  # {'Ana', 'Carlos', 'Fernando', 'Gabriela'}

# Usando el operador ^
exclusivos = estudiantes_python ^ estudiantes_java
print(exclusivos)  # {'Ana', 'Carlos', 'Fernando', 'Gabriela'}










# Unión in-place (update)
grupo_a = {1, 2, 3}
grupo_b = {3, 4, 5}
grupo_a.update(grupo_b)  # Equivalente a grupo_a |= grupo_b
print(grupo_a)  # {1, 2, 3, 4, 5}

# Intersección in-place (intersection_update)
grupo_a = {1, 2, 3, 4}
grupo_b = {3, 4, 5, 6}
grupo_a.intersection_update(grupo_b)  # Equivalente a grupo_a &= grupo_b
print(grupo_a)  # {3, 4}

# Diferencia in-place (difference_update)
grupo_a = {1, 2, 3, 4}
grupo_b = {3, 4, 5, 6}
grupo_a.difference_update(grupo_b)  # Equivalente a grupo_a -= grupo_b
print(grupo_a)  # {1, 2}

# Diferencia simétrica in-place (symmetric_difference_update)
grupo_a = {1, 2, 3, 4}
grupo_b = {3, 4, 5, 6}
grupo_a.symmetric_difference_update(grupo_b)  # Equivalente a grupo_a ^= grupo_b
print(grupo_a)  # {1, 2, 5, 6}















