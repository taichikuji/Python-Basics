x = (1, 2, 3, 4)
# tuples no pueden ser modificadas.
print(x[0])

# esto nos dará un error, ya que son inmutables
# x[4] = 10

# esto también nos dará un error ya que se ha eliminado antes de mostrar el valor
# del x
# sin el "del" podremos ver la lista entera de la siguiente manera
print(x)

# para mostrar tuples de un solo elemento, podemos hacer lo siguiente;
y = (1,)
print(y)

# libreria usando tuples dentro de un diccionario
locations = {
    (35.12312, 39.000): "Tokyo",
    (35.12312, 39.000): "New York",
}
print(type(locations))
