f = open("nelson-input.txt", "r")

nb_publiques = 0
nb_privees = 0
nb_paires = 0


def convertir(chaine):
    adresse = chaine.split('.')

    return list(map(lambda x: int(x), adresse))


adresses = list(map(convertir, f.readlines()))


for adresse in adresses:
    if adresse[0] == 10:
        nb_privees += 1
    elif adresse[0] == 172 and 16 <= adresse[1] <= 31:
        nb_privees += 1
    elif (adresse[0], adresse[1]) == (192, 168):
        nb_privees += 1
    else:
        nb_publiques += 1

    if adresse[0] % 2 == 0 and adresse[1] % 2 == 0 and adresse[2] % 2 == 0 and adresse[3] % 2 == 0:
        nb_paires += 1

print("Nombre privées = " + str(nb_privees))
print("Nombre publiques = " + str(nb_publiques))
print("Réponse #1 = " + str(nb_privees * nb_publiques))
print("Réponse #2 = " + str(nb_paires))
