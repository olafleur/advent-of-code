f = open("day10-puzzle-input.txt", "r")

chaines = f.readlines()

joltages = list(map(lambda x: int(x), chaines))

max = max(joltages)

joltages.append(0)
joltages.append(max + 3)
joltages.sort()

count = 0


def agrandir(liste):
    global count
    derniere = liste[-1]

    if derniere == max + 3:
        count += 1
        print(liste)
        return

    if derniere + 1 in joltages:
        liste1 = liste[:]
        liste1.append(derniere + 1)
        agrandir(liste1)
    if derniere + 2 in joltages:
        liste2 = liste[:]
        liste2.append(derniere + 2)
        agrandir(liste2)
    if derniere + 3 in joltages:
        liste3 = liste[:]
        liste3.append(derniere + 3)
        agrandir(liste3)

    return


agrandir([0])
print(count)
