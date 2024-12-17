f = open("day10-puzzle-input.txt", "r")

grid = []
trailheads = []
summits_of = dict()
total = 0

for line in f:
    grid.append(line)

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == '0':
            trailheads.append((i, j))


def find_summits(head, current_coord, current_value):
    if current_value == 9:
        if head not in summits_of:
            summits_of[head] = [current_coord]  # only changes are here
        else:
            summits_of[head].append(current_coord)  # and here
        return

    if current_coord[0] + 1 < len(grid) and int(grid[current_coord[0] + 1][current_coord[1]]) == current_value + 1:
        find_summits(head, (current_coord[0] + 1, current_coord[1]), current_value + 1)
    if current_coord[1] + 1 < len(grid) and int(grid[current_coord[0]][current_coord[1] + 1]) == current_value + 1:
        find_summits(head, (current_coord[0], current_coord[1] + 1), current_value + 1)
    if current_coord[0] - 1 >= 0 and int(grid[current_coord[0] - 1][current_coord[1]]) == current_value + 1:
        find_summits(head, (current_coord[0] - 1, current_coord[1]), current_value + 1)
    if current_coord[1] - 1 >= 0 and int(grid[current_coord[0]][current_coord[1] - 1]) == current_value + 1:
        find_summits(head, (current_coord[0], current_coord[1] - 1), current_value + 1)


for trailhead in trailheads:
    find_summits(trailhead, trailhead, 0)

for trailhead in summits_of:
    total += len(summits_of[trailhead])

print(total)
