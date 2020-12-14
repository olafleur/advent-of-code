f = open("day14-puzzle-input.txt", "r")

memoire = dict()
masque = ""


def generer_adresses(resultat, valeur):
    if "X" in resultat:
        index = resultat.index("X")
        copie0 = resultat[:]
        copie1 = resultat[:]

        copie0[index] = "0"
        copie1[index] = "1"

        generer_adresses(copie0, valeur)
        generer_adresses(copie1, valeur)
    else:
        nombre = int("".join(resultat), 2)
        memoire[nombre] = valeur


def appliquer_masque(valeur, adresse):
    resultat = []

    for i in range(len(adresse)):
        if masque[i] == '1':
            resultat.append(masque[i])
        elif masque[i] == '0':
            resultat.append(adresse[i])
        else:  # X
            resultat.append("X")

    generer_adresses(resultat, valeur)

    return resultat


for line in f:
    if "mask" in line:
        masque = line.split(" ")[2]
    else:
        split = line.split(" ")
        valeur = int(split[2])
        adresse = int(split[0][4:-1])
        valeur_binaire = format(valeur, 'b').zfill(36)
        adresse_binaire = format(adresse, 'b').zfill(36)

        appliquer_masque(str(valeur_binaire), str(adresse_binaire))

somme = 0

for valeur in memoire.values():
    somme += int(valeur, 2)

print(somme)
