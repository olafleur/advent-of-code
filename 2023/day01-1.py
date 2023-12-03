f = open("day01-puzzle-input.txt", "r")

total = 0

for ligne in f:
    i = 0
    j = len(ligne) - 1

    while not ligne[i].isnumeric():
        i += 1

    while not ligne[j].isnumeric():
        j -= 1

    nombre = ligne[i] + ligne[j]

    total += int(nombre)

print(total)
