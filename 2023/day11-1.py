f = open("day11-puzzle-input.txt", "r")

universe = []

for line in f:
    cleaned_up_line = line.strip()
    universe.append(cleaned_up_line)

    if not any(x != '.' for x in cleaned_up_line):
        universe.append(cleaned_up_line)

expanded_universe = ['' for x in range(len(universe))]

for col in range(len(universe[0])):

    for line in range(len(universe)):
        expanded_universe[line] += universe[line][col]

    different_than_dot = False
    for line in range(len(universe)):
        if universe[line][col] != '.':
            different_than_dot = True

    if not different_than_dot:
        for line in range(len(universe)):
            expanded_universe[line] += '.'


galaxies_dict = {}
galaxies_counter = 0

for i in range(len(expanded_universe)):
    for j in range(len(expanded_universe[0])):
        if expanded_universe[i][j] == '#':
            galaxies_dict[galaxies_counter] = (i, j)
            galaxies_counter += 1


def minimum_distance(coord1, coord2):
    if coord1 == coord2:
        return 0

    if (coord1[0]+1, coord1[1]) == coord2 or (coord1[0]-1, coord1[1]) == coord2 \
            or (coord1[0], coord1[1]+1) == coord2 or (coord1[0], coord1[1]-1) == coord2:
        return 1

    if coord1[0] > coord2[0]:
        return 1 + minimum_distance((coord1[0]-1, coord1[1]), coord2)
    if coord1[0] < coord2[0]:
        return 1 + minimum_distance((coord1[0]+1, coord1[1]), coord2)
    if coord1[1] > coord2[1]:
        return 1 + minimum_distance((coord1[0], coord1[1]-1), coord2)
    if coord1[1] < coord2[1]:
        return 1 + minimum_distance((coord1[0], coord1[1]+1), coord2)

    return


distances = []

for i in range(len(galaxies_dict)):
    for j in range(i+1, len(galaxies_dict)):
        distances.append(minimum_distance(galaxies_dict[i], galaxies_dict[j]))

print(sum(distances))
