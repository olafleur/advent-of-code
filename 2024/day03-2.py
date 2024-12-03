f = open("day03-puzzle-input.txt", "r")

everything = ""
total = 0
enabled = True

for ligne in f:
    for char in ligne:
        everything += char

counter = 0
num1 = ""
num2 = ""

for i in range(len(everything)):
    num1 = ""
    num2 = ""

    if everything[i:].startswith('do()'):
        enabled = True

    if everything[i:].startswith("don't()"):
        enabled = False

    if everything[i:].startswith('mul(') and enabled:
        counter = i + 4

        while everything[counter].isnumeric():
            num1 += everything[counter]
            counter += 1

        if everything[counter] == ',':
            counter += 1

        while everything[counter].isnumeric():
            num2 += everything[counter]
            counter += 1

        if everything[counter] == ')':
            total += int(num1) * int(num2)

print(total)
