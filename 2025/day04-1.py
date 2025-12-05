f = open("day04-puzzle-input.txt", "r")

grid = []
accessible = []

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

print(accessible)
print(len(accessible))
