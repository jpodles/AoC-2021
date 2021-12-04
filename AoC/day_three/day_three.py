with open("data.txt") as file:
    data_list = [line.strip() for line in file]


def most_common(data: list):
    return [1 if t.count('1') >= t.count('0') else 0 for t in data]


def least_common(data: list):
    return [0 if t.count('1') >= t.count('0') else 1 for t in data]


def reverse_array(data: list):
    return list(zip(*data[::-1]))


def part_one(data: list):
    d = reverse_array(data)
    most_common_list = most_common(d)
    least_common_list = least_common(d)
    most, least = 0, 0
    for bit in most_common_list:
        most = (most << 1) | bit
    for bit in least_common_list:
        least = (least << 1) | bit
    return most * least


print(f'Part one: {part_one(data_list)}')



