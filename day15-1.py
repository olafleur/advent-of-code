tableau = [5, 2, 8, 16, 18, 0, 1]


def first_time(nb):
    return nb not in tableau[:-1]


def trouver_avant(nb):
    inverse = tableau[:-1]
    inverse.reverse()

    return len(tableau) - 1 - (inverse.index(nb) + 1)


for i in range(len(tableau) - 1, 2020):
    if first_time(tableau[i]):
        tableau.append(0)
    else:
        index = trouver_avant(tableau[i])
        tableau.append(i - index)

print(tableau[2019])
