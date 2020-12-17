f = open("day16-puzzle-input.txt", "r")

valeurs_possibles = set()
ligne = f.readline()

while ligne != "\n":
    minmax1 = ligne.split(" or ")[1].split("-")
    minmax2 = ligne.split(" or ")[0].split(" ")[-1].split("-")

    min1 = int(minmax1[0])
    max1 = int(minmax1[1])
    min2 = int(minmax2[0])
    max2 = int(minmax2[1])

    for i in range(min1, max1 + 1):
        valeurs_possibles.add(i)

    for i in range(min2, max2 + 1):
        valeurs_possibles.add(i)

    ligne = f.readline()

while "nearby" not in ligne:
    ligne = f.readline()

total = 0

for ligne in f:
    split = ligne.split(",")

    for val in split:
        if int(val) not in valeurs_possibles:
            total += int(val)

print(total)
