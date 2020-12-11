from copy import deepcopy

f = open("day11-puzzle-input.txt", "r")

chaines = f.readlines()

sieges = []

for ligne in chaines:
    ligne_sieges = []
    for siege in ligne:
        if siege != "\n":
            ligne_sieges.append(siege)

    sieges.append(ligne_sieges)


def afficher(grille):
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            print(grille[i][j], end='')
        print("\n")


def grilles_egales(grille1, grille2):
    egales = True

    for i in grille1:
        for j in grille1[i]:
            if grille1[i][j] != grille2:
                egales = False

    return egales


def est_seul(grille, i, j):
    return "#" not in valeurs_visibles(grille, i, j)


def chercher_dans_direction_hg(grille, i, j):
    if grille[i][j] != '.':
        return grille[i][j]

    if i > 0 and j > 0:
        return chercher_dans_direction_hg(grille, i-1, j-1)

    return None


def chercher_dans_direction_h(grille, i, j):
    if grille[i][j] != '.':
        return grille[i][j]

    if j > 0:
        return chercher_dans_direction_hg(grille, i, j - 1)

    return None


def chercher_dans_direction_hd(grille, i, j):
    if grille[i][j] != '.':
        return grille[i][j]

    if i < len(grille) - 1 and j > 0:
        return chercher_dans_direction_hd(grille, i+1, j-1)

    return None


def chercher_dans_direction_g(grille, i, j):
    if grille[i][j] != '.':
        return grille[i][j]

    if i > 0:
        return chercher_dans_direction_g(grille, i-1, j)

    return None


def chercher_dans_direction_d(grille, i, j):
    if grille[i][j] != '.':
        return grille[i][j]

    if i < len(grille) - 1:
        return chercher_dans_direction_d(grille, i+1, j)

    return None


def chercher_dans_direction_bg(grille, i, j):
    if grille[i][j] != '.':
        return grille[i][j]

    if i > 0 and j < len(grille[i]) - 1:
        return chercher_dans_direction_bg(grille, i-1, j+1)

    return None


def chercher_dans_direction_b(grille, i, j):
    if grille[i][j] != '.':
        return grille[i][j]

    if j < len(grille[i]) - 1:
        return chercher_dans_direction_b(grille, i, j+1)

    return None


def chercher_dans_direction_bd(grille, i, j):
    if grille[i][j] != '.':
        return grille[i][j]

    if i < len(grille) - 1 and j < len(grille[i]) - 1:
        return chercher_dans_direction_bd(grille, i+1, j+1)

    return None


def valeurs_visibles(grille, i, j):
    valeurs = []

    if i > 0 and j > 0:
        valeurs.append(chercher_dans_direction_hg(grille, i-1, j-1))
    if i > 0:
        valeurs.append(chercher_dans_direction_g(grille, i-1, j))
    if i > 0 and j < len(grille[i]) - 1:
        valeurs.append(chercher_dans_direction_bg(grille, i-1, j+1))
    if j > 0:
        valeurs.append(chercher_dans_direction_h(grille, i, j-1))
    if j < len(grille[i]) - 1:
        valeurs.append(chercher_dans_direction_b(grille, i, j+1))
    if i < len(grille) - 1 and j > 0:
        valeurs.append(chercher_dans_direction_hd(grille, i+1, j-1))
    if i < len(grille) - 1:
        valeurs.append(chercher_dans_direction_d(grille, i+1, j))
    if i < len(grille) - 1 and j < len(grille[i]) - 1:
        valeurs.append(chercher_dans_direction_bd(grille, i+1, j+1))

    return valeurs


def est_entoure(grille, i, j):
    return valeurs_visibles(grille, i, j).count("#") >= 5


def iterer(grille):
    grille_initiale = deepcopy(grille)
    nouvelle_iteration = deepcopy(grille)

    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille_initiale[i][j] != ".":
                if est_seul(grille_initiale, i, j):
                    nouvelle_iteration[i][j] = "#"
                elif grille_initiale[i][j] == "#" and est_entoure(grille_initiale, i, j):
                    nouvelle_iteration[i][j] = "L"

    if grille_initiale == nouvelle_iteration:
        return nouvelle_iteration
    else:
        return iterer(nouvelle_iteration)


invariant = iterer(sieges)
afficher(invariant)

total = 0
for ligne in invariant:
    total += ligne.count("#")

print(total)
