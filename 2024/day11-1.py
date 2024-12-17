f = open("day11-puzzle-input.txt", "r")

ligne = f.readline().rstrip('\n').split()
chiffres = list(map(int, ligne))


def iterate(depart):
    resultat = []

    for chiffre in depart:
        if chiffre == 0:
            resultat.append(1)
        elif len(str(chiffre)) % 2 == 0:
            chaine = str(chiffre)
            longueur_moitie = len(chaine) // 2
            resultat.append(int(chaine[:longueur_moitie]))
            resultat.append(int(chaine[longueur_moitie:]))
        else:
            resultat.append(chiffre * 2024)

    return resultat


for i in range(25):
    chiffres = iterate(chiffres)

print(len(chiffres))
