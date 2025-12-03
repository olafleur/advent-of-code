f = open("day02-puzzle-input.txt", "r")

count = 0

chaine = f.readline()
valeurs = chaine.split(',')
results = set()


def is_invalid(num):
    str_version = str(num)

    if len(str_version) % 2 != 0:
        return False

    half = len(str_version) // 2

    return str_version[:half] == str_version[half:]


for vals in valeurs:
    begin = int(vals.split('-')[0])
    end = int(vals.split('-')[1])
    for number in range(begin, end + 1):
        if is_invalid(number):
            results.add(number)

print(len(results))
print(sum(results))
