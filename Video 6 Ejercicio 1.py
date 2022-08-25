class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


audi = Coche('rojo', 4, 5, 200, 100)


print(f"Color: {audi.color}")
print(f"Ruedas: {audi.ruedas}")
print(f"Puertas: {audi.puertas}")
print(f"Velocidad: {audi.velocidad}")
print(f"Cilindrada: {audi.cilindrada}")

