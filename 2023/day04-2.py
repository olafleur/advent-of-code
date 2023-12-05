f = open("day04-puzzle-input.txt", "r")


class Card:
    def __init__(self, idd, winning, numbers):
        self.id = idd
        self.winning = winning
        self.numbers = numbers

    def nb_of_winning_numbers(self):
        number_winning = 0

        for number in self.numbers:
            if number in self.winning:
                number_winning += 1

        return number_winning

    @staticmethod
    def generate_card_from_line(string):
        [winning_string, numbers_string] = string.split(':')[1].split('|')
        winning = list(map(lambda n: int(n), list(filter(lambda n: n != '', winning_string.split(' ')))))
        numbers = list(map(lambda n: int(n), list(filter(lambda n: n != '', numbers_string.split(' ')))))

        extracted_id = int(string.split(':')[0].split(' ')[-1])

        return Card(extracted_id, winning, numbers)


total = 0
all_values = {}
all_instances = {}


def real_value_of_card(number):
    nb_of_copies = all_values[number]

    for i in range(nb_of_copies):
        all_instances[number+i+1] += 1
        real_value_of_card(number+i+1)


for line in f:
    card = Card.generate_card_from_line(line)
    all_values[card.id] = card.nb_of_winning_numbers()
    all_instances[card.id] = 1

for card_number in all_instances:
    real_value_of_card(card_number)

total = 0

for card_number, value in all_instances.items():
    total += value

print(total)
