f = open("day13-puzzle-input.txt", "r")

f.readline()  # ignorer

chaine = f.readline().split(',')

heures = []
les_bus = []
maximum = 0

for valeur in chaine:
    if valeur.isnumeric():
        nombre = int(valeur)

        if nombre > maximum:
            maximum = nombre

        les_bus.append(nombre)

        heures.append(nombre)
    else:
        heures.append(valeur)

les_bus.sort(reverse=True)

indices = []

for bus in les_bus:
    indices.append(heures.index(bus))

nb = maximum - indices[0]

trouve = False
a_sa_place = True
i = 0

while not trouve:
    while i < len(indices) and a_sa_place:
        if (nb + indices[i]) % les_bus[i] != 0:
            a_sa_place = False
        i += 1

    if a_sa_place:
        trouve = True

    nb += maximum
    i = 0
    a_sa_place = True

print(nb - maximum)
