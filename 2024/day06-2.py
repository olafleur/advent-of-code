f = open("day06-puzzle-input.txt", "r")

grille = []
x_start = 0
y_start = 0
direction_start = '^'
# x_courant = 0
# y_courant = 0
# direction_courante = '^'
nb_possibility = 0

for line in f:
    grille.append(line.replace('\n', ''))


def replace_in_grid(x, y, symbol):
    grille[x] = grille[x][:y] + symbol + grille[x][y + 1:]


for i in range(len(grille)):
    for j in range(len(grille)):
        if grille[i][j] == '^':
            x_start = i
            y_start = j
            # remove ^ from grid
            grille[i] = grille[i][:j] + '.' + grille[i][j + 1:]


def back_to_square_one(x, y, direction):
    return x == x_start and y == y_start and direction == direction_start


def grid_loops():
    x_courant = x_start - 1
    y_courant = y_start
    direction_courante = direction_start
    nb_steps = 0

    while (0 < x_courant < len(grille) - 1 and 0 < y_courant < len(grille) - 1) \
            and not back_to_square_one(x_courant, y_courant, direction_courante) and nb_steps < 10000:
        # print(x_courant, y_courant, direction_courante)
        if direction_courante == '^':
            if grille[x_courant - 1][y_courant] == '.':
                nb_steps += 1
                x_courant -= 1
            else:
                direction_courante = '>'
        elif direction_courante == '>':
            if grille[x_courant][y_courant + 1] == '.':
                nb_steps += 1
                y_courant += 1
            else:
                direction_courante = 'v'
        elif direction_courante == 'v':
            if grille[x_courant + 1][y_courant] == '.':
                nb_steps += 1
                x_courant += 1
            else:
                direction_courante = '<'
        elif direction_courante == '<':
            if grille[x_courant][y_courant - 1] == '.':
                y_courant -= 1
                nb_steps += 1
            else:
                direction_courante = '^'

    if back_to_square_one(x_courant, y_courant, direction_courante) or nb_steps == 10000:
        return True

    return False


for i in range(len(grille)):
    for j in range(len(grille)):
        # on peut potentiellement placer un objet
        if grille[i][j] == '.':
            replace_in_grid(i, j, '#')

            if grid_loops():
                nb_possibility += 1

            replace_in_grid(i, j, '.')


print(nb_possibility)
