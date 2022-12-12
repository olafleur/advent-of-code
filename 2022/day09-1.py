f = open("day09-puzzle-input.txt", "r")

# R : y+
# U : x-
# L : y-
# D : x+

h = (0, 0)
t = (0, 0)
visited = [(0, 0)]


def move_right(h2, t2, chiffre):
    for i in range(chiffre):
        h2 = (h2[0], h2[1] + 1)

        if abs(h2[0] - t2[0]) > 1 or abs(h2[1] - t2[1]) > 1:
            t2 = (t2[0], t2[1] + 1)

            if h2[0] > t2[0]:
                t2 = (t2[0] + 1, t2[1])
            elif h2[0] < t2[0]:
                t2 = (t2[0] - 1, t2[1])

            visited.append(t2)

    return [h2, t2]


def move_left(h2, t2, chiffre):
    for i in range(chiffre):
        h2 = (h2[0], h2[1] - 1)

        if abs(h2[0] - t2[0]) > 1 or abs(h2[1] - t2[1]) > 1:
            t2 = (t2[0], t2[1] - 1)

            if h2[0] > t2[0]:
                t2 = (t2[0] + 1, t2[1])
            elif h2[0] < t2[0]:
                t2 = (t2[0] - 1, t2[1])

            visited.append(t2)

    return [h2, t2]


def move_up(h2, t2, chiffre):
    for i in range(chiffre):
        h2 = (h2[0] - 1, h2[1])

        if abs(h2[0] - t2[0]) > 1 or abs(h2[1] - t2[1]) > 1:
            t2 = (t2[0] - 1, t2[1])

            if h2[1] > t2[1]:
                t2 = (t2[0], t2[1] + 1)
            elif h2[1] < t2[1]:
                t2 = (t2[0], t2[1] - 1)

            visited.append(t2)

    return [h2, t2]


def move_down(h2, t2, chiffre):
    for i in range(chiffre):
        h2 = (h2[0] + 1, h2[1])

        if abs(h2[0] - t2[0]) > 1 or abs(h2[1] - t2[1]) > 1:
            t2 = (t2[0] + 1, t2[1])

            if h2[1] > t2[1]:
                t2 = (t2[0], t2[1] + 1)
            elif h2[1] < t2[1]:
                t2 = (t2[0], t2[1] - 1)

            visited.append(t2)

    return [h2, t2]


for deplacement in f:
    [move, number] = deplacement.split()
    num = int(number)

    if move == 'R':
        [h, t] = move_right(h, t, num)
    elif move == 'U':
        [h, t] = move_up(h, t, num)
    elif move == 'D':
        [h, t] = move_down(h, t, num)
    elif move == 'L':
        [h, t] = move_left(h, t, num)

print(len(set(visited)))
