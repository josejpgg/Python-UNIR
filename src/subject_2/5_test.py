lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]
lista1 = set(lista1)
lista2 = set(lista2)
interseccion = lista1 & lista2
diferencia1 = lista1 - lista2
diferencia2 = lista2 - lista1
union = lista1 | lista2
print(interseccion)
print(diferencia1)
print(diferencia2)
print(union)