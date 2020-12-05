def calcul_nb_arbres(horizontal):
    longueur_ligne = 31
    compteur_horizontal = 0
    nb_arbres = 0

    f = open("day3-1-puzzle-input.txt", "r")

    for ligne in f:
        if ligne[compteur_horizontal % longueur_ligne] == '#':
            nb_arbres += 1

        compteur_horizontal += horizontal

    return nb_arbres


def calcul_2_1():
    longueur_ligne = 31
    compteur_vertical = 0
    compteur_horizontal = 0
    nb_arbres = 0

    f = open("day3-1-puzzle-input.txt", "r")

    for ligne in f:
        if compteur_vertical % 2 == 0:
            if ligne[compteur_horizontal % longueur_ligne] == '#':
                nb_arbres += 1

            compteur_horizontal += 1
        compteur_vertical += 1

    return nb_arbres


print(calcul_nb_arbres(1))
print(calcul_nb_arbres(3))
print(calcul_nb_arbres(5))
print(calcul_nb_arbres(7))
print(calcul_2_1())

total = calcul_nb_arbres(1) * calcul_nb_arbres(3) * calcul_nb_arbres(5) * calcul_nb_arbres(7) * calcul_2_1()

print(total)

