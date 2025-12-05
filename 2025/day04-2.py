f = open("day04-puzzle-input.txt", "r")

grid = []
accessible = []
total = 0

for ligne in f:
    grid.append(ligne.replace('\n', ''))

length = len(grid)


def nb_voisins(x, y):
    count = 0

    if x == 0 and 0 < y < length - 1:
        count += (1 if grid[x][y - 1] == '@' else 0)
        count += (1 if grid[x][y + 1] == '@' else 0)
        count += (1 if grid[x + 1][y - 1] == '@' else 0)
        count += (1 if grid[x + 1][y] == '@' else 0)
        count += (1 if grid[x + 1][y + 1] == '@' else 0)

    if x == length - 1 and 0 < y < length - 1:
        count += (1 if grid[x][y - 1] == '@' else 0)
        count += (1 if grid[x][y + 1] == '@' else 0)
        count += (1 if grid[x - 1][y - 1] == '@' else 0)
        count += (1 if grid[x - 1][y] == '@' else 0)
        count += (1 if grid[x - 1][y + 1] == '@' else 0)

    if 0 < x < length - 1 and y == 0:
        count += (1 if grid[x - 1][y] == '@' else 0)
        count += (1 if grid[x + 1][y] == '@' else 0)
        count += (1 if grid[x - 1][y + 1] == '@' else 0)
        count += (1 if grid[x][y + 1] == '@' else 0)
        count += (1 if grid[x + 1][y + 1] == '@' else 0)

    if 0 < x < length - 1 and y == length - 1:
        count += (1 if grid[x - 1][y] == '@' else 0)
        count += (1 if grid[x + 1][y] == '@' else 0)
        count += (1 if grid[x - 1][y - 1] == '@' else 0)
        count += (1 if grid[x][y - 1] == '@' else 0)
        count += (1 if grid[x + 1][y - 1] == '@' else 0)

    if 0 < x < length - 1 and 0 < y < length - 1:
        count += (1 if grid[x - 1][y - 1] == '@' else 0)
        count += (1 if grid[x - 1][y] == '@' else 0)
        count += (1 if grid[x - 1][y + 1] == '@' else 0)
        count += (1 if grid[x][y - 1] == '@' else 0)
        count += (1 if grid[x][y + 1] == '@' else 0)
        count += (1 if grid[x + 1][y - 1] == '@' else 0)
        count += (1 if grid[x + 1][y] == '@' else 0)
        count += (1 if grid[x + 1][y + 1] == '@' else 0)

    return count


for i in range(length):
    for j in range(length):
        if grid[i][j] == '@':
            if nb_voisins(i, j) < 4:
                accessible.append((i, j))

while len(accessible) > 0:
    total += len(accessible)
    print(accessible)
    print(len(accessible))

    for (x, y) in accessible:
        grid[x] = grid[x][:y] + '.' + grid[x][y + 1:]

    accessible = []
    for i in range(length):
        for j in range(length):
            if grid[i][j] == '@':
                if nb_voisins(i, j) < 4:
                    accessible.append((i, j))

print(accessible)
print(len(accessible))
print(total)
