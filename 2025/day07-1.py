f = open("day07-puzzle-input.txt", "r")

y_depart = -1
grid = []
beams = set()
split_total = 0

for ligne in f:
    if 'S' in ligne:
        y_depart = ligne.index('S')
    grid.append(ligne.replace('\n', ''))

beams.add((0, y_depart))

for i in range(1, len(grid) - 1):
    new_beams = set()

    for beam in beams:
        if grid[beam[0] + 1][beam[1]] == '.':
            new_beams.add((beam[0] + 1, beam[1]))
        else:
            split_total += 1
            new_beams.add((beam[0] + 1, beam[1] - 1))
            new_beams.add((beam[0] + 1, beam[1] + 1))
    beams = new_beams.copy()

print(split_total)
