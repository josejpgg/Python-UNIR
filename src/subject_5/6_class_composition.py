# Enfoque con herencia (problemático)
class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def enviar(self):
        pass  # Método base

class NotificacionEmail(Notificacion):
    def enviar(self):
        print(f"Enviando email: {self.mensaje}")

class NotificacionSMS(Notificacion):
    def enviar(self):
        print(f"Enviando SMS: {self.mensaje}")

# ¿Y si queremos enviar por ambos medios? ¿Herencia múltiple?

# Enfoque con composición
class CanalNotificacion:
    def enviar(self, mensaje):
        pass

class CanalEmail(CanalNotificacion):
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")

class CanalSMS(CanalNotificacion):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

class Notificador:
    def __init__(self):
        self.canales = []
    
    def agregar_canal(self, canal):
        self.canales.append(canal)
    
    def enviar(self, mensaje):
        for canal in self.canales:
            canal.enviar(mensaje)

# Uso
notificador = Notificador()
notificador.agregar_canal(CanalEmail())
notificador.agregar_canal(CanalSMS())
notificador.enviar("¡Alerta importante!")  # Se envía por email y SMS


##### Usa herencia cuando:
# Existe una clara relación "es un"
# La clase hija no necesita cambiar el comportamiento de la clase padre
# No necesitas cambiar la implementación en tiempo de ejecución
##### Usa composición cuando:
# La relación es más bien "tiene un" o "usa un"
# Necesitas mayor flexibilidad para cambiar comportamientos
# Quieres evitar los problemas de la herencia múltiple
# Necesitas reutilizar código de clases no relacionadas















class Rueda:
    def __init__(self, tamaño, presion):
        self.tamaño = tamaño
        self.presion = presion
    
    def inflar(self, nueva_presion):
        self.presion = nueva_presion
        print(f"Rueda inflada a {self.presion} PSI")

class Bicicleta:
    def __init__(self, marca, modelo, tamaño_ruedas):
        self.marca = marca
        self.modelo = modelo
        # Relación uno a muchos: una bicicleta tiene varias ruedas
        self.ruedas = [Rueda(tamaño_ruedas, 0) for _ in range(2)]
    
    def inflar_ruedas(self, presion):
        print(f"Inflando ruedas de {self.marca} {self.modelo}")
        for i, rueda in enumerate(self.ruedas):
            print(f"Rueda {i+1}: ", end="")
            rueda.inflar(presion)

# Uso de la relación
mi_bici = Bicicleta("Trek", "Marlin 7", 29)
mi_bici.inflar_ruedas(35)






# Relaciones con diccionarios

class Componente:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
    
    def describir(self):
        return f"{self.nombre} ({self.peso}g)"

class Computadora:
    def __init__(self):
        # Relación uno a muchos con acceso por clave
        self.componentes = {}
    
    def agregar_componente(self, tipo, nombre, peso):
        self.componentes[tipo] = Componente(nombre, peso)
    
    def listar_componentes(self):
        print("Componentes de la computadora:")
        for tipo, componente in self.componentes.items():
            print(f"- {tipo}: {componente.describir()}")
    
    def peso_total(self):
        return sum(c.peso for c in self.componentes.values())

# Uso de la relación
mi_pc = Computadora()
mi_pc.agregar_componente("CPU", "Intel i7-12700K", 125)
mi_pc.agregar_componente("GPU", "NVIDIA RTX 3080", 750)
mi_pc.agregar_componente("RAM", "Corsair Vengeance 32GB", 150)

mi_pc.listar_componentes()
print(f"Peso total: {mi_pc.peso_total()}g")















class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []  # Relación uno a muchos con Empleado
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        # Establecemos la relación bidireccional
        empleado.departamento = self
    
    def listar_empleados(self):
        print(f"Empleados en {self.nombre}:")
        for empleado in self.empleados:
            print(f"- {empleado.nombre}")

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamento = None  # Relación uno a uno con Departamento
    
    def cambiar_departamento(self, nuevo_departamento):
        # Eliminamos al empleado del departamento actual
        if self.departamento:
            self.departamento.empleados.remove(self)
        
        # Establecemos la nueva relación
        nuevo_departamento.agregar_empleado(self)

# Uso de la relación bidireccional
rrhh = Departamento("Recursos Humanos")
tecnologia = Departamento("Tecnología")

ana = Empleado("Ana García")
juan = Empleado("Juan Pérez")
maria = Empleado("María López")

rrhh.agregar_empleado(ana)
tecnologia.agregar_empleado(juan)
tecnologia.agregar_empleado(maria)

print("Situación inicial:")
rrhh.listar_empleados()
tecnologia.listar_empleados()

print("\nDespués de cambio:")
ana.cambiar_departamento(tecnologia)
rrhh.listar_empleados()
tecnologia.listar_empleados()













class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def encender(self):
        print(f"Motor {self.tipo} encendido")

class Transmision:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def cambiar_marcha(self, marcha):
        print(f"Cambiando a marcha {marcha} en transmisión {self.tipo}")

class Vehiculo:
    def __init__(self, motor, transmision):
        # Inyección de dependencias
        self.motor = motor
        self.transmision = transmision
    
    def iniciar_marcha(self):
        self.motor.encender()
        self.transmision.cambiar_marcha(1)
        print("Vehículo en movimiento")

# Creamos los componentes por separado
motor_diesel = Motor("diésel", 180)
transmision_automatica = Transmision("automática")

# Inyectamos los componentes al crear el vehículo
camioneta = Vehiculo(motor_diesel, transmision_automatica)
camioneta.iniciar_marcha()

# Podemos reutilizar componentes
motor_electrico = Motor("eléctrico", 250)
coche_electrico = Vehiculo(motor_electrico, transmision_automatica)
coche_electrico.iniciar_marcha()













class BaseDatos:
    def __init__(self, conexion_string):
        self.conexion_string = conexion_string
        print(f"Configurando conexión a {conexion_string}")
        # No conectamos inmediatamente
        self._conexion = None
    
    @property
    def conexion(self):
        # Inicialización perezosa: solo conectamos cuando se necesita
        if self._conexion is None:
            print(f"Conectando a {self.conexion_string}...")
            # Aquí iría el código real de conexión
            self._conexion = f"Conexión activa a {self.conexion_string}"
        return self._conexion

class Aplicacion:
    def __init__(self, nombre):
        self.nombre = nombre
        # Configuramos la base de datos pero no conectamos todavía
        self.db = BaseDatos("postgresql://localhost/miapp")
    
    def procesar_datos(self):
        print(f"Aplicación {self.nombre} procesando datos...")
        # Aquí se establece la conexión por primera vez
        print(f"Usando {self.db.conexion}")

# La aplicación se inicia sin conectar a la base de datos
app = Aplicacion("GestorTareas")
print("Aplicación iniciada")

# La conexión se establece solo cuando se necesita
app.procesar_datos()

# En usos posteriores, se reutiliza la conexión existente
app.procesar_datos()

















