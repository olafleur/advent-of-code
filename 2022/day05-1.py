f = open("day05-puzzle-input.txt", "r")

# stacks = [
#     ['Z', 'N'],
#     ['M', 'C', 'D'],
#     ['P']
# ]

stacks = [
    ['Q', 'M', 'G', 'C', 'L'],
    ['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'],
    ['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'],
    ['J', 'F', 'D', 'V', 'Q', 'P'],
    ['N', 'F', 'M', 'S', 'L', 'B', 'T'],
    ['R', 'N', 'V', 'H', 'C', 'D', 'P'],
    ['H', 'C', 'T'],
    ['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'],
    ['Z', 'F', 'H', 'G']
]

for ligne in f:
    first_split = ligne[5:].strip().replace(' ', '').split('from')
    qte = int(first_split[0])
    second_split = first_split[1].split('to')
    depart = int(second_split[0]) - 1
    arrivee = int(second_split[1]) - 1

    for i in range(qte):
        stacks[arrivee].append(stacks[depart][-1])
        stacks[depart] = stacks[depart][:-1]

for ligne in stacks:
    print(ligne[-1])
