f = open("day14-puzzle-input.txt", "r")

memoire = dict()
masque = ""


def appliquer_masque(binaire):
    resultat = ""

    for i in range(len(binaire)):
        if masque[i] == "X":
            resultat += binaire[i]
        else:
            resultat += masque[i]
    return resultat


for line in f:
    if "mask" in line:
        masque = line.split(" ")[2]
    else:
        split = line.split(" ")
        valeur = int(split[2])
        adresse = split[0][4:-1]
        valeur_binaire = format(valeur, 'b').zfill(36)

        resultat = appliquer_masque(str(valeur_binaire))

        memoire[adresse] = resultat

somme = 0

for valeur in memoire.values():
    somme += int(valeur, 2)

print(somme)
