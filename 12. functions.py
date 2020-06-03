# def permite crear una función
# def hello(name)
# hello es el nombre de la función
# name es el valor que se espera
# si se introduce un valor de la siguiente manera;
# hello(name="valor")
# el "valor" será el valor por defecto que se utilizará si no ponemos ningun valor esperado
def hello(name="don nadie"):
    print("HOLA " + name)

# pequeño ejemplo de calculadora;


def sumar(value1, value2):
    return value1 + value2


def restar(value1, value2):
    return value1 + value2


def multiplicar(value1, value2):
    return value1 * value2


def dividir(value1, value2):
    return value1 / value2


# como podemos ver, necesita de un integer o float para funcionar, y si escribimos un str...
# no funcionará.
print(sumar("3", "4"))
# este es solo un ejemplo, pero se puede hacer algo como lo siguiente para hacerlo funcionar;


# de nuevo, se puede mejorar, pero es para tener una idea de las cosas que se pueden hacer.
def sumarfloat(value1, value2):
    try:
        value1 = float(value1)
        value2 = float(value2)
        return value1 + value2
    except:
        return("Valor no compatible")


# de esta manera podremos hacer alguna tontería como la siguiente y aún así debería funcionar;
print(sumarfloat(1, "30"))
# además también podríamos escribir texto para que nos saltase el error en vez de que el codigo se rompa
print(sumarfloat("hola", "texto"))
