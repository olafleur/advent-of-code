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

totaux.sort()

print(int(totaux[-1]) + int(totaux[-2]) + int(totaux[-3]))
