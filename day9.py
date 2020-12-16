def part_one():
    with open("files/day9input.txt") as my_file:
        lines = [int(line.strip()) for line in my_file.readlines()]

    for index in range(len(lines)):
        if index + 25 <= len(lines):
            preamble = lines[index:index + 25]
            number = lines[index+25]

            found = len([True for x in preamble for y in preamble if x != y and x + y == number]) > 0

            if not found:
                return number


def part_two(invalid):
    with open("files/day9input.txt") as my_file:
        lines = [int(line.strip()) for line in my_file.readlines()]

        for x in range(len(lines)):
            for y in range(len(lines)):
                total_list = lines[x:x+y] if x + y <= len(lines) else lines[x:]
                if sum(total_list) == invalid and invalid not in total_list:
                    total_list.sort()
                    return total_list[0] + total_list[-1]




if __name__ == '__main__':
    invalid = part_one()
    print(invalid)
    print(part_two(invalid))
