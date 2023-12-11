import math

f = open("day10-puzzle-input.txt", "r")

coords = []

i = 0

starting_line = 0
starting_col = 0
starting_point = None
previous_point = None
current_point = None
direction = None
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


# calculate direction at starting point
if coords[current_point[0]-1][current_point[1]] in ['|', 'F', '7']:
    direction = 'top'
elif coords[current_point[0]+1][current_point[1]] in ['|', 'L', 'J']:
    direction = 'down'
elif coords[current_point[0]][current_point[1]-1] in ['-', 'F', 'L']:
    direction = 'left'
else:
    direction = 'right'

while current_point != starting_point or starting_point == previous_point:
    previous_point = current_point
    current_point = calculate_new_coord(current_point, direction)

    if coords[current_point[0]][current_point[1]] != 'S':
        direction = calculate_new_direction(coords[current_point[0]][current_point[1]], direction)
        path.append(current_point)

print(math.floor(len(path)/2))
