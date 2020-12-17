f = open("day01-puzzle-input.txt", "r")

ligne = f.readline()

somme = 0

for caractere in ligne:
    if caractere == '(':
        somme += 1
    elif caractere == ')':
        somme -= 1

print(somme)
