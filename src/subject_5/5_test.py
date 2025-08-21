# Crea una jerarquía de clases para modelar vehículos. Debes implementar:

# Una clase base Vehiculo con los siguientes atributos y métodos:
# Atributos: marca, modelo y año
# Un método mostrar_info() que devuelva un string con la información básica del vehículo
# Una clase derivada Automovil que herede de Vehiculo y añada:
# Un atributo adicional puertas (número de puertas)
# Sobrescribe el método mostrar_info() para incluir el número de puertas
# Una clase derivada Motocicleta que herede de Vehiculo y añada:
# Un atributo adicional cilindrada (en cc)
# Sobrescribe el método mostrar_info() para incluir la cilindrada
# Finalmente, crea una instancia de cada clase derivada y muestra su información usando el método mostrar_info().

class Vehiculo:

	def __init__(self, marca, modelo, ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano

	def __str__(self):
		return f"marca={self.marca}, modelo={self.modelo}, año={self.ano}"

	def mostrar_info(self):
		return self.__str__()

class Automovil(Vehiculo):

	def __init__(self, marca, modelo, ano, numero_puertas):
		super().__init__(marca, modelo, ano)
		self.numero_puertas = numero_puertas

	def mostrar_info(self):
		return f"{self.__str__()} número de puertas={self.numero_puertas}"

class Motocicleta(Vehiculo):

	def __init__(self, marca, modelo, ano, cilindrada):
		super().__init__(marca, modelo, ano)
		self.cilindrada = cilindrada

	def mostrar_info(self):
		return f"{self.__str__()} cilindrada={self.cilindrada}"

automovil = Automovil("Toyota", "Corolla", 2020, 4)
motocicleta = Motocicleta("Honda", "CB500", 2019, 500)

print(automovil.mostrar_info())
print(motocicleta.mostrar_info())
