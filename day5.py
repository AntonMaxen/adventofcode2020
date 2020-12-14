import math
def part_one():
    with open("files/day5input.txt") as my_file:
        lines = [line.strip() for line in my_file.readlines()]


    row_ids = []
    for line in lines:
        min_row = 0
        max_row = 127
        min_column = 0
        max_column = 7

        for index, character in enumerate(line):
            if character == "F":
                max_row = max_row - math.ceil((max_row - min_row) / 2)
            elif character == "B":
                min_row = min_row + math.ceil((max_row - min_row) / 2)
            elif character == "R":
                min_column = min_column + math.ceil((max_column - min_column) / 2)
            elif character == "L":
                max_column = max_column - math.ceil((max_column - min_column) / 2)

            if index + 1 < len(line):
                if (character == "F" or character == "B"):
                    if line[index + 1] in ["R", "L"]:
                        row = min_row if character == "F" else max_row
            else:
                column = max_column if character == "R" else min_column

        row_id = row * 8 + column
        row_ids.append(row_id)

    row_ids.sort(reverse=True)
    return row_ids


if __name__ == "__main__":
    row_ids = part_one()
    for i in range(row_ids[-1], row_ids[0] + 1):
        if i not in row_ids:
            print(i)