f = open("day07-puzzle-input.txt", "r")

total = 0


def has_valid_path(calib, partial, remaining_numbers):
    new_sum = partial + remaining_numbers[0]
    new_product = partial * remaining_numbers[0]

    if len(remaining_numbers) == 1:
        return new_sum == calib or new_product == calib
    elif new_sum > calib and new_product > calib:
        return False
    elif new_sum > calib or new_product > calib:
        if new_sum > calib:
            return has_valid_path(calib, new_product, remaining_numbers[1:])
        else:
            return has_valid_path(calib, new_sum, remaining_numbers[1:])
    else:
        return has_valid_path(calib, new_sum, remaining_numbers[1:]) or \
            has_valid_path(calib, new_product, remaining_numbers[1:])


for line in f:
    calibration = int(line.split(': ')[0])
    numbers = list(map(int, line.split(': ')[1].split(' ')))
    partial_sum = numbers[0]

    if has_valid_path(calibration, partial_sum, numbers[1:]):
        total += calibration

print(total)







