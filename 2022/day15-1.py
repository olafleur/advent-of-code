f = open("day15-puzzle-input.txt", "r")

points = []
sensors = []
beacons = []
max_dist = 0

VAL_Y = 2000000


def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))


def add_points(x, y, dist_here):
    for xt in range(x - dist_here + 1, x + dist_here - 1):
        if manhattan([x, y], [xt, VAL_Y]) <= dist_here:
            points.append(xt)


for line in f:
    clean = line.replace('Sensor at x=', '').replace(' closest beacon is at ', '')
    x_sensor = int(clean.split(', y=')[0])
    y_sensor = int(clean.split(', y=')[1].split(':x=')[0])
    x_beacon = int(clean.split(', y=')[1].split(':x=')[1])
    y_beacon = int(clean.split(', y=')[2])

    sensors.append((x_sensor, y_sensor))
    beacons.append((x_beacon, y_beacon))

    dist_la = manhattan([x_sensor, y_sensor], [x_beacon, y_beacon])

    if dist_la > max_dist:
        max_dist = dist_la


for i in range(len(sensors)):
    dist_local = manhattan([sensors[i][0], sensors[i][1]], [beacons[i][0], beacons[i][1]])

    if VAL_Y - dist_local < sensors[i][1] < VAL_Y + dist_local:
        add_points(sensors[i][0], sensors[i][1], dist_local)

points_clean = list(filter(lambda x: (x, VAL_Y) not in beacons, points))
points_clean.sort()
print(set(points_clean))
print(len(set(points_clean)))
