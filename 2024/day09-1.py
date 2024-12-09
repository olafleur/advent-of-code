f = open("day09-puzzle-input.txt", "r")

ligne = f.readline().rstrip('\n')
chiffres = list(map(int, ligne))

empty = False
file_no = 0
disk = []
checksum = 0

# convert to disk representation
for chiffre in chiffres:
    if not empty:
        for i in range(chiffre):
            disk.append(file_no)
        file_no += 1
        empty = True
    else:
        for i in range(chiffre):
            disk.append('.')
        empty = False


def disk_has_space():
    space = False

    for elem in disk:
        if elem == '.':
            space = True

        if elem != '.' and space:
            return True

    return False


def shift_to_compact():
    to_move = 0
    space_index = 0

    for i in reversed(range(len(disk))):
        if disk[i] != '.':
            to_move = i
            break

    for i in range(len(disk)):
        if disk[i] == '.':
            space_index = i
            break

    disk[space_index] = disk[to_move]
    disk[to_move] = '.'


while disk_has_space():
    shift_to_compact()

for i in range(len(disk)):
    if disk[i] != '.':
        checksum += i*disk[i]

print(checksum)
