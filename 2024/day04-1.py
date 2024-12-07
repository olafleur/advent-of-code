f = open("day04-puzzle-input.txt", "r")

grille = []
total = 0

for ligne in f:
    grille.append(ligne.replace('\n', ''))

length = len(grille)


def nb_xmas(x, y):
    espace_gauche = y >= 3
    espace_droite = y < length - 3
    espace_haut = x >= 3
    espace_bas = x < length - 3

    resultat = 0

    if espace_gauche:
        # SAMX
        if grille[x][y-1] == 'M' and grille[x][y-2] == 'A' and grille[x][y-3] == 'S':
            resultat += 1

    if espace_gauche and espace_haut:
        # S
        #  A
        #   M
        #    X
        if grille[x-1][y-1] == 'M' and grille[x-2][y-2] == 'A' and grille[x-3][y-3] == 'S':
            resultat += 1

    if espace_haut:
        # S
        # A
        # M
        # X
        if grille[x - 1][y] == 'M' and grille[x - 2][y] == 'A' and grille[x - 3][y] == 'S':
            resultat += 1

    if espace_haut and espace_droite:
        #    S
        #   A
        #  M
        # X
        if grille[x - 1][y + 1] == 'M' and grille[x - 2][y + 2] == 'A' and grille[x - 3][y + 3] == 'S':
            resultat += 1

    if espace_droite:
        # XMAS
        if grille[x][y + 1] == 'M' and grille[x][y + 2] == 'A' and grille[x][y + 3] == 'S':
            resultat += 1

    if espace_droite and espace_bas:
        # X
        #  M
        #   A
        #    S
        if grille[x + 1][y + 1] == 'M' and grille[x + 2][y + 2] == 'A' and grille[x + 3][y + 3] == 'S':
            resultat += 1

    if espace_bas:
        # X
        # M
        # A
        # S
        if grille[x + 1][y] == 'M' and grille[x + 2][y] == 'A' and grille[x + 3][y] == 'S':
            resultat += 1

    if espace_gauche and espace_bas:
        #    X
        #   M
        #  A
        # S
        if grille[x + 1][y - 1] == 'M' and grille[x + 2][y - 2] == 'A' and grille[x + 3][y - 3] == 'S':
            resultat += 1

    return resultat


for i in range(length):
    for j in range(length):
        if grille[i][j] == 'X':
            total += nb_xmas(i, j)

print(total)
