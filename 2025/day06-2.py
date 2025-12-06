from functools import reduce
from operator import mul

f = open("day06-puzzle-input.txt", "r")

grid = []
nombres_courants = []
op_courante = ''
total = 0

for ligne in f:
    grid.append(ligne.replace('\n', '').replace('a', ''))

for i in range(len(grid[0])):
    colonne = []
    for j in range(len(grid)):
        colonne.append(grid[j][i])

    if ''.join(colonne[:-1]).strip() != '':
        nombre = int(''.join(colonne[:-1]))
        nombres_courants.append(nombre)

        if colonne[-1] == '*':
            op_courante = '*'
        elif colonne[-1] == '+':
            op_courante = '+'
    else:
        if op_courante == '+':
            total += sum(nombres_courants)
        else:
            total += reduce(mul, nombres_courants)

        nombres_courants = []

if op_courante == '+':
    total += sum(nombres_courants)
else:
    total += reduce(mul, nombres_courants)

print(total)


