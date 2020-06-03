# condicional if usando elif
# se utiliza try para saber si al escribir un valor, salta un error o no.
# Sabremos que no es un número si al interactuar con el valor nos salta un error.
# podremos hacer lo mismo con otros valores como floats o strings
try:
    x = float(input("Introduce un valor > "))
    if x < 30:
        print("x es menor que 30!")
    elif x > 30:
        print("x es mayor que 30!")
    else:
        print("x es 30!")
except:
    print("ERROR, value is not a number or couldn't be transformed")

name = input("Escribe un nombre > ")
surname = input("Escribe un apellido > ")

# condicional if usando and
if name == "John" and surname == "Zapato":
    print("Tu eres John Zapato")
else:
    print(f"No eres John Zapato, eres {name} {surname}")

# condicional if usando not
if (not(name == "John")):
    print("Valor no es John!")
# condicional if usando or
if (name == "John" or surname == "Zapato"):
    print("Tu nombre es John, o tu apellido es Zapato. Uno de los dos.")
