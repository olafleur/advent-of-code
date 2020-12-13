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
    ensemble = {''}

    for element in tableau:
        for lettre in element:
            ensemble.add(lettre)

    ensemble.remove('')
    ensemble.remove('\n')

    return len(ensemble)


decompte = 0
for element in contenu:
    decompte += nb_lettres(element)

print(decompte)
