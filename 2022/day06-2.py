f = open("day06-puzzle-input.txt", "r")

chaine = f.readline()

for i in range(len(chaine)):
    ensemble = set(chaine[i:i+14])

    if len(ensemble) == 14:
        print(i + 14)

