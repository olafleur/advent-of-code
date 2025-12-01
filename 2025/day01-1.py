f = open("day01-puzzle-input.txt", "r")

curr = 50
count = 0

for ligne in f:
    if ligne[0] == 'R':
        curr = (curr + int(ligne[1:])) % 100
    else:
        curr = (curr - int(ligne[1:])) % 100

    if curr == 0:
        count += 1

print(count)
