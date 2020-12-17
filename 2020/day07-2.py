f = open("day07-puzzle-input.txt", "r")

lignes = f.readlines()
regles = dict()
couleurs = []


def generer_regle(ligne):
    split = ligne.split(" bags contain")
    couleur = split[0]
    couleurs.append(couleur)
    split2 = split[1].replace(" bags.", "").replace(" bag.", "").replace("no other", "").replace("\n", "")[1:]
    split3 = split2.split(',')
    if split3[0] == '':
        return {couleur: []}

    nombre = int(split3[0][0])
    valeur = split3[0][2:].replace(" bags", "").replace(" bag", "")

    if len(split3) == 1:
        return {couleur: [(nombre, valeur)]}

    valeurs = [(nombre, valeur)]
    for i in range(1, len(split3)):
        valeurs.append((int(split3[i][1]), split3[i][3:].replace(" bags", "").replace(" bag", "")))

    return {couleur: valeurs}


for ligne in lignes:
    regle = generer_regle(ligne)
    regles = {**regle, **regles}


def compter(couleur):
    if len(regles[couleur]) == 0:
        return 0

    count = 0

    for paire in regles[couleur]:
        count += paire[0] + (paire[0] * compter(paire[1]))

    return count


print(compter("shiny gold"))
