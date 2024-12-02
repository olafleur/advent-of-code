f = open("day02-puzzle-input.txt", "r")

total = 0

potential = []


def is_safe(entry, first=True):
    increase = True

    if entry[1] == entry[0]:
        if first:
            potential.append(entry)
        return False

    if entry[1] < entry[0]:
        increase = False

    for i in range(0, len(entry)-1):
        if increase:
            if entry[i] > entry[i+1]:
                if first:
                    potential.append(entry)
                return False
            else:
                if entry[i+1] - entry[i] > 3 or entry[i+1] - entry[i] < 1:
                    if first:
                        potential.append(entry)
                    return False
        else:
            if entry[i] < entry[i+1]:
                if first:
                    potential.append(entry)
                return False
            else:
                if entry[i] - entry[i+1] > 3 or entry[i] - entry[i+1] < 1:
                    if first:
                        potential.append(entry)
                    return False

    return True


for ligne in f:
    if is_safe(list(map(int, ligne.split()))):
        total += 1

for potent in potential:
    print('-----potent', potent)
    proof = False

    for i in range(len(potent)):
        second = potent.copy()
        del second[i]
        print('second', second)
        if is_safe(second, False):
            print(second, 'is safe')
            total += 1
            break

print(total)
