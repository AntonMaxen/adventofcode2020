with open("files/day1input.txt") as my_file:
    content = [int(line) for line in my_file.readlines()]
wanted_sum = 2020
sum_correct = []
for x, x_line in enumerate(content):
    for y, y_line in enumerate(content):
        for z, z_line in enumerate(content):
            if x == y == z:
                continue

            if x_line + y_line + z_line == wanted_sum and sorted((x, y, z)) not in sum_correct:
                sum_correct.append(sorted((x, y, z)))

results = [content[my_tuple[0]] * content[my_tuple[1]] * content[my_tuple[2]]for my_tuple in sum_correct]
print(results[0])



