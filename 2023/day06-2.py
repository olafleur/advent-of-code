f = open("day06-puzzle-input.txt", "r")

time = int(f.readline().split(':')[1].replace(' ', ''))
distance = int(f.readline().split(':')[1].replace(' ', ''))

speed = 0
travel_distance = 0
nb_of_wins = 0

for i in range(time):
    speed = i
    travel_distance = (time - i) * speed

    if travel_distance > distance:
        nb_of_wins += 1

print(nb_of_wins)
