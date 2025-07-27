contactos = {
    "persona1": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    "persona2": {"nombre": "Maria", "telefono": "45124124", "email": "maria@ejemplo.com"},
    "persona3": {"nombre": "Juan", "telefono": "65431221", "email": "juan@ejemplo.com"}
}
print(contactos['persona2']['email'])
contactos.update({"persona4": {"nombre": "Pedro", "telefono": "2222222", "email": "pedro@ejemplo.com"}
})
contactos['persona1']['telefono'] = '0000000'
for contacto in contactos.values():
    print(contacto['nombre'])