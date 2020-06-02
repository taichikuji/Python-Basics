demo_list = [1, 'hola', 1.34, True, [1, 2, 3]]
colors = ['red', 'yellow', 'black']

numbers_list = list((1, 2, 3, 4))

print(numbers_list)
# print(type(numbers_list))

# para crear un rango, se puede usar "range(primer valor, segundo valor)"
# esto se puede combinar con list para generar una lista con estos valores.
r = list(range(1, 10))
print(r)

# opciones que se puede utilizar con una lista.
print(dir(colors))
# muestra la posicion de una lista
print(colors[0])
# muestra en True / False si el valor existe en la lista
print('red' in colors)

# cambia el valor de una opción dentro de una lista
colors[0] = 'negro'

# añade un valor a la lista
colors.append('violet')

# print(colors)
# añadir varios valores a la lista
colors.extend(['pink', 'hai'])
# insertar en una posición concreta un valor en una lista
colors.insert(1, 'valor')
# insertar en una ultima posición un valor en la lista
colors.insert(len(colors), 'ultimo')
# eliminar el ultimo valor
colors.pop()

# eliminar basado en nombre
colors.remove('negro')
# eliminar basado en posición: pop(posicion)
colors.pop(1)

# eliminar todos los valores de una lista, sin eliminar la lista
colors.clear()

# ordenar la lista de manera inversa
colors.sort(reverse=True)

print(colors.index('yellow'))