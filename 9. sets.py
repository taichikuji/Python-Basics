# sets sirven si quieres una lista de objetos sin ordenar
colors = {'Red', 'Green', 'Blue'}

print(type(colors))
print(colors)

print('Red' in colors)

# añade un valor al principio del set
colors.add('Violet')
print(colors)

# eliminar un valor basado en un elemento o variable introducido.
colors.remove('Violet')

# elimina el set entero
del colors
