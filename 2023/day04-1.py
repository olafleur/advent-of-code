f = open("day04-puzzle-input.txt", "r")


class Card:
    def __init__(self, winning, numbers):
        self.winning = winning
        self.numbers = numbers

    def winning_value(self):
        number_winning = 0

        for number in self.numbers:
            if number in self.winning:
                number_winning += 1

        if number_winning >= 1:
            return 2 ** (number_winning - 1)

        return number_winning

    @staticmethod
    def generate_card_from_line(string):
        [winning_string, numbers_string] = string.split(':')[1].split('|')
        winning = list(map(lambda n: int(n), list(filter(lambda n: n != '', winning_string.split(' ')))))
        numbers = list(map(lambda n: int(n), list(filter(lambda n: n != '', numbers_string.split(' ')))))

        return Card(winning, numbers)


total = 0

for line in f:
    total += Card.generate_card_from_line(line).winning_value()

print(total)
