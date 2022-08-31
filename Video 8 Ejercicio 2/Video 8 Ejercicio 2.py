import pickle


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def getMarca(self):
        return self.marca


v1 = Vehiculo('Ford', 'Fiesta')
f = open('vehiculos.txt', 'wb')
pickle.dump(v1, f)
f.close()


f = open('vehiculos.txt', 'rb')
auto = pickle.load(f)
f.close()

print(type(auto))
print(auto.getMarca())






