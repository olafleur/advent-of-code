f = open("day10-puzzle-input.txt", "r")

chaines = f.readlines()

joltages = list(map(lambda x: int(x), chaines))

max = max(joltages)

joltages.append(0)
joltages.append(max + 3)
joltages.sort()

i = 0
liste = [joltages[0]]
count = 1
chemins = {3: 2, 4: 4, 5: 7}

while i < len(joltages) - 1:
    if joltages[i+1] - joltages[i] == 1:
        if joltages[i] not in liste:
            liste.append(joltages[i])
        liste.append(joltages[i+1])
    else:
        nb = len(liste)
        if nb >= 3:
            count *= chemins[nb]
            print(liste)
        liste = []
    i += 1

print(count)
