f = open("day01-puzzle-input.txt", "r")

list1 = []
list2 = []

total = 0

for ligne in f:
    tableau = ligne.split()
    list1.append(int(tableau[0]))
    list2.append(int(tableau[1]))

list1.sort()
list2.sort()

for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)
