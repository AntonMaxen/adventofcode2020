def part_one():
    lines = get_lines()
    return boot_program(lines)['acc']


def part_two():
    my_lines = get_lines()

    line_index = 0
    while line_index < len(my_lines):
        lines = my_lines.copy()
        line = lines[line_index]
        if "jmp" in line:
            lines[line_index] = line.replace("jmp", "nop")
        elif "nop" in line:
            lines[line_index] = line.replace("nop", "jmp")

        result = boot_program(lines)
        if result['index'] >= len(lines):
            return result['acc']

        line_index += 1


def get_lines():
    with open("files/day8input.txt") as my_file:
        lines = [line.strip() for line in my_file.readlines()]

    return lines


def add_or_sub(acc, value):
    if "+" in value:
        acc += int(value.split("+")[-1])
    else:
        acc -= int(value.split("-")[-1])

    return acc


def boot_program(lines):
    visited_locations = []
    index = 0
    acc = 0
    while index not in visited_locations and 0 <= index < len(lines):
        visited_locations.append(index)
        line = lines[index]
        cmd, value = line.split()
        if "acc" in cmd:
            acc = add_or_sub(acc, value)
            index += 1
        elif "jmp" in cmd:
            index = add_or_sub(index, value)
        else:
            index += 1

    return {"acc": acc, "index": index}


if __name__ == '__main__':
    print(part_one())
    print(part_two())
