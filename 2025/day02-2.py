f = open("day02-puzzle-input.txt", "r")

count = 0

chaine = f.readline()
valeurs = chaine.split(',')
results = set()
lengths = set()


def is_invalid(num):
    str_version = str(num)
    lengths.add(len(str_version))

    if num >= 10 and len(set(str_version)) == 1:
        return True

    if len(str_version) == 2:
        return str_version[0] == str_version[1]

    if len(str_version) == 4:
        return str_version[:2] == str_version[2:]

    if len(str_version) == 6:
        return str_version[:3] == str_version[3:] or str_version[:2] == str_version[2:4] == str_version[4:]

    if len(str_version) == 8:
        return str_version[:4] == str_version[4:]

    if len(str_version) == 9:
        return str_version[:3] == str_version[3:6] == str_version[6:]

    if len(str_version) == 10:
        return str_version[:5] == str_version[5:] or str_version[:2] == str_version[2:4] == str_version[4:6] == str_version[6:8] == str_version[8:]

    return False


for vals in valeurs:
    begin = int(vals.split('-')[0])
    end = int(vals.split('-')[1])
    for number in range(begin, end + 1):
        if is_invalid(number):
            results.add(number)

print(len(results))
print(sum(results))
