f = open("day03-puzzle-input.txt", "r")

endroits_visites = set()

endroits_visites.add((0, 0))

ligne = f.readline()

courant = (0, 0)

for caractere in ligne:
    if caractere == '^':
        courant = (courant[0] + 1, courant[1])
    elif caractere == 'v':
        courant = (courant[0] - 1, courant[1])
    elif caractere == '>':
        courant = (courant[0], courant[1] + 1)
    elif caractere == '<':
        courant = (courant[0], courant[1] - 1)

    endroits_visites.add(courant)

print(len(endroits_visites))
