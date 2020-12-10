f = open("day10-small-input.txt", "r")

chaines = f.readlines()

joltages = list(map(lambda x: int(x), chaines))

max = max(joltages)

joltages.append(0)
joltages.append(max + 3)
joltages.sort()


def est_valide(liste):
    valide = True

    for i in range(len(liste) - 1):
        if liste[i + 1] - liste[i] > 3:
            valide = False

    return valide


possibles = set()


def trouver_valide(liste):
    if est_valide(liste):
        possibles.add(tuple(liste))

        for i in liste[1:-1]:
            nouveau = liste[:]
            nouveau.remove(i)

            trouver_valide(nouveau)
    else:
        return


trouver_valide(joltages)
print(possibles)
print(str(len(possibles)) + " possibilités")