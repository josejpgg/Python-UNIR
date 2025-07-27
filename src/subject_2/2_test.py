numeros = [10,20,30,40,50]
numeros.append(60)
numeros.insert(1,15)
numeros.remove(30)
suma = sum(num for num in numeros)
promedio = suma / len(numeros)
print(numeros)
print(suma)
print(promedio)
