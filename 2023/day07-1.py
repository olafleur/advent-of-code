f = open("day07-puzzle-input.txt", "r")


order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
types = ['five', 'four', 'full', 'three', 'two', 'one', 'high']


class Card:
    def __init__(self, card: str):
        self.card = card

    def __lt__(self, other):
        return order.index(self.card) > order.index(other.card)

    def __gt__(self, other):
        return order.index(self.card) < order.index(other.card)


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = self.evaluate_hand()

    def evaluate_hand(self):
        cards_list = list(map(lambda x: x.card, self.cards))
        cards_set = set(cards_list)
        different_cards = len(cards_set)
        occurrences = dict((k, 0) for k in cards_set)

        if different_cards == 1:
            return 'five'
        if different_cards == 4:
            return 'one'
        if different_cards == 5:
            return 'high'
        if different_cards == 2:
            for j in cards_list:
                occurrences[j] += 1

            if occurrences[list(cards_set)[0]] in [2, 3]:
                return 'full'
            return 'four'
        if different_cards == 3:
            for j in cards_list:
                occurrences[j] += 1

            if any(value == 3 for key, value in occurrences.items()):
                return 'three'
            return 'two'

    def __lt__(self, other):
        if self.type != other.type:
            return types.index(self.type) > types.index(other.type)
        else:
            j = 0

            while self.cards[j].card == other.cards[j].card:
                j += 1

            return self.cards[j] < other.cards[j]

    def __gt__(self, other):
        if self.type != other.type:
            return types.index(self.type) < types.index(other.type)
        else:
            j = 0

            while self.cards[j].card == other.cards[j].card:
                j += 1

            return self.cards[j] > other.cards[j]

    def __str__(self):
        result = ''
        for card in self.cards:
            result += card.card
        return result

    @staticmethod
    def generate_hand(string):
        bid = int(string.split(' ')[1])
        cards = string.split(' ')[0]

        return Hand([Card(cards[0]), Card(cards[1]), Card(cards[2]), Card(cards[3]), Card(cards[4])], bid)


hands = []

for line in f:
    hand = Hand.generate_hand(line)
    hands.append(hand)

sorted_hands = sorted(hands)

total_winnings = 0

for i in range(len(sorted_hands)):
    total_winnings += ((i + 1) * sorted_hands[i].bid)

print(total_winnings)
