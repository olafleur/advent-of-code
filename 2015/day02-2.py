f = open("day02-puzzle-input.txt", "r")

total = 0

for ligne in f:
    split = ligne.split('x')
    l = int(split[0])
    w = int(split[1])
    h = int(split[2])

    trier = sorted([l, w, h])
    print(trier)

    total += l*w*h + 2*trier[0] + 2*trier[1]

print(total)
