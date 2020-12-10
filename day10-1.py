f = open("day10-puzzle-input.txt", "r")

chaines = f.readlines()

joltages = list(map(lambda x: int(x), chaines))

max = max(joltages)

joltages.append(0)
joltages.append(max + 3)
joltages.sort()

diff_3 = 0
diff_1 = 0

for i in range(len(joltages) - 1):
    if joltages[i+1] - joltages[i] == 3:
        diff_3 += 1
    elif joltages[i+1] - joltages[i] == 1:
        diff_1 += 1
    else:
        print(joltages[i+1] - joltages[i])

print(joltages)
print(diff_1)
print(diff_3)
print(diff_3 * diff_1)