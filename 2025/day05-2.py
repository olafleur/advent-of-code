f = open("day05-puzzle-input.txt", "r")

ranges = []
points = set()

for ligne in f:
    if '-' in ligne:
        (x, y) = (ligne.replace('\n', '').split('-'))
        ranges.append((int(x), int(y)))
        points.add(int(x))
        points.add(int(y))


def val_in_ranges(value):
    nb_ranges = len(ranges)
    i = 0

    while i < nb_ranges:
        if ranges[i][0] <= value <= ranges[i][1]:
            return True
        i += 1

    return False


sorted_points = list(points)
sorted_points.sort()

current = sorted_points[0]
count = len(sorted_points)

for point in sorted_points[1:]:
    if val_in_ranges(point - 1):
        count += (point - current - 1)
    current = point

print(count)
