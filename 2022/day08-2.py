f = open("day08-puzzle-input.txt", "r")

grille = []

for ligne_chiffres in f:
    ligne = []

    for g in ligne_chiffres.strip():
        ligne.append(int(g))

    grille.append(ligne)

longueur = len(grille[0])


def batir_haut(x, y):
    result = []

    for k in range(x):
        result.append(grille[k][y])

    return result


def batir_bas(x, y):
    result = []

    for k in range(x + 1, longueur):
        result.append(grille[k][y])

    return result


def find_nb(val, list):
    k = 0
    cont = True

    while k < len(list) and cont:
        if list[k] >= val:
            cont = False
        k += 1

    return k


scenic = []

for i in range(longueur):
    scenic_ligne = []
    for j in range(longueur):
        if i == 0 or j == 0 or i == longueur-1 or j == longueur-1:
            scenic_ligne.append(0)
        else:
            val = grille[i][j]

            gauche = (grille[i][:j])[::-1]
            droite = grille[i][j+1:]
            haut = (batir_haut(i, j))[::-1]
            bas = batir_bas(i, j)

            result = find_nb(val, gauche) * find_nb(val, droite) * find_nb(val, haut) * find_nb(val, bas)
            scenic_ligne.append(result)

    scenic.append(scenic_ligne)

print(scenic)

maximum = 0

for i in range(longueur):
    for j in range(longueur):
        if scenic[i][j] > maximum:
            maximum = scenic[i][j]

print(maximum)

