f = open("day05-puzzle-input.txt", "r")

transitions = dict()
total = 0


def reorder(path):
    i = 0

    while i < len(path) - 1:
        if path[i] in transitions and path[i+1] in transitions[path[i]]:
            i += 1
        else:
            # swap
            path[i], path[i+1] = path[i+1], path[i]
            i = 0

    return path


for ligne in f:
    if "|" in ligne:
        num1 = int(ligne.split("|")[0])
        num2 = int(ligne.split("|")[1])

        if num1 in transitions.keys():
            transitions[num1].append(num2)
        else:
            transitions[num1] = [num2]

    if "," in ligne:
        chemin = list(map(int, ligne.split(',')))
        valide = True
        i = 0

        while valide and i < len(chemin)-1:
            if chemin[i] not in transitions or chemin[i+1] not in transitions[chemin[i]]:
                valide = False
            i += 1

        if not valide:
            total += reorder(chemin)[len(chemin)//2]

print(total)
