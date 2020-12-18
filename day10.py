def part_one():
    with open("files/day10input.txt") as my_file:
        adapters = [int(line.strip()) for line in my_file.readlines()]

    adapters.sort()
    differences = []
    current = 0
    running = True
    while running:
        for jolt in range(current + 1, current + 4):
            if jolt in adapters:
                differences.append(jolt - current)
                current = jolt
                break

        if current >= adapters[-1]:
            running = False



    return differences.count(1) * (differences.count(3) + 1)


def part_two():
    with open("files/day10input.txt") as my_file:
        adapters = [int(line.strip()) for line in my_file.readlines()]

    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    paths = [0] * (max(adapters) + 1)
    paths[0] = 1

    for index in range(1, max(adapters) + 1):
        for x in range(1, 4):
            if (index - x) in adapters:
                paths[index] += paths[index - x]


    return paths[-1]


if __name__ == '__main__':
    print(part_two())
