# condicional if
try:
    x = input("Introduce un valor > ")
    if x < 30:
        print("x es menor que 30!")
    elif x > 30:
        print("x es mayor que 30!")
    else:
        print("x es 30!")
except TypeError:
    print("No es un número!")


name = input("Escribe un nombre > ")
surname = input("Escribe un apellido > ")

if name == "John":
    print("Tu eres John")
    if surname == "Zapato":
        print("Tu eres John Zapato")
    else:
        print("No eres John Zapato")
else:
    print(f"No eres John, eres {name} {surname}")
