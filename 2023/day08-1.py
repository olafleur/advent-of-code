f = open("day08-puzzle-input.txt", "r")

instructions = f.readline().strip()
f.readline()  # empty
mappings = {}

for line in f.readlines():
    key = line.split('=')[0].strip()
    left = line.split('(')[1].split(',')[0]
    right = line.split(', ')[1][:3]

    mappings[key] = (left, right)

current = 'AAA'
nb_steps = 0

while current != 'ZZZ':
    instruction = instructions[nb_steps % len(instructions)]

    if instruction == 'L':
        current = mappings[current][0]
    else:
        current = mappings[current][1]

    nb_steps += 1

print(nb_steps)
