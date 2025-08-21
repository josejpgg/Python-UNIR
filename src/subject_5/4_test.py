# Crea una clase llamada Contador que gestione un valor numérico. La clase debe implementar:

# Un atributo de clase contadores_creados que lleve la cuenta de cuántas instancias se han creado.

# Un método de instancia incrementar() que aumente el valor del contador en 1 y devuelva el nuevo valor.

# Un método de instancia decrementar() que disminuya el valor del contador en 1 y devuelva el nuevo valor. El contador nunca debe ser negativo.

# Un método de clase @classmethod llamado reiniciar_contador_global() que ponga a cero el contador de instancias creadas.

# Un método estático @staticmethod llamado es_par(numero) que devuelva True si el número proporcionado es par, o False en caso contrario.

# Puedes empezar con este esquema:

# class Contador:
#     # Atributo de clase para contar instancias
#     contadores_creados = 0
    
#     def __init__(self, valor_inicial=0):
#         # Completa el constructor
#         pass
        
#     # Implementa los métodos requeridos

class Contador:
	contadores_creados = 0

	def __init__(self, valor_inicial = 0):
		self.valor = max(0, valor_inicial)
		Contador.contadores_creados += 1

	def incrementar(self) -> int:
		self.valor += 1
		return self.valor

	def decrementar(self) -> int:
		if self.valor > 0:
			self.valor -= 1
		return self.valor

	@classmethod
	def reiniciar_contador_global(cls):
		cls.contadores_creados = 0

	@staticmethod
	def es_par(numero: int) -> bool:
		return numero % 2 == 0

contador1 = Contador()
contador2 = Contador()
Contador()
contador2.incrementar()
contador2.incrementar()
# contador2.decrementar()
print(Contador.contadores_creados)
print(Contador.es_par(contador2.valor))