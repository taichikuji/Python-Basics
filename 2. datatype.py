# Strings
print("Hello World")
print('Hello World')
print('''Hello World''')
print("""Hello World""")

# Mostrar tipo de datatype es el siguiente contenido;
type("Hello World")

# Necesitamos "print(comando)" si queremos ver el output por pantalla terminal.
# Integer
print(type(100))
# Float
print(type(100.5))
# Boolean
print(type(True))
# Array | List | Los valores en su interior pueden ser modificados
print(type([10, 20, "Hello!", 50]))
# Tuples | Los valores en su interior no pueden ser modificados
print(type((10, 20, 30, "Hello!")))
# Dictionaries | Agrupar valores que pertenecen a una misma entidad
print(type({
    "Nombre":"Ryan", # "nombre vinculado a valor":"valor"
    "Apellido":"Ray",
    "Apodo":"Los Taichos"}))
# None
print(type(None))
# Juntar dos datatypes mediante "valor"+"valor"
print("Good"+"Job")
