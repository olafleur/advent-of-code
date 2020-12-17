f = open("day17-puzzle-input.txt", "r")

contenu = f.readlines()
actifs = []
min_x = -1
max_x = 8
min_y = -1
max_y = 8
min_z = -1
max_z = 1

for i in range(len(contenu)):
    for j in range(len(contenu)):
        if contenu[i][j] == "#":
            actifs.append((i, j, 0))


def somme_tuple(tuple1, tuple2):
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1], tuple1[2] + tuple2[2]


def voisins_actifs(etat, x, y, z):
    voisins_actifs = []
    possibilites = [(x, y, z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]
    possibilites.remove((0, 0, 0))

    for possibilite in possibilites:
        addition = somme_tuple((x, y, z), possibilite)
        if addition in etat:
            voisins_actifs.append(addition)

    return voisins_actifs


def maximum_des_x(etat):
    maximum_x = 0

    for truc in etat:
        if truc[0] + 1 > maximum_x:
            maximum_x = truc[0] + 1

    return maximum_x


def maximum_des_y(etat):
    maximum_y = 0

    for truc in etat:
        if truc[1] + 1 > maximum_y:
            maximum_y = truc[1] + 1

    return maximum_y


def maximum_des_z(etat):
    maximum_z = 0

    for truc in etat:
        if truc[2] + 1 > maximum_z:
            maximum_z = truc[2] + 1

    return maximum_z


def minimum_des_x(etat):
    minimum_x = 0

    for truc in etat:
        if truc[0] - 1 < minimum_x:
            minimum_x = truc[0] - 1

    return minimum_x


def minimum_des_y(etat):
    minimum_y = 0

    for truc in etat:
        if truc[1] - 1 < minimum_y:
            minimum_y = truc[1] - 1

    return minimum_y


def minimum_des_z(etat):
    minimum_z = 0

    for truc in etat:
        if truc[2] - 1 < minimum_z:
            minimum_z = truc[2] - 1

    return minimum_z


def iterer(etat_initial):
    nouvel_etat = []
    global max_x, max_y, max_z
    global min_x, min_y, min_z

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                les_voisins_actifs = voisins_actifs(etat_initial, x, y, z)
                if (x, y, z) in etat_initial and (len(les_voisins_actifs) == 2 or len(les_voisins_actifs) == 3):
                    nouvel_etat.append((x, y, z))
                if (x, y, z) not in etat_initial and len(les_voisins_actifs) == 3:
                    nouvel_etat.append((x, y, z))

    if maximum_des_x(nouvel_etat) > max_x:
        max_x = maximum_des_x(nouvel_etat)

    if maximum_des_y(nouvel_etat) > max_y:
        max_y = maximum_des_y(nouvel_etat)

    if maximum_des_z(nouvel_etat) > max_z:
        max_z = maximum_des_z(nouvel_etat)

    if minimum_des_x(nouvel_etat) < min_x:
        min_x = minimum_des_x(nouvel_etat)

    if minimum_des_y(nouvel_etat) < min_y:
        min_y = minimum_des_y(nouvel_etat)

    if minimum_des_z(nouvel_etat) < min_z:
        min_z = minimum_des_z(nouvel_etat)

    return nouvel_etat


for i in range(6):
    actifs = iterer(actifs)

print(len(actifs))
