f = open("day06-puzzle-input.txt", "r")

grille = []
x_courant = 0
y_courant = 0
direction = '^'
visited = set()

for line in f:
    grille.append(line.replace('\n', ''))

for i in range(len(grille)):
    for j in range(len(grille)):
        if grille[i][j] == '^':
            x_courant = i
            y_courant = j
            # remove ^ from grid
            grille[i] = grille[i][:y_courant] + '.' + grille[i][y_courant + 1:]
            visited.add((x_courant, y_courant))


while 0 < x_courant < len(grille) - 1 and 0 < y_courant < len(grille) - 1:
    if direction == '^':
        if grille[x_courant-1][y_courant] == '.':
            visited.add((x_courant, y_courant))
            x_courant -= 1
        else:
            direction = '>'
    elif direction == '>':
        if grille[x_courant][y_courant+1] == '.':
            visited.add((x_courant, y_courant))
            y_courant += 1
        else:
            direction = 'v'
    elif direction == 'v':
        if grille[x_courant+1][y_courant] == '.':
            visited.add((x_courant, y_courant))
            x_courant += 1
        else:
            direction = '<'
    elif direction == '<':
        if grille[x_courant][y_courant-1] == '.':
            visited.add((x_courant, y_courant))
            y_courant -= 1
        else:
            direction = '^'

print(len(visited) + 1)
