def part_one(lines, x_move=3, y_move=1, filename="newlines.txt"):
    x = 0
    y = 0
    trees = 0
    with open(f"files/{filename}", mode="w") as my_file:
        my_file.write(lines[0])
        my_file.write("\n")

    while y + y_move < len(lines):
        for z in range(y + 1, y+y_move):
            with open(f"files/{filename}", mode="a") as my_file:
                my_file.write(lines[z])
                my_file.write("\n")

        y += y_move
        line = lines[y]
        if x + x_move > len(line) - 1:
            x = x - len(line)
        x += x_move
        character = line[x]
        new_line = [c for c in line]
        if character == "#":
            trees += 1
            new_line[x] = "X"
        else:
            new_line[x] = "O"

        with open(f"files/{filename}", mode="a") as my_file:
            my_file.write("".join(new_line))
            my_file.write("\n")

    for z in range(y + 1, len(lines)):
        with open(f"files/{filename}", mode="a") as my_file:
            my_file.write(lines[z])
            my_file.write("\n")

    return trees

if __name__ == "__main__":
    with open("files/day3input.txt") as my_file:
        lines = [line.replace("\n", "") for line in my_file.readlines()]

    res11 = part_one(lines, x_move=1, y_move=1, filename="11.txt")
    res31 = part_one(lines, x_move=3, y_move=1, filename="31.txt")
    res51 = part_one(lines, x_move=5, y_move=1, filename="51.txt")
    res71 = part_one(lines, x_move=7, y_move=1, filename="71.txt")
    res12 = part_one(lines, x_move=1, y_move=2, filename="12.txt")
    res110 = part_one(lines, x_move=1, y_move=10, filename="110.txt")

    print(res11 * res31 * res51 * res71 * res12)