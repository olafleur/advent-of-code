f = open("day12-puzzle-input.txt", "r")


def is_valid_arrangement(string, numbers):
    current_series_number = 0
    calculated_numbers = []

    for char in string:
        if char == '#':
            current_series_number += 1
        if char == '.':
            if current_series_number > 0:
                calculated_numbers.append(current_series_number)
                current_series_number = 0

    if current_series_number > 0:
        calculated_numbers.append(current_series_number)

    return calculated_numbers == numbers


def replace_char(string, index, char):
    return string[:index] + char + string[index + 1:]


def nb_of_valid_arrangements(pattern, question_marks, numbers):
    if len(question_marks) == 0:
        return 1 if is_valid_arrangement(pattern, numbers) else 0

    option1 = replace_char(pattern, question_marks[0], '#')
    option2 = replace_char(pattern, question_marks[0], '.')

    return nb_of_valid_arrangements(option1, question_marks[1:], numbers) +\
        nb_of_valid_arrangements(option2, question_marks[1:], numbers)


patterns = []
numbers = []

for line in f:
    patterns.append(line.split(' ')[0])
    numbers.append(list(map(lambda x: int(x.strip()), line.split(' ')[1].split(','))))

valids = []

for p in range(len(patterns)):
    valid_patterns = 0
    current_pattern = patterns[p]
    question_indexs = []

    for i in range(len(current_pattern)):
        if current_pattern[i] == '?':
            question_indexs.append(i)

    valids.append(nb_of_valid_arrangements(current_pattern, question_indexs, numbers[p]))

print(sum(valids))
