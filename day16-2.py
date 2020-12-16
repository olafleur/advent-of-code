f = open("day16-puzzle-input.txt", "r")

valeurs_possibles = set()
ligne = f.readline()
categories = dict()
associations = dict()
vraies_associations = dict()
tickets = []

while ligne != "\n":
    minmax1 = ligne.split(" or ")[1].split("-")
    minmax2 = ligne.split(" or ")[0].split(" ")[-1].split("-")

    min1 = int(minmax1[0])
    max1 = int(minmax1[1])
    min2 = int(minmax2[0])
    max2 = int(minmax2[1])

    valeurs = []

    for i in range(min2, max2 + 1):
        valeurs_possibles.add(i)
        valeurs.append(i)

    for i in range(min1, max1 + 1):
        valeurs_possibles.add(i)
        valeurs.append(i)

    nom = ligne.split(":")[0]

    categories[nom] = valeurs

    ligne = f.readline()

for categorie in categories:
    associations[categorie] = []

while "your" not in ligne:
    ligne = f.readline()

mon_ticket = list(map(lambda x: int(x), f.readline().split(",")))

tickets.append(mon_ticket)

while "nearby" not in ligne:
    ligne = f.readline()

total = 0

for ligne in f:
    valide = True
    split = ligne.split(",")

    for val in split:
        if int(val) not in valeurs_possibles:
            total += int(val)
            valide = False

    if valide:
        mon_ticket = list(map(lambda x: int(x), split))
        tickets.append(mon_ticket)

for categorie, possibilites in categories.items():
    association_possible = True

    i = 0
    j = 0

    while i < len(mon_ticket):
        while association_possible and j < len(tickets):
            if tickets[j][i] not in possibilites:
                association_possible = False
            j += 1

        if association_possible:
            associations[categorie].append(i)

        association_possible = True
        i += 1
        j = 0


def reste_juste_un(assoc):
    for categorie, vals in assoc.items():
        if len(vals) == 1:
            return True

    return False


def enlever_tout_le_monde(associations, valeur):
    for categorie, vals in associations.items():
        if valeur in vals:
            vals.remove(valeur)


while reste_juste_un(associations):
    for categorie, vals in associations.items():
        if len(vals) == 1:
            vraies_associations[categorie] = vals[0]
            enlever_tout_le_monde(associations, vals[0])

resultat = 1

for categorie, id in vraies_associations.items():
    if "departure" in categorie:
        resultat *= tickets[0][id]

print(resultat)
