import math

f = open("day08-puzzle-input.txt", "r")

instructions = f.readline().strip()
f.readline()  # empty
mappings = {}
currents = []

for line in f.readlines():
    key = line.split('=')[0].strip()
    left = line.split('(')[1].split(',')[0]
    right = line.split(', ')[1][:3]

    mappings[key] = (left, right)

    if key[2] == 'A':
        currents.append(key)

nb_steps = 0


def transition(inst, curr):
    if inst == 'L':
        result = mappings[curr][0]
    else:
        result = mappings[curr][1]

    return result


nb_found = 0
founds = {x: [] for x in currents}

for current in currents:
    new_current = current

    while new_current[2] != 'Z':
        instruction = instructions[nb_steps % len(instructions)]

        new_current = transition(instruction, new_current)

        if new_current[2] == 'Z':
            founds[current] += [(new_current, nb_steps+1)]

        nb_steps += 1

    nb_steps = 0

print(founds)
print(math.lcm(21409, 14363, 15989, 16531, 19241, 19783))
