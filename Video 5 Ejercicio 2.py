from typing import Union


def esprimo(n) -> Union[bool, str]:
    try:
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    except TypeError:
        return "El valor ingresado no es un número entero"


print(esprimo(18))
print(esprimo(7))
print(esprimo(1))
print(esprimo(2))
print(esprimo(3))
print(esprimo(4.5))