f = open("day06-puzzle-input.txt", "r")

chaine = f.readline()

for i in range(len(chaine)):
    ensemble = set(chaine[i:i+4])

    if len(ensemble) == 4:
        print(i + 4)

