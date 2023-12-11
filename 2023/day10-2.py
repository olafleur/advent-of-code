f = open("day10-puzzle-input.txt", "r")

coords = []

i = 0

starting_line = 0
starting_col = 0
starting_point = None
previous_point = None
current_point = None
direction = None
second_direction = None
path = []


for line in f:
    coords.append(line.strip())

    if 'S' in line:
        starting_line = i
        starting_col = line.index('S')
        starting_point = (starting_line, starting_col)
        previous_point = (starting_line, starting_col)
        current_point = (starting_line, starting_col)
        path.append(starting_point)
    i += 1


def calculate_new_direction(symbol, old_direction):
    if symbol == '|' or symbol == '-':
        return old_direction

    if symbol == 'L':
        if old_direction == 'left':
            return 'top'
        return 'right'

    if symbol == 'J':
        if old_direction == 'right':
            return 'top'
        return 'left'

    if symbol == '7':
        if old_direction == 'right':
            return 'down'
        return 'left'

    if symbol == 'F':
        if old_direction == 'left':
            return 'down'
        return 'right'
    return


def calculate_new_coord(coord, direction_to_go):
    if direction_to_go == 'right':
        return coord[0], coord[1] + 1
    if direction_to_go == 'left':
        return coord[0], coord[1] - 1
    if direction_to_go == 'top':
        return coord[0] - 1, coord[1]
    if direction_to_go == 'down':
        return coord[0] + 1, coord[1]
    return


def replace_char(string, index, char):
    return string[:index] + char + string[index + 1:]


def classify_points():
    nb_intersection = 0
    f_started = False
    l_started = False

    for i in range(len(coords)):
        for j in range(len(coords[0])):
            if (i, j) not in path:
                if nb_intersection % 2 == 0:
                    coords[i] = replace_char(coords[i], j, 'O')
                else:
                    coords[i] = replace_char(coords[i], j, 'I')
            else:
                if coords[i][j] == '|':
                    nb_intersection += 1
                elif coords[i][j] == 'F':
                    f_started = True
                elif coords[i][j] == 'L':
                    l_started = True
                elif coords[i][j] == 'J':
                    if f_started:
                        nb_intersection += 1
                        f_started = False
                    if l_started:
                        l_started = False
                elif coords[i][j] == '7':
                    if l_started:
                        nb_intersection += 1
                        l_started = False
                    if f_started:
                        f_started = False

        nb_intersection = 0


# calculate direction at starting point
if coords[current_point[0]-1][current_point[1]] in ['|', 'F', '7']:
    direction = 'top'
if coords[current_point[0]+1][current_point[1]] in ['|', 'L', 'J']:
    direction = 'down'
if coords[current_point[0]][current_point[1]-1] in ['-', 'F', 'L']:
    second_direction = 'left'
else:
    second_direction = 'right'

# replace S with the correct symbol
if (direction, second_direction) == ('top', 'left'):
    coords[current_point[0]] = replace_char(coords[current_point[0]], current_point[1], 'J')
elif (direction, second_direction) == ('top', 'right'):
    coords[current_point[0]] = replace_char(coords[current_point[0]], current_point[1], 'L')
elif (direction, second_direction) == ('down', 'left'):
    coords[current_point[0]] = replace_char(coords[current_point[0]], current_point[1], '7')
elif (direction, second_direction) == ('down', 'right'):
    coords[current_point[0]] = replace_char(coords[current_point[0]], current_point[1], 'F')


while current_point != starting_point or starting_point == previous_point:
    previous_point = current_point
    current_point = calculate_new_coord(current_point, direction)
    direction = calculate_new_direction(coords[current_point[0]][current_point[1]], direction)

    if coords[current_point[0]][current_point[1]] != 'S':
        path.append(current_point)

classify_points()

total = 0

for i in range(len(coords)):
    for j in range(len(coords[0])):
        if coords[i][j] == 'I':
            total += 1

print(total)
