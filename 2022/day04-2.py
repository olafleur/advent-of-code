f = open("day04-puzzle-input.txt", "r")

total = 0

for ligne in f:
    splitted = ligne.split(',')
    gauche = list(map(lambda x: int(x), splitted[0].split('-')))
    droite = list(map(lambda x: int(x), splitted[1].strip().split('-')))

    if (gauche[0] >= droite[0] and gauche[1] <= droite[1]) or (
            droite[0] >= gauche[0] and droite[1] <= gauche[1]) or (
            gauche[0] <= droite[0] <= gauche[1]) or (droite[0] <= gauche[0] <= droite[1]):
        total += 1

print(total)
