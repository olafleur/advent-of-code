f = open("day03-puzzle-input.txt", "r")

somme = 0

for ligne in f:
    list_nums = list(map(lambda x: int(x), ligne[:-1]))
    max_val1 = max(list_nums[:-1])
    index_of_max = list_nums.index(max_val1)

    max_val2 = max(list_nums[index_of_max + 1:])

    somme += int(str(max_val1) + str(max_val2))

print(somme)

