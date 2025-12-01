f = open("day01-puzzle-input.txt", "r")

curr = 50
count = 0

for ligne in f:
    if ligne[0] == 'R':
        end = curr + int(ligne[1:])
        count += (end // 100)
        curr = end % 100
    else:
        end = curr - int(ligne[1:])
        if end <= 0 and curr != 0:
            count += (abs(end - 100) // 100)
        elif end <= 0 and curr == 0:
            count += (abs(end - 100) // 100) - 1
        curr = end % 100

print(count)
