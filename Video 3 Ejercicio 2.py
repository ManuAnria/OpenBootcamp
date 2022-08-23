peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
IMC = round(peso / (altura ** 2), 2)

print(f"Tu índice de masa corporal es: {IMC}")