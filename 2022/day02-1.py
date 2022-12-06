f = open("day02-puzzle-input.txt", "r")

total = 0

score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def partie(adversaire, moi):
    choix = score[moi]

    if adversaire == 'A':
        if moi == 'X':
            affrontement = 3
        elif moi == 'Y':
            affrontement = 6
        else:
            affrontement = 0
    elif adversaire == 'B':
        if moi == 'X':
            affrontement = 0
        elif moi == 'Y':
            affrontement = 3
        else:
            affrontement = 6
    else:
        if moi == 'X':
            affrontement = 6
        elif moi == 'Y':
            affrontement = 0
        else:
            affrontement = 3

    return choix + affrontement


for ligne in f:
    jeu = ligne.split()
    opponent = jeu[0]
    moi = jeu[1]
    resultat = partie(opponent, moi)
    total += resultat

print(total)
