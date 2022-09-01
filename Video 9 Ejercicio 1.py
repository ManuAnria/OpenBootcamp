lista = []
agregar = False

while not agregar:
    paises = input("Ingrese un país: ").capitalize()
    lista.append(paises)
    lista_rev = set(lista)

    continuar = input("¿Desea continuar? (S/N): ").upper()
    if continuar == "N":
        agregar = True

    elif continuar == "S":
        agregar = False

    else:
        print("Error. Ingrese una opción válida.")
        agregar = False

print(f'La lista de paises ordenada y sin duplicados: {sorted(lista_rev)}')


