f = open("day02-puzzle-input.txt", "r")

total = 0


def is_safe(entry):
    increase = True

    if entry[1] == entry[0]:
        return False

    if entry[1] < entry[0]:
        increase = False

    for i in range(0, len(entry)-1):
        if increase:
            if entry[i] > entry[i+1]:
                return False
            else:
                if entry[i+1] - entry[i] > 3 or entry[i+1] - entry[i] < 1:
                    return False
        else:
            if entry[i] < entry[i+1]:
                return False
            else:
                if entry[i] - entry[i+1] > 3 or entry[i] - entry[i+1] < 1:
                    return False

    return True


for ligne in f:
    if is_safe(list(map(int, ligne.split()))):
        total += 1

print(total)
