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


def valide_hcl(chaine):
    if len(chaine) != 7:
        return False

    if chaine[0] != '#':
        return False

    for i in range(1,7):
        if not chaine[i].isnumeric() and chaine[i] not in "abcdef":
            return False

    return True


def valide_en_cm(chaine):
    trouve = chaine.find('cm')

    if trouve == -1:
        return False

    valeur = int(chaine[:trouve])

    return 150 <= valeur <= 193


def valide_en_in(chaine):
    trouve = chaine.find('in')

    if trouve == -1:
        return False

    valeur = int(chaine[:trouve])

    return 59 <= valeur <= 76


def valide_hgt(chaine):
    return valide_en_cm(chaine) or valide_en_in(chaine)


def valide_pid(chaine):
    if len(chaine) != 9:
        return False

    for i in range(9):
        if not chaine[i].isnumeric():
            return False

    return True


def validation(passeport):
    valide = True
    valeurs = {'eyr': False, 'byr': False, 'hcl': False, 'ecl': False, 'hgt': False, 'iyr': False, 'pid': False}

    for val in passeport:
        split = val.split(':')
        cle = split[0]
        valeur = None

        if len(split) > 1:
            valeur = split[1]

        if cle == 'eyr':
            annee = int(valeur)
            valeurs['eyr'] = 2020 <= annee <= 2030
        if cle == 'byr':
            annee = int(valeur)
            valeurs['byr'] = 1920 <= annee <= 2002
        if cle == 'hcl':
            valeurs['hcl'] = valide_hcl(valeur)
        if cle == 'ecl':
            valeurs['ecl'] = valeur in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if cle == 'hgt':
            valeurs['hgt'] = valide_hgt(valeur)
        if cle == 'iyr':
            annee = int(valeur)
            valeurs['iyr'] = 2010 <= annee <= 2020
        if cle == 'pid':
            valeurs['pid'] = valide_pid(valeur)

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
