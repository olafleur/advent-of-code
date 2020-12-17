f = open("day01-puzzle-input.txt", "r")

ligne = f.readline()

somme = 0
position = 0

for caractere in ligne:
    position += 1

    if caractere == '(':
        somme += 1
    elif caractere == ')':
        somme -= 1

    if somme == -1:
        print(position)
        break
