f = open("day13-puzzle-input.txt", "r")

heure_depart = int(f.readline())

chaine = f.readline().split(',')

heures = []

for valeur in chaine:
    if valeur != "x":
        heures.append(int(valeur))

bus = 0
temps = heure_depart

while bus == 0:
    for multiple in heures:
        if temps % multiple == 0:
            bus = multiple
    temps += 1

temps -= 1

diff = temps - heure_depart

print(diff * bus)
