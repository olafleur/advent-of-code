def appliquer_operation(tab):
    if tab[1] == '+':
        return str(int(tab[0]) + int(tab[2]))
    else:
        return str(int(tab[0]) * int(tab[2]))


def trouver_fin_correspondante(index, chaine):
    compteur = 1

    while compteur > 0:
        index += 1
        if chaine[index] == ')':
            compteur -= 1
        elif chaine[index] == '(':
            compteur += 1

    return index


def evaluer(chaine):
    if "(" not in chaine:
        valeurs = chaine.split(" ")

        while len(valeurs) > 1:
            resultat = appliquer_operation(valeurs[0:3])
            valeurs = [resultat] + valeurs[3:]

        return valeurs[0]
    else:
        deb = chaine.index("(")
        fin = trouver_fin_correspondante(deb, chaine)

        return evaluer(chaine[:deb] + evaluer(chaine[deb + 1:fin]) + chaine[fin+1:])

#f = open("day18-puzzle-input.txt", "r")