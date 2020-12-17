from functools import reduce


# code trouvé ici : https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# début de mon code
f = open("day13-puzzle-input.txt", "r")

f.readline()  # ignorer

chaine = f.readline().split(',')

heures = []
les_bus = []
maximum = 0

for valeur in chaine:
    if valeur.isnumeric():
        nombre = int(valeur)

        if nombre > maximum:
            maximum = nombre

        les_bus.append(nombre)

        heures.append(nombre)
    else:
        heures.append(valeur)

les_bus.sort(reverse=True)

indices = []

for bus in les_bus:
    indices.append(heures.index(bus))

nb = maximum - indices[0]

print(indices)
print(les_bus)

a = []

for i in range(len(indices)):
    a.append(les_bus[i] - indices[i])

print(chinese_remainder(les_bus, a))
