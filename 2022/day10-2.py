f = open("day10-puzzle-input.txt", "r")

cycle = 1
X = 1


def draw(sprite_center, crt_render):
    if crt_render % 40 in [sprite_center-1, sprite_center, sprite_center+1]:
        char = '#'
    else:
        char = '.'

    if crt_render % 40 == 39:
        print(char)
    else:
        print(char, end='')


for line in f:
    draw(X, cycle-1)
    if line.strip() != 'noop':
        val = int(line.split()[1])
        cycle += 1
        draw(X, cycle-1)
        X += val

    cycle += 1
