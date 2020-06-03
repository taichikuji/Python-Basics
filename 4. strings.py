texto = "Hola"

# print(dir(texto))

# printa el texto en mayusculas
print(texto.upper())
# printa el texto en minusculas
print(texto.lower())
# reemplaza los caracteres en la primera zona de valores, y lo reemplaza por la segunda zona de valores.
print(texto.replace('Hola', 'bye'))
# cuenta cuantos caracteres existen con el valor introducido en la variable
print(texto.count('a'))
# muestra un true / false dependiendo si el valor a buscar existe en el principio de la variable introducida.
print(texto.startswith('Ho'))
# muestra un true / false dependiendo si el valor a buscar existe en el final de la variable introducida.
print(texto.endswith('Ho'))
# separa la variable tantas veces como aparezca el caracter introducido dentro de split() en una lista.
print(texto.split(','))
# muestra la posición del caracter dentro de find() en común con la variable.
print(texto.find('H'))
# busca la longitud de la variable
print(len(texto))
# muestra si la variable es numerico o alfa numerico
print(texto.isnumeric())
print(texto.isalpha())
# muestra la posición 3 de la variable usada
print(texto[3])  # a
# poner un valor negativo hace que muestre la posición desde el final.
print(texto[-3])  # o

print("Mi nombre es " + texto)
# equals
print(f"Mi nombre es {texto}")
# equals
print("Mi nombre es {0}".format(texto))
