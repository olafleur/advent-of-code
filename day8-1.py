f = open("day8-puzzle-input.txt", "r")

lignes = f.readlines()


def structurer(chaine):
    return [chaine[:3], int(chaine[4:]), False]


instructions = list(map(structurer, lignes))


def executer(acc, index):
    courante = instructions[index]

    if courante[2]:
        print(acc)
        return

    instructions[index][2] = True

    if courante[0] == 'acc':
        acc += courante[1]
        executer(acc, index + 1)
        return

    if courante[0] == 'nop':
        executer(acc, index + 1)
        return

    if courante[0] == 'jmp':
        executer(acc, index + courante[1])
        return


executer(0, 0)

