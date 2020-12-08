f = open("day7-puzzle-input.txt", "r")

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

    valeur = split3[0][2:].replace(" bags", "").replace(" bag", "")

    if len(split3) == 1:
        return {couleur: [valeur]}

    valeurs = [valeur]
    for i in range(1, len(split3)):
        valeurs.append(split3[i][3:].replace(" bags", "").replace(" bag", ""))

    return {couleur: valeurs}


for ligne in lignes:
    regle = generer_regle(ligne)
    regles = {**regle, **regles}


def peut_contenir_shiny_gold(couleur_parent):
    peut_contenir = False

    if couleur_parent == 'shiny gold':
        return True

    if couleur_parent not in regles:
        return False

    if len(regles[couleur_parent]) == 0:
        return False
    else:
        for couleur in regles[couleur_parent]:
            if peut_contenir_shiny_gold(couleur):
                peut_contenir = True

    return peut_contenir


count = 0

for couleur in couleurs:
    if couleur != "shiny gold" and peut_contenir_shiny_gold(couleur):
        count += 1


print(count)
