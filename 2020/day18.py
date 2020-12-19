def appliquer_operation(tab):
    if tab[1] == '+':
        return str(int(tab[0]) + int(tab[2]))
    else:
        return str(int(tab[0]) * int(tab[2]))


def evaluer(chaine):
    if "(" not in chaine:
        valeurs = chaine.split(" ")

        while len(valeurs) > 1:
            resultat = appliquer_operation(valeurs[0:3])
            valeurs = [resultat] + valeurs[3:]

        return valeurs[0]
    else:
        return "15"

#f = open("day18-puzzle-input.txt", "r")