f = open("day05-puzzle-input.txt", "r")

ranges = []
vals = []
count = 0

for ligne in f:
    if '-' in ligne:
        (x, y) = (ligne.replace('\n', '').split('-'))
        ranges.append((int(x), int(y)))
    elif ligne.strip() != '':
        vals.append(int(ligne))


def val_in_ranges(value):
    nb_ranges = len(ranges)
    i = 0

    while i < nb_ranges:
        if ranges[i][0] <= value <= ranges[i][1]:
            return True
        i += 1

    return False


for val in vals:
    if val_in_ranges(val):
        count += 1

print(count)
