f = open("day01-puzzle-input.txt", "r")

total = 0


def contains_number(string):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']

    return any(x in string for x in numbers)


def extract_number(string):
    conversion = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for key, value in conversion.items():
        if key in string:
            return value


for line in f:
    i = 0
    j = len(line) - 1
    number1 = 0
    number2 = 0

    while not line[i].isnumeric() and not contains_number(line[:i+1]):
        i += 1

    if line[i].isnumeric():
        number1 = line[i]
    else:
        number1 = extract_number(line[:i+1])

    while not line[j].isnumeric() and not contains_number(line[j:]):
        j -= 1

    if line[j].isnumeric():
        number2 = line[j]
    else:
        number2 = extract_number(line[j:])

    number = number1 + number2

    print(number)

    total += int(number)


print(total)
