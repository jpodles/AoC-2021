with open("data.txt") as file:
    data_list = file.readlines()
    data_list = [int(line.strip()) for line in data_list]


def part_one(data):
    return sum([x < y for x, y in zip(data, data[1:])])


def part_two(data):
    return [x + y + z for x, y, z in zip(data, data[1:], data[2:])]


print("Result part one: " + str(part_one(data_list)))
print("Result part two: " + str(part_one(part_two(data_list))))

