from functools import reduce
import operator

f = open("day06-puzzle-input.txt", "r")


def parse_line():
    return list(map(lambda y: int(y.strip()), filter(lambda x: x != '', f.readline().split(':')[1].split(' '))))


times = parse_line()
distances = parse_line()
wins = []

for race in range(len(times)):
    speed = 0
    race_duration = times[race]
    travel_distance = 0
    nb_of_wins = 0

    for i in range(race_duration):
        speed = i
        travel_distance = (race_duration - i) * speed

        if travel_distance > distances[race]:
            nb_of_wins += 1

    wins.append(nb_of_wins)

print(reduce(operator.mul, wins, 1))
