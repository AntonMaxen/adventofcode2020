def get_rows():
    with open(f'files/day11input.txt') as my_file:
        rows = [line.strip() for line in my_file.readlines()]

    return rows


def check_around(rows, start_y, start_x):
    result_dict = {}
    for y in range(-1, 2):
        for x in range(-1, 2):
            y_coord = start_y + y
            x_coord = start_x + x

            if not 0 <= y_coord < len(rows):
                continue

            if not 0 <= x_coord < len(rows[y_coord]):
                continue

            if start_y == y_coord and start_x == x_coord:
                continue

            symbol = rows[start_y + y][start_x + x]
            if symbol in result_dict:
                result_dict[symbol] += 1
            else:
                result_dict[symbol] = 1

    return result_dict


def determine_symbol(current_symbol, result_dict):
    change = False
    if current_symbol == 'L':
        if '#' not in result_dict:
            current_symbol = '#'
            change = True
    elif current_symbol == '#':
        if '#' in result_dict and result_dict['#'] >= 4:
            current_symbol = 'L'
            change = True

    return current_symbol, change


def part_one():
    rows = get_rows()

    active = True
    while active:
        active = False
        new_rows = []
        for y in range(len(rows)):
            new_row = ""
            for x in range(len(rows[y])):
                result_dict = check_around(rows, y, x)
                current_symbol = rows[y][x]
                current_symbol, change = determine_symbol(
                    current_symbol,
                    result_dict
                )
                if change:
                    active = True
                new_row += current_symbol
            new_rows.append(new_row)

        rows = new_rows

    return len([sym for row in rows for sym in row if sym == '#'])


if __name__ == '__main__':
    one = part_one()
    print(one)


