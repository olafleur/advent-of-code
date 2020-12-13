f = open("day06-puzzle-input.txt", "r")

liste = f.readlines()
indices = []

for i in range(len(liste)):
    if liste[i] == '\n':
        indices.append(i)

contenu = [liste[:indices[0]]]

for i in range(len(indices)-1):
    contenu.append(liste[indices[i]:indices[i+1]])

contenu.append(liste[indices[len(indices)-1]:])


def nb_lettres(tableau):
    tableau_ensembles = []
    tableau_clean = []

    for element in tableau:
        tableau_clean.append(element.replace('\n', ''))

    for element in tableau_clean:
        if element != '':
            ensemble = {''}
            for lettre in element:
                ensemble.add(lettre)

            ensemble.remove('')
            tableau_ensembles.append(ensemble)

    ensemble_intersection = tableau_ensembles[0]

    for ensemble in tableau_ensembles:
        ensemble_intersection = ensemble_intersection.intersection(ensemble)

    print(ensemble_intersection)

    return len(ensemble_intersection)


decompte = 0
for element in contenu:
    decompte += nb_lettres(element)

print(decompte)
