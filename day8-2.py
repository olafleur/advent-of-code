def structurer(chaine):
    return [chaine[:3], int(chaine[4:]), False]


def creer_instructions():
    f = open("day8-puzzle-input.txt", "r")
    lignes = f.readlines()
    return list(map(structurer, lignes))


def executer(acc, index, inst):
    if index == len(inst):
        print("Programme terminé avec valeur " + str(acc))
        return

    courante = inst[index]

    if courante[2]:
        return

    inst[index][2] = True

    if courante[0] == 'acc':
        acc += courante[1]
        executer(acc, index + 1, inst)
        return

    if courante[0] == 'nop':
        executer(acc, index + 1, inst)
        return

    if courante[0] == 'jmp':
        executer(acc, index + courante[1], inst)
        return


def executer_modifier(inst, index):
    if inst[index][0] == 'jmp':
        inst[index][0] = 'nop'
    elif inst[index][0] == 'nop':
        inst[index][0] = 'jmp'

    executer(0, 0, inst)


for i in range(len(creer_instructions())):
    executer_modifier(creer_instructions(), i)
