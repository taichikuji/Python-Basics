foods = ['CPU', 'apple', 'food', 'carrot', 'cobblestone']

# normal loop
# index muestra el numero int de la posición de la lista, y después muestro el valor.
for food in foods:
    # utilizo f"text {value}" para hacer funcionar las variables dentro;
    print(f"food {foods.index(food)}: {food}")

print("x-----------------------------x")

# loop con break
for food in foods:
    print(food)
    if food == 'apple':
        # para mostrar que también se puede utilizar otra manera para mezclar texto con variables
        # se puede hacer lo siguiente;
        # hay que tener cuidado con este método porque
        # hay que específicar que tipo de valor queremos utilizar
        # si no queremos la posibilidad de que se rompa el codigo en algun momento
        print("Oh no, i found "+str(food)+" i'm going do die aa")
        break

print("x-----------------------------x")

# loop con continue
for food in foods:
    print(food)
    if food == 'apple':
        # apple no se mostrará, pero el loop no se rompe
        print("Como tengo un 'continue', este valor se ignora pero continua el loop")
        continue

print("x-----------------------------x")

# loop con rango
# esto escribe un valor desde 1 hasta 9
for number in range(1, 9):
    print(number)

print("x-----------------------------x")

# esto escribe un valor desde la primera letra hasta la ultima
for letra in "HOLA QUE TAL!":
    print(letra)

print("x-----------------------------x")

contador = 0
# while seguirá imprimiendo hasta que el while se cumpla
while contador <= 10:
    print(contador)
    contador = contador + 1

print("x-----------------------------x")

# loop while infinito
# como while NUNCA se cumple, no parará de repetirse hasta que se termine el proceso manualmente
# este apartado está comentado para evitar problemas con el script
# descomenta la siguiente parte para ver como funciona el loop while infinito

# infinito = 1
# while infinito > 0:
#    print(infinito, end=" ")
#    infinito += 1
