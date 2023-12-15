f = open("day14-puzzle-input.txt", "r")

content = []

for line in f:
    content.append(line.strip())


def replace_char(string, index, char):
    return string[:index] + char + string[index + 1:]


# tilt
for i in range(1, len(content)):
    for j in range(len(content[0])):
        if content[i][j] == 'O' and content[i-1][j] == '.':
            up = i-1
            while content[up][j] == '.' and up >= 0:
                up -= 1

            content[i] = replace_char(content[i], j, '.')
            content[up+1] = replace_char(content[up+1], j, 'O')

load = len(content)
total = 0

for line in content:
    for char in line:
        if char == 'O':
            total += load
    load -= 1

print(total)
