f = open("day5-puzzle-input.txt", "r")
max_id = 0

def calculer_id(chaine):
    exposant_bf = 6
    exposant_rl = 2
    total_bf = 0
    total_rl = 0

    for i in range(7):
        if chaine[i] == 'B':
            total_bf += pow(2, exposant_bf)
        exposant_bf -= 1

    for i in range(3):
        if chaine[7 + i] == 'R':
            total_rl += pow(2, exposant_rl)
        exposant_rl -= 1

    return total_bf * 8 + total_rl


for ligne in f:
    seat_id = calculer_id(ligne)
    if seat_id > max_id:
        max_id = seat_id

print(max_id)
