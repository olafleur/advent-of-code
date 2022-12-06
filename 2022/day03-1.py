import string

f = open("day03-puzzle-input.txt", "r")

total = 0


def score(res):
    if res in string.ascii_lowercase:
        return ord(res) - 96
    else:
        return ord(res) - 38


for ligne in f:
    longueur = len(ligne.strip())
    moitie = int(longueur / 2)
    premiere = ligne[:moitie]
    derniere = ligne[moitie:]

    resultat = list(filter(lambda x: x in derniere, premiere))[0]
    nb = score(resultat)
    total += nb

print(total)
