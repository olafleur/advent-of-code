f = open("day11-puzzle-input.txt", "r")

universe = []
coords_galaxies = []
empty_to_add = 1000000 - 1
already_empty_rows = []
already_empty_cols = []
counter = 0

for line in f:
    cleaned_up_line = line.strip()
    universe.append(cleaned_up_line)

    if not any(x != '.' for x in cleaned_up_line):
        already_empty_rows.append(counter)

    counter += 1

for i in range(len(universe)):
    for j in range(len(universe[0])):
        if universe[i][j] == '#':
            coords_galaxies.append((i, j))

for col in range(len(universe[0])):
    different_than_dot = False
    for line in range(len(universe)):
        if universe[line][col] != '.':
            different_than_dot = True

    if not different_than_dot:
        already_empty_cols.append(col)

expanded_rows = []

counter = 0
previous_empty = 0

for empty in already_empty_rows:
    for coord in coords_galaxies:
        if previous_empty <= coord[0] < empty:
            expanded_rows.append((coord[0] + counter, coord[1]))
    counter += empty_to_add
    previous_empty = empty

# after last empty
for coord in coords_galaxies:
    if previous_empty <= coord[0]:
        expanded_rows.append((coord[0] + counter, coord[1]))

counter = 0
previous_empty = 0
expanded_universe = []

for empty in already_empty_cols:
    for coord in expanded_rows:
        if previous_empty <= coord[1] < empty:
            expanded_universe.append((coord[0], coord[1] + counter))
    counter += empty_to_add
    previous_empty = empty

for coord in expanded_rows:
    if previous_empty <= coord[1]:
        expanded_universe.append((coord[0], coord[1] + counter))

universe_dict = {}

for i in range(len(expanded_universe)):
    universe_dict[i] = expanded_universe[i]


def minimum_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


distances = []

for i in range(len(universe_dict)):
    for j in range(i+1, len(universe_dict)):
        distances.append(minimum_distance(universe_dict[i], universe_dict[j]))

print(sum(distances))
