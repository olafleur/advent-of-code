import time

start_time = time.time()
tableau = [5, 2, 8, 16, 18, 0, 1]
nombre_interessant = 30000000
nombres_vus = dict()

for i in range(len(tableau)):
    nombres_vus[tableau[i]] = i


def first_time(nb):
    return nb not in nombres_vus


def trouver_avant(nb):
    return nombres_vus[nb]


for i in range(len(tableau) - 1, nombre_interessant):
    if first_time(tableau[i]):
        tableau.append(0)
    else:
        index = trouver_avant(tableau[i])
        tableau.append(i - index)

    nombres_vus[tableau[i]] = i

print(tableau[nombre_interessant - 1])
print("--- %s seconds ---" % (time.time() - start_time))  # 24.49664807319641 seconds
