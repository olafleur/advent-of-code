f = open("day4-puzzle-input.txt", "r")

lignes = f.readlines()
contenu = []
contenu_clean = []

for ligne in lignes:
    splitter = ligne.split(' ')

    for split in splitter:
        contenu.append(split)

for element in contenu:
    contenu_clean.append(element.replace('\n', ''))

indices = [0]

for i in range(len(contenu_clean)):
    if contenu_clean[i] == '':
        indices.append(i)

passeports_separes = []

for i in range(len(indices) - 1):
    truc = contenu_clean[indices[i]:indices[i+1]]
    passeports_separes.append(truc)

truc2 = contenu_clean[indices[len(indices)-1]:]
passeports_separes.append(truc2)


def validation(passeport):
    valide = True
    valeurs = {'eyr': False, 'byr': False, 'hcl': False, 'ecl': False, 'hgt': False, 'iyr': False, 'pid': False}

    for val in passeport:
        valeur = val.split(':')[0]
        valeurs[valeur] = True

    for cle in valeurs:
        if not valeurs[cle]:
            valide = False
    return valide


def nb_passeports_valides(passeports):
    count = 0

    for passeport in passeports:
        if validation(passeport):
            count += 1

    return count


print(nb_passeports_valides(passeports_separes))
