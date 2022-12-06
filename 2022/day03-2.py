import string

f = open("day03-puzzle-input.txt", "r")

total = 0
lignes = []
nb_lignes = 0


def score(res):
    if res in string.ascii_lowercase:
        return ord(res) - 96
    else:
        return ord(res) - 38


for ligne in f:
    nb_lignes += 1
    lignes.append(ligne)

nb_sac = int(nb_lignes / 3)

for i in range(nb_sac):
    index = 3*i
    premiere = lignes[index]
    deuxieme = lignes[index + 1]
    troisieme = lignes[index + 2]

    resultat = list(filter(lambda x: x in deuxieme and x in troisieme, premiere))[0]
    nb = score(resultat)
    total += nb

print(total)
