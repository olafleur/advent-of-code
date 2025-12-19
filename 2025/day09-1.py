f = open("day09-puzzle-input.txt", "r")

pts = []
maximum = 0
max_pt = []

for ligne in f:
    coord = ligne.replace('\n', '').split(',')
    pts.append((int(coord[0]), int(coord[1])))


def calculate_area(pt1, pt2):
    length = abs(pt2[1] - pt1[1]) + 1
    height = abs(pt2[0] - pt1[0]) + 1

    return length * height


for i in range(len(pts)):
    for j in range(i + 1, len(pts)):
        area = calculate_area(pts[i], pts[j])
        if area > maximum:
            maximum = area
            max_pt = [pts[i], pts[j]]


print(maximum, max_pt)
