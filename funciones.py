import math

def primo(num):
    if num < 0:
        return 'No se permiten números negativos.'

    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True



def cubica(a):
    return a * a * a


def saludo(name):
    return "Hola, " + name

def cambio():
    return "el cambio"

primo(21)

primo(0)
primo(20)
primo(5888)
primo(78)