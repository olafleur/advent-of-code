f = open("day01-puzzle-input.txt", "r")

total = 0
totaux = []

for ligne in f:
    if ligne != '\n':
        total += int(ligne)
    else:
        totaux.append(total)
        total = 0
totaux.append(total)

print(max(totaux))
