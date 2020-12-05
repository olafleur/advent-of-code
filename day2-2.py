def valide(ligne):
    split_dash = ligne.split('-')

    premier_nombre = int(split_dash[0])
    split_space = split_dash[1].split(' ')

    deuxieme_nombre = int(split_space[0])
    split_comma = split_space[1].split(':')

    lettre = split_comma[0]
    chaine = split_space[2]

    if chaine[premier_nombre - 1] == lettre:
        if chaine[deuxieme_nombre - 1] == lettre:
            return False
        else:
            return True
    else:
        if chaine[deuxieme_nombre - 1] == lettre:
            return True
        else:
            return False


f = open("day2-1-puzzle-input.txt", "r")
nombre_valide = 0

for ligne_fichier in f:
    if valide(ligne_fichier):
        nombre_valide += 1

print(nombre_valide)


