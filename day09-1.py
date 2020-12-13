f = open("day09-puzzle-input.txt", "r")

lignes = f.readlines()

entiers = list(map(lambda x: int(x), lignes))


def somme_est_dans(entier, liste):
    somme = False

    for i in range(len(liste)-1):
        for j in range(i, len(liste)):
            if liste[i] + liste[j] == entier:
                somme = True

    return somme


for i in range(25, len(entiers)):
    sous_liste = entiers[i-25:i]

    if not somme_est_dans(entiers[i], sous_liste):
        print(entiers[i])
