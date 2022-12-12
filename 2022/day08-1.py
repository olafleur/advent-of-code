f = open("day08-puzzle-input.txt", "r")

grille = []

for ligne_chiffres in f:
    ligne = []

    for g in ligne_chiffres.strip():
        ligne.append(int(g))

    grille.append(ligne)

longueur = len(grille[0])

visible = []


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


def is_visible(val, ligne):
    result = list(filter(lambda x: x >= val, ligne))
    return len(result) == 0


for i in range(longueur):
    visibilite_ligne = []
    for j in range(longueur):
        if i == 0 or j == 0 or i == longueur-1 or j == longueur-1:
            visibilite_ligne.append(True)
        else:
            val = grille[i][j]

            gauche = grille[i][:j]
            droite = grille[i][j+1:]
            haut = batir_haut(i, j)
            bas = batir_bas(i, j)

            if is_visible(val, gauche) or is_visible(val, droite) or is_visible(val, haut) or is_visible(val, bas):
                # print('val ' + str(val) + ' is visible')
                visibilite_ligne.append(True)
            else:
                # print('val ' + str(val) + ' not')
                visibilite_ligne.append(False)

    visible.append(visibilite_ligne)

print(visible)

compte = 0

for i in range(longueur):
    for j in range(longueur):
        if visible[i][j]:
            compte += 1

print(compte)
