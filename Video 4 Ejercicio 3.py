lista = []
for i in range(1,101):
    lista.append(i)
    lista.sort(reverse=True)

print(*lista, sep="\n")
