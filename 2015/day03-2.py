f = open("day03-puzzle-input.txt", "r")

endroits_visites = set()

endroits_visites.add((0, 0))

ligne = f.readline()

pere_noel = (0, 0)
robot = (0, 0)

for i in range(len(ligne)):
    if i % 2 == 0:
        if ligne[i] == '^':
            pere_noel = (pere_noel[0] + 1, pere_noel[1])
        elif ligne[i] == 'v':
            pere_noel = (pere_noel[0] - 1, pere_noel[1])
        elif ligne[i] == '>':
            pere_noel = (pere_noel[0], pere_noel[1] + 1)
        elif ligne[i] == '<':
            pere_noel = (pere_noel[0], pere_noel[1] - 1)

        endroits_visites.add(pere_noel)
    else:
        if ligne[i] == '^':
            robot = (robot[0] + 1, robot[1])
        elif ligne[i] == 'v':
            robot = (robot[0] - 1, robot[1])
        elif ligne[i] == '>':
            robot = (robot[0], robot[1] + 1)
        elif ligne[i] == '<':
            robot = (robot[0], robot[1] - 1)

        endroits_visites.add(robot)

print(len(endroits_visites))
