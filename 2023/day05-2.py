import sys

f = open("day05-puzzle-input.txt", "r")


class Range:
    def __init__(self, destination_start, source_start, range_length):
        self.destination_start = destination_start
        self.source_start = source_start
        self.range_length = range_length

    def source_in_range(self, value):
        return self.source_start <= value < self.source_start + self.range_length

    def calculate_destination(self, value):
        diff = value - self.source_start

        return self.destination_start + diff


class Map:
    def __init__(self, rangezs):
        self.rangezs = rangezs

    def apply_map_to_interval(self, intervalz):
        result = []
        for rangez in self.rangezs:
            if rangez.source_in_range(intervalz[0]):
                if rangez.source_in_range(intervalz[1]):
                    result.append([rangez.calculate_destination(intervalz[0]), rangez.calculate_destination(intervalz[1])])
                else:
                    k = intervalz[0]

                    while rangez.source_in_range(k):
                        k += 1

                    result.append([rangez.calculate_destination(intervalz[0]), rangez.calculate_destination(k-1)])

                    if k != intervalz[1]:
                        result += self.apply_map_to_interval([k, intervalz[1]])

        if not result:
            return [intervalz]

        return result


seeds = list(map(lambda x: int(x.strip()), f.readline().split(': ')[1].split(' ')))

intervals = []

for i in range(0, len(seeds), 2):
    intervals.append([seeds[i], seeds[i] + seeds[i + 1] - 1])

f.readline()

maps = []
ranges = []

while True:
    line = f.readline()

    if not line:
        maps.append(Map(ranges))
        break

    if line == '\n':
        maps.append(Map(ranges))
        ranges = []
    elif line[0].isnumeric():
        one_range = list(map(lambda x: int(x.strip()), line.split(' ')))
        ranges.append(Range(one_range[0], one_range[1], one_range[2]))


for mapz in maps:
    new_intervals = []

    for interval in intervals:
        new_intervals += mapz.apply_map_to_interval(interval)

    intervals = new_intervals.copy()


mini = sys.maxsize

for inte in intervals:
    if inte[0] < int(mini):
        mini = inte[0]

print(mini)
