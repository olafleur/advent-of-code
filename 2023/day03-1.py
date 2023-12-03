f = open("day03-puzzle-input.txt", "r")

i = 0
content = []
numbers = []
line_max = 0
num_of_lines = 0


class Number:
    def __init__(self, value, line_num, c1, c2):
        self.value = value
        self.line_num = line_num
        self.c1 = c1
        self.c2 = c2

    def has_symbol(self):
        coords_to_check = [[self.line_num, self.c1-1], [self.line_num, self.c2+1]]

        for k in range(self.c1-1, self.c2+2):
            coords_to_check.append([self.line_num-1, k])
            coords_to_check.append([self.line_num+1, k])

        results = list(filter(lambda coord: 0 <= coord[0] <= line_max and 0 <= coord[1] < num_of_lines, coords_to_check))

        return any(content[result[0]][result[1]] != '.' for result in results)

    @staticmethod
    def create_numbers_from_string(line_num, string):
        j = 0
        current_num = ''
        current_begin = 0
        num_objects = []

        while j < len(string):
            if string[j].isnumeric():
                if current_num == '':
                    current_begin = j
                current_num += string[j]
            else:
                if current_num != '':
                    num_objects.append(Number(int(current_num), line_num, current_begin, j-1))

                current_num = ''
            j += 1

        return num_objects


for string_line in f:
    line = []
    line_max = len(string_line) - 1

    numbers += Number.create_numbers_from_string(i, string_line)

    for char in string_line[:len(string_line)-1]:
        line.append(char)

    i += 1
    num_of_lines += 1
    content.append(line)


total = 0

for x in numbers:
    if x.has_symbol():
        total += x.value

print(total)
