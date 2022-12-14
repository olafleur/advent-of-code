f = open("day09-small-input.txt", "r")

# R : y+
# U : x-
# L : y-
# D : x+

visited = [(0, 0)]

snake = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]


def move_right(serpent, chiffre):
    for i in range(chiffre):
        serpent[0] = (serpent[0][0], serpent[0][1] + 1)

        for j in range(1, 10):
            if abs(serpent[j-1][0] - serpent[j][0]) > 1 or abs(serpent[j-1][1] - serpent[j][1]) > 1:
                serpent[j] = (serpent[j][0], serpent[j][1] + 1)

                if serpent[j-1][0] > serpent[j][0]:
                    serpent[j] = (serpent[j][0] + 1, serpent[j][1])
                elif serpent[j-1][0] < serpent[j][0]:
                    serpent[j] = (serpent[j][0] - 1, serpent[j][1])

                if j == 9:
                    # La queue bouge!
                    visited.append(serpent[9])
    return serpent


def move_left(serpent, chiffre):
    for i in range(chiffre):
        serpent[0] = (serpent[0][0], serpent[0][1] - 1)

        for j in range(1, 10):
            if abs(serpent[j-1][0] - serpent[j][0]) > 1 or abs(serpent[j-1][1] - serpent[j][1]) > 1:
                serpent[j] = (serpent[j][0], serpent[j][1] - 1)

                if serpent[j-1][0] > serpent[j][0]:
                    serpent[j] = (serpent[j][0] + 1, serpent[j][1])
                elif serpent[j-1][0] < serpent[j][0]:
                    serpent[j] = (serpent[j][0] - 1, serpent[j][1])

                if j == 9:
                    # La queue bouge!
                    visited.append(serpent[9])
        print(serpent)
    return serpent


def move_up(serpent, chiffre):
    for i in range(chiffre):
        serpent[0] = (serpent[0][0] - 1, serpent[0][1])

        for j in range(1, 10):
            if abs(serpent[j-1][0] - serpent[j][0]) > 1 or abs(serpent[j-1][1] - serpent[j][1]) > 1:
                serpent[j] = (serpent[j][0] - 1, serpent[j][1])

                if serpent[j-1][1] > serpent[j][1]:
                    serpent[j] = (serpent[j][0], serpent[j][1] + 1)
                elif serpent[j-1][1] < serpent[j][1]:
                    serpent[j] = (serpent[j][0], serpent[j][1] - 1)

                if j == 9:
                    # La queue bouge!
                    visited.append(serpent[9])
    return serpent


def move_down(serpent, chiffre):
    for i in range(chiffre):
        serpent[0] = (serpent[0][0] + 1, serpent[0][1])

        for j in range(1, 10):
            if abs(serpent[j-1][0] - serpent[j][0]) > 1 or abs(serpent[j-1][1] - serpent[j][1]) > 1:
                serpent[j] = (serpent[j][0] + 1, serpent[j][1])

                if serpent[j-1][1] > serpent[j][1]:
                    serpent[j] = (serpent[j][0], serpent[j][1] + 1)
                elif serpent[j-1][1] < serpent[j][1]:
                    serpent[j] = (serpent[j][0], serpent[j][1] - 1)

                if j == 9:
                    # La queue bouge!
                    visited.append(serpent[9])
    return serpent


for deplacement in f:
    print(deplacement)
    [move, number] = deplacement.split()
    num = int(number)

    if move == 'R':
        snake = move_right(snake, num)
    elif move == 'U':
        snake = move_up(snake, num)
    elif move == 'D':
        snake = move_down(snake, num)
    elif move == 'L':
        snake = move_left(snake, num)

    # print(snake)

print(len(set(visited)))
print(visited)
