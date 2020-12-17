f = open("day02-puzzle-input.txt", "r")

total = 0

for ligne in f:
    split = ligne.split('x')
    l = int(split[0])
    w = int(split[1])
    h = int(split[2])

    minimum = min(l*w, w*h, h*l)
    print((l, w, h, minimum))

    total += 2*l*w + 2*w*h + 2*h*l + minimum

print(total)
