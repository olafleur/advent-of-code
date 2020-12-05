f = open("day1-1-puzzle-input.txt", "r")
nombres = []

for x in f:
    nombres.append(int(x))

for nombre in range(len(nombres)):
    for deuxieme in range(nombre, len(nombres)):
        if nombres[nombre] + nombres[deuxieme] == 2020:
            print(nombres[nombre])
            print(nombres[deuxieme])
            print(nombres[nombre] * nombres[deuxieme])
