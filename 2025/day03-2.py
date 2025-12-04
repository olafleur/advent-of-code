f = open("day03-puzzle-input.txt", "r")

somme = 0

for ligne in f:
    list_nums = list(map(lambda x: int(x), ligne.replace('\n', '')))

    curr = -1
    chosen = []

    for i in range(12):
        max_val = max(list_nums[curr + 1:i-11]) if i - 11 != 0 else max(list_nums[curr + 1:])
        if i - 11 != 0:
            curr += list_nums[curr + 1:i-11].index(max_val) + 1
        chosen.append(max_val)

    somme += int(''.join(list(map(lambda x: str(x), chosen))))

print(somme)
