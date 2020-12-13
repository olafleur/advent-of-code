f = open("day09-puzzle-input.txt", "r")

lignes = f.readlines()

entiers = list(map(lambda x: int(x), lignes))

nombre = 556543474

for i in range(len(entiers)):
    somme = entiers[i]
    j = 1
    min = entiers[i]
    max = entiers[i]

    if entiers[i] < nombre:
        while somme < nombre:
            somme += entiers[i + j]

            if entiers[i + j] > max:
                max = entiers[i + j]

            if entiers[i + j] < min:
                min = entiers[i + j]

            j += 1

        if somme == nombre:
            print("min = " + str(min))
            print("max = " + str(min))
            print("résultat = " + str(min + max))
