from collections import defaultdict

with open("data.txt") as file:
    data_list = file.readlines()


def part_one(data: list):
    data_dict = defaultdict(list)
    sum_dict = defaultdict(list)
    for line in data:
        key, value = line.split()
        data_dict[key].append(int(value))
    for k in data_dict.keys():
        sum_dict[k].append(sum(data_dict[k]))
    return sum_dict['forward'][0] * (sum_dict['down'][0] - sum_dict['up'][0])


def part_two(data: list):
    horizontal = 0
    depth = 0
    aim = 0

    for line in data:
        key, value = line.split()
        value = int(value)
        if key == 'forward':
            horizontal += value
            if aim != 0:
                depth += value * aim
        if key == 'up':
            aim -= value
        if key == 'down':
            aim += value
    return horizontal * depth


print(f'Part one: {int(part_one(data_list))}')
print(f'Part two: {int(part_two(data_list))}')
