import math

f = open("day08-puzzle-input.txt", "r")

coords = []
dist = {}
used = set()
circuits = []

for ligne in f:
    coord = ligne.replace('\n', '').split(',')
    coords.append([int(coord[0]), int(coord[1]), int(coord[2])])

for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        dist[(i, j)] = math.dist(coords[i], coords[j])

# print(dist)

def find_point_in_circuits(point):
    for k in range(len(circuits)):
        if point in circuits[k]:
            return k


for i in range(1000):
    min_key = min(dist, key=dist.get)
    # print(coords[min_key[0]], coords[min_key[1]], dist[min_key])
    del dist[min_key]
    if min_key[0] not in used and min_key[1] not in used:
        circuits.append([min_key[0], min_key[1]])
    elif min_key[0] not in used:
        index = find_point_in_circuits(min_key[1])
        circuits[index].append(min_key[0])
    elif min_key[1] not in used:
        index = find_point_in_circuits(min_key[0])
        circuits[index].append(min_key[1])
    elif find_point_in_circuits(min_key[0]) != find_point_in_circuits(min_key[1]):
        index0 = find_point_in_circuits(min_key[0])
        index1 = find_point_in_circuits(min_key[1])

        circuits[index0].extend(circuits[index1])
        del circuits[index1]

    used.add(min_key[0])
    used.add(min_key[1])

max_len1 = len(max(circuits, key=len))
index = circuits.index(max(circuits, key=len))
del circuits[index]

max_len2 = len(max(circuits, key=len))
index = circuits.index(max(circuits, key=len))
del circuits[index]

max_len3 = len(max(circuits, key=len))

print(max_len1 * max_len2 * max_len3)
