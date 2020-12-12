f = open("day12-puzzle-input.txt", "r")

chaines = f.readlines()

x = 0
y = 0
waypoint_x = 10
waypoint_y = 1


def structurer(ligne):
    ligne = ligne.replace("\n", "")

    return ligne[0], int(ligne[1:])


instructions = list(map(structurer, chaines))


def rotation_anti_90():
    global waypoint_x, waypoint_y

    ancien_x = waypoint_x
    ancien_y = waypoint_y

    waypoint_x = ancien_y * -1
    waypoint_y = ancien_x


def rotation_180():
    global waypoint_x, waypoint_y

    ancien_x = waypoint_x
    ancien_y = waypoint_y

    waypoint_x = ancien_x * -1
    waypoint_y = ancien_y * -1


def rotation_horaire_90():
    global waypoint_x, waypoint_y

    ancien_x = waypoint_x
    ancien_y = waypoint_y

    waypoint_x = ancien_y
    waypoint_y = ancien_x * -1


def changer_direction_waypoint(action, valeur):
    if action == 'L':
        if valeur == 90:
            rotation_anti_90()
        elif valeur == 180:
            rotation_180()
        elif valeur == 270:
            rotation_horaire_90()
    elif action == 'R':
        if valeur == 90:
            rotation_horaire_90()
        elif valeur == 180:
            rotation_180()
        elif valeur == 270:
            rotation_anti_90()


def avancer(valeur):
    global x, y

    x += valeur * waypoint_x
    y += valeur * waypoint_y


def appliquer(coord):
    global waypoint_x, waypoint_y
    action = coord[0]
    valeur = coord[1]

    if action == 'N':
        waypoint_y += valeur
    elif action == 'S':
        waypoint_y -= valeur
    elif action == 'E':
        waypoint_x += valeur
    elif action == 'W':
        waypoint_x -= valeur
    elif action in 'LR':
        changer_direction_waypoint(action, valeur)
    elif action == 'F':
        avancer(valeur)


for instruction in instructions:
    appliquer(instruction)

print(x, y)

manhattan = abs(x) + abs(y)

print(manhattan)
