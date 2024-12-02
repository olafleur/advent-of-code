f = open("day01-puzzle-input.txt", "r")

list1 = []
list2 = []

total = 0

for ligne in f:
    tableau = ligne.split()
    list1.append(int(tableau[0]))
    list2.append(int(tableau[1]))

for i in range(len(list1)):
    total += list1[i] * list2.count(list1[i])

print(total)
