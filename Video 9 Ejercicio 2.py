from functools import reduce

numeros = []

for i in range(1, 21):
    numeros.append(i)


def impares(x):
    if x % 2 != 0:
        return True

    return False


resultado = list(filter(impares, numeros))
suma = reduce(lambda x, y: x + y, resultado)

print(f'Lista de numeros: {numeros}')
print(f'Los numeros impares de la lista son: {list(resultado)}')
print(f'La suma de los números impares es: {suma}')

