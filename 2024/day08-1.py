f = open("day08-puzzle-input.txt", "r")

grid = []
frequencies = set()
antenna_locations = {}
antinode_locations = set()
longueur = 0

for line in f:
    grid.append(line)

longueur = len(grid)

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] != '.':
            frequencies.add(grid[i][j])

            if grid[i][j] in antenna_locations:
                antenna_locations[grid[i][j]].append((i, j))
            else:
                antenna_locations[grid[i][j]] = [(i, j)]


def calculate_antinodes(location1, location2):
    (x1, y1) = location1
    (x2, y2) = location2

    antinode1 = (x2 + (x2 - x1), y2 + (y2 - y1))
    antinode2 = (x1 - (x2 - x1), y1 - (y2 - y1))

    if 0 <= antinode1[0] < longueur and 0 <= antinode1[1] < longueur:
        antinode_locations.add(antinode1)

    if 0 <= antinode2[0] < longueur and 0 <= antinode2[1] < longueur:
        antinode_locations.add(antinode2)


for frequency in frequencies:
    locations = antenna_locations[frequency]
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            calculate_antinodes(locations[i], locations[j])

print(len(antinode_locations))
