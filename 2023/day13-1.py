f = open("day13-puzzle-input.txt", "r")

patterns = []
pattern = []
current_line = []

for line in f:
    if line == '\n':
        patterns.append(pattern)
        pattern = []
    else:
        for c in line.strip():
            current_line.append(c)

        pattern.append(current_line)
        current_line = []

# last one
patterns.append(pattern)


def vertical_pattern(patt, index1, index2):
    if index1 < 0:
        return True
    if index2 >= len(patt[0]):
        return True

    symmetry = True

    for i in range(len(patt)):
        if patt[i][index1] != patt[i][index2]:
            symmetry = False

    if not symmetry:
        return False

    return vertical_pattern(patt, index1-1, index2+1)


def horizontal_pattern(patt, index1, index2):
    if index1 < 0:
        return True
    if index2 >= len(patt):
        return True

    symmetry = True

    for j in range(len(patt[0])):
        if patt[index1][j] != patt[index2][j]:
            symmetry = False

    if not symmetry:
        return False

    return horizontal_pattern(patt, index1-1, index2+1)


total = 0

for pattern in patterns:
    found = False
    num = 0
    for col in range(1, len(pattern[0])):
        if vertical_pattern(pattern, col-1, col):
            found = True
            num = col
            break

    if found:
        total += num
        found = False
    else:
        for line in range(1, len(pattern)):
            if horizontal_pattern(pattern, line-1, line):
                num = line
                break
        total += 100*num

print(total)


