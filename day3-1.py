f = open("day3-1-puzzle-input.txt", "r")

horizontal = 3
vertical = 1

longueur_ligne = 31
compteur_horizontal = 0
nb_arbres = 0

for ligne in f:
    print(compteur_horizontal % longueur_ligne)
    if ligne[compteur_horizontal % longueur_ligne] == '#':
        nb_arbres += 1

    compteur_horizontal += 3

print(nb_arbres)
