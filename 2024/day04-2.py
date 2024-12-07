f = open("day04-puzzle-input.txt", "r")

grille = []
total = 0

for ligne in f:
    grille.append(ligne.replace('\n', ''))

length = len(grille)


def nb_xmas(x, y):
    if x == 0 or x == length - 1 or y == 0 or y == length - 1:
        return 0

    resultat = 0

    if grille[x-1][y-1] == 'M' and grille[x+1][y+1] == 'S':
        # M M
        #  A
        # S S
        if grille[x-1][y+1] == 'M' and grille[x+1][y-1] == 'S':
            resultat += 1

        # M S
        #  A
        # M S
        elif grille[x-1][y+1] == 'S' and grille[x+1][y-1] == 'M':
            resultat += 1

    elif grille[x-1][y-1] == 'S' and grille[x+1][y+1] == 'M':
        # S M
        #  A
        # S M
        if grille[x - 1][y + 1] == 'M' and grille[x + 1][y - 1] == 'S':
            resultat += 1

        # S S
        #  A
        # M M
        elif grille[x - 1][y + 1] == 'S' and grille[x + 1][y - 1] == 'M':
            resultat += 1

    return resultat


for i in range(length):
    for j in range(length):
        if grille[i][j] == 'A':
            total += nb_xmas(i, j)

print(total)
