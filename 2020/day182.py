#def appliquer_operation(tab):
#    if tab[1] == '+':
#        return str(int(tab[0]) + int(tab[2]))
#    else:
#        return str(int(tab[0]) * int(tab[2]))


def appliquer_addition(tab):
    i = -1

    while '+' in tab:
        if tab[i] == '+':
            tab = tab[:i-1] + [str(int(tab[i-1]) + int(tab[i+1]))] + tab[i+2:]
        else:
            i += 2

    return tab


def appliquer_multiplication(tab):
    while len(tab) > 1:
        tab = [str(int(tab[0]) * int(tab[2]))] + tab[3:]

    return tab


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
            if "+" in valeurs:
                valeurs = appliquer_addition(valeurs)
            else:
                valeurs = appliquer_multiplication(valeurs)

        return valeurs[0]
    else:
        deb = chaine.index("(")
        fin = trouver_fin_correspondante(deb, chaine)

        return evaluer(chaine[:deb] + evaluer(chaine[deb + 1:fin]) + chaine[fin+1:])


f = open("day18-puzzle-input.txt", "r")
total = 0

for ligne in f:
    total += int(evaluer(ligne))

print(total)
