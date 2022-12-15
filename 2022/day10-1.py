f = open("day10-puzzle-input.txt", "r")

cycle = 1
X = 1
total = 0


def interesting_cycle(total):
    if cycle in [20, 60, 100, 140, 180, 220]:
        print('cycle ' + str(cycle))
        print('val ' + str(X))
        strength = cycle * X
        print('strength ' + str(strength))
        total += strength
        print('total ' + str(total))

    return total


for line in f:
    total = interesting_cycle(total)

    if line.strip() != 'noop':
        val = int(line.split()[1])
        cycle += 1
        total = interesting_cycle(total)
        X += val

    cycle += 1

