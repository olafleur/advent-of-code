from enum import Enum

f = open("day12-puzzle-input.txt", "r")

chaines = f.readlines()


class Directions(Enum):
    NORD = 1
    SUD = 2
    EST = 3
    OUEST = 4


direction = Directions.EST
x = 0
y = 0


def structurer(ligne):
    ligne = ligne.replace("\n", "")

    return ligne[0], int(ligne[1:])


instructions = list(map(structurer, chaines))


def rotation_anti_90():
    global direction

    changement = {Directions.EST: Directions.NORD, Directions.NORD: Directions.OUEST,
                  Directions.OUEST: Directions.SUD, Directions.SUD: Directions.EST}

    direction = changement[direction]


def rotation_180():
    global direction

    changement = {Directions.EST: Directions.OUEST, Directions.NORD: Directions.SUD,
                  Directions.OUEST: Directions.EST, Directions.SUD: Directions.NORD}

    direction = changement[direction]


def rotation_horaire_90():
    global direction

    changement = {Directions.EST: Directions.SUD, Directions.NORD: Directions.EST,
                  Directions.OUEST: Directions.NORD, Directions.SUD: Directions.OUEST}

    direction = changement[direction]


def changer_direction(action, valeur):
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

    if direction == Directions.EST:
        x += valeur
    elif direction == Directions.OUEST:
        x -= valeur
    elif direction == Directions.NORD:
        y += valeur
    elif direction == Directions.SUD:
        y -= valeur


def appliquer(coord):
    global x, y
    action = coord[0]
    valeur = coord[1]

    if action == 'N':
        y += valeur
    elif action == 'S':
        y -= valeur
    elif action == 'E':
        x += valeur
    elif action == 'W':
        x -= valeur
    elif action in 'LR':
        changer_direction(action, valeur)
    elif action == 'F':
        avancer(valeur)

    return action, valeur


for instruction in instructions:
    appliquer(instruction)

print(instructions)
print(x, y)

manhattan = abs(x) + abs(y)

print(manhattan)
