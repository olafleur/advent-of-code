f = open("day14-puzzle-input.txt", "r")

content = []

for line in f:
    content.append(line.strip())


def replace_char(string, index, c):
    return string[:index] + c + string[index + 1:]


def tilt_north():
    for i in range(1, len(content)):
        for j in range(len(content[0])):
            if content[i][j] == 'O' and content[i-1][j] == '.':
                up = i-1
                while content[up][j] == '.' and up >= 0:
                    up -= 1

                content[i] = replace_char(content[i], j, '.')
                content[up+1] = replace_char(content[up+1], j, 'O')


def tilt_west():
    for i in range(len(content)):
        for j in range(1, len(content[0])):
            if content[i][j] == 'O' and content[i][j-1] == '.':
                left = j-1
                while content[i][left] == '.' and left >= 0:
                    left -= 1

                content[i] = replace_char(content[i], j, '.')
                content[i] = replace_char(content[i], left+1, 'O')


def tilt_south():
    for i in range(len(content)-2, -1, -1):
        for j in range(len(content[0])):
            if content[i][j] == 'O' and content[i+1][j] == '.':
                down = i+1
                while down <= len(content)-1 and content[down][j] == '.':
                    down += 1
                content[i] = replace_char(content[i], j, '.')
                content[down-1] = replace_char(content[down-1], j, 'O')


def tilt_east():
    for i in range(len(content)):
        for j in range(len(content[0])-2, -1, -1):
            if content[i][j] == 'O' and content[i][j+1] == '.':
                right = j+1
                while right < len(content[0]) and content[i][right] == '.':
                    right += 1

                content[i] = replace_char(content[i], j, '.')
                content[i] = replace_char(content[i], right-1, 'O')


def calculate_load():
    total = 0
    load = len(content)
    for line in content:
        for char in line:
            if char == 'O':
                total += load
        load -= 1

    return total


def cycle():
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()


for i in range(1000):
    cycle()

    print('after cycle', (i+1) % 38, calculate_load())


for line in content:
    print(line)

load = len(content)
total = 0

print(1000000000 % 38)

# 18 is 104409
