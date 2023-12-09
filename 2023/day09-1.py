f = open("day09-puzzle-input.txt", "r")


def calculate_next_iteration(array):
    next_iteration = []
    for i in range(1, len(array)):
        next_iteration.append(array[i]-array[i-1])

    return next_iteration


def extrapolate(nums):
    steps = [nums]

    while len(set(nums)) != 1 or nums[0] != 0:
        nums = calculate_next_iteration(nums)
        steps.append(nums)

    steps_order = steps[::-1]
    steps_order[0].append(0)

    for i in range(1, len(steps[::-1])):
        steps_order[i].append(steps_order[i][-1] + steps_order[i-1][-1])

    print(steps_order)
    return steps_order[-1][-1]


extrapolated = []

for line in f:
    numbers_line = line.split(' ')
    numbers = list(map(lambda x: int(x.strip()), numbers_line))
    extrapolated.append(extrapolate(numbers))

print(sum(extrapolated))
