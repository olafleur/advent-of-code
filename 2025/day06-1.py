from functools import reduce
from operator import mul

f = open("day06-puzzle-input.txt", "r")

numbers = []
operations = []
total = 0

for ligne in f:
    if '+' not in ligne:
        numbers.append(list(map(lambda x: int(x), ligne.split())))
    else:
        operations = ligne.split()

for i in range(len(numbers[0])):
    calculands = []
    if operations[i] == '+':
        for j in range(len(numbers)):
            calculands.append(numbers[j][i])
        total += sum(calculands)
    else:
        for j in range(len(numbers)):
            calculands.append(numbers[j][i])
        total += reduce(mul, calculands)

print(total)
