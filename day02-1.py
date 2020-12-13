def count(lettre, chaine):
    total = 0

    for c in chaine:
        if c == lettre:
            total += 1

    return total


def valide(ligne):
    split_dash = ligne.split('-')

    minimum = int(split_dash[0])
    split_space = split_dash[1].split(' ')

    maximum = int(split_space[0])
    split_comma = split_space[1].split(':')

    lettre = split_comma[0]
    chaine = split_space[2]

    return minimum <= count(lettre, chaine) <= maximum


f = open("day02-1-puzzle-input.txt", "r")
nombre_valide = 0

for ligne_fichier in f:
    if valide(ligne_fichier):
        nombre_valide += 1

print(nombre_valide)


