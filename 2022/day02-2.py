f = open("day02-puzzle-input.txt", "r")

total = 0

score = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}


def partie(adversaire, resultat_attendu):
    resultat_affrontement = score[resultat_attendu]

    if adversaire == 'A':
        if resultat_attendu == 'X':
            choix = 3
        elif resultat_attendu == 'Y':
            choix = 1
        else:
            choix = 2
    elif adversaire == 'B':
        if resultat_attendu == 'X':
            choix = 1
        elif resultat_attendu == 'Y':
            choix = 2
        else:
            choix = 3
    else:
        if resultat_attendu == 'X':
            choix = 2
        elif resultat_attendu == 'Y':
            choix = 3
        else:
            choix = 1

    return resultat_affrontement + choix


for ligne in f:
    jeu = ligne.split()
    opponent = jeu[0]
    moi = jeu[1]
    resultat = partie(opponent, moi)
    total += resultat

print(total)
