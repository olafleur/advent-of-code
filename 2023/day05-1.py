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

    def calculate_output(self, input_value):
        for rangez in self.rangezs:
            if rangez.source_in_range(input_value):
                return rangez.calculate_destination(input_value)

        return input_value


seeds = list(map(lambda x: int(x.strip()), f.readline().split(': ')[1].split(' ')))
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


def calculate_all_mappings(value):
    current_value = value

    for mapz in maps:
        current_value = mapz.calculate_output(current_value)

    return current_value


print(min(list(map(lambda x: calculate_all_mappings(x), seeds))))
