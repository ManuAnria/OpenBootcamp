import math


def area_tri(base, altura):
    return round((base * altura) / 2, 2)


print(area_tri(10, 5))


def area_circ(radio):
    return round(math.pi * (radio ** 2), 2)


print(area_circ(10))