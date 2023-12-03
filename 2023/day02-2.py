f = open("day02-puzzle-input.txt", "r")


class Game:
    def __init__(self, idd, sets):
        self.id = idd
        self.sets = sets

    def power(self):
        higher_red = 0
        higher_green = 0
        higher_blue = 0

        for setz in self.sets:
            if setz[0] > higher_red:
                higher_red = setz[0]

            if setz[1] > higher_green:
                higher_green = setz[1]

            if setz[2] > higher_blue:
                higher_blue = setz[2]

        return higher_red * higher_green * higher_blue

    @staticmethod
    def create_game(string):
        idd = string.split(':')[0].split(' ')[1]
        string_sets = string.split(':')[1].split(';')
        sets = []

        for one_string_set in string_sets:
            one_set = [0, 0, 0]
            set_split = one_string_set.split(',')
            for color_string in set_split:
                qty = int(color_string[1:].split(' ')[0])
                color = color_string[1:].split(' ')[1]

                if 'red' in color:
                    one_set[0] = qty
                elif 'green' in color:
                    one_set[1] = qty
                elif 'blue' in color:
                    one_set[2] = qty

            sets.append(one_set)

        return Game(int(idd), sets)


total = 0

for line in f:
    game = Game.create_game(line)

    total += game.power()

print(total)
