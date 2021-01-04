import re


def setup():
    with open("files/day20input.txt") as my_file:
        lines = [line.strip() for line in my_file.readlines()]
    tiles = []
    tile = []
    for line in lines:
        if line:
            tile.append(line)
        else:
            tiles.append(tile)
            tile = []

    sides = []
    for tile in tiles:
        side = {
            "id": tile[0].replace("Tile ", "").replace(":", "").strip(),
            "up": tile[1], "down": tile[-1],
            "left": "".join([char[0] for index, char in enumerate(tile) if index != 0]),
            "right": "".join([char[-1] for index, char in enumerate(tile) if index != 0]),
            "full": [line for index, line in enumerate(tile) if index != 0],
            "rotation": 0,
            "flipped_horisontal": False,
            "flipped_vertical": False
        }
        side["full"] = remove_borders(side["full"])
        sides.append(side)

    return sides


def remove_borders(tile):
    return [line[1:-1] for i, line in enumerate(tile) if i != 0 and i != len(tile) - 1]


def test():
    sides = setup()
    tester = sides[0]
    print(tester["full"])
    tester["full"] = remove_borders(tester["full"])
    for row in tester["full"]:
        print(" ".join([c for c in row]))


def place(placed, new):
    placed_x, placed_y = placed["coord"]
    for i in range(4):
        if i == 1:
            flip_horisontal(new)
        elif i == 2:
            flip_vertical(new)
        elif i == 3:
            flip_horisontal(new)

        if piece_match(placed, new, "left", "right"):
            new["coord"] = (placed_x - 1, placed_y + 0)
            return new

        if piece_match(placed, new, "up", "down"):
            new["coord"] = (placed_x + 0, placed_y - 1)
            return new

        if piece_match(placed, new, "right", "left"):
            new["coord"] = (placed_x + 1, placed_y + 0)
            return new

        if piece_match(placed, new, "down", "up"):
            new["coord"] = (placed_x + 0, placed_y + 1)
            return new


def piece_match(placed, new, p_side="left", n_side="right"):
    for i in range(4):
        if placed[p_side] == new[n_side]:
            return True
        rotate(new, 1)

    return False


def rotate(tile, rotations):
    for _ in range(rotations):
        tile["rotation"] = (tile["rotation"] + 1) % 4
        temp_up = tile["up"]
        temp_right = tile["right"]
        temp_down = tile["down"]
        temp_left = tile["left"]

        tile["up"] = temp_left[::-1]
        tile["right"] = temp_up
        tile["down"] = temp_right[::-1]
        tile["left"] = temp_down

        tile["full"] = rotate_tile(tile["full"])


def rotate_tile(tile):
    new_tile = []
    for x in range(len(tile)):
        new_string = ""
        for y, row in enumerate(tile):
            new_string += row[x]
        new_tile.append(new_string[::-1])

    return new_tile


def flip_tile_horisontal(tile):
    return [t[::-1] for t in tile]


def flip_tile_vertical(tile):
    return tile[::-1]


def flip_horisontal(tile):
    tile["flipped_horisontal"] = not tile["flipped_horisontal"]
    temp = tile["left"]
    tile["left"] = tile["right"]
    tile["right"] = temp
    tile["up"] = tile["up"][::-1]
    tile["down"] = tile["down"][::-1]

    tile["full"] = flip_tile_horisontal(tile["full"])


def flip_vertical(tile):
    tile["flipped_vertical"] = not tile["flipped_vertical"]
    temp = tile["up"]
    tile["up"] = tile["down"]
    tile["down"] = temp
    tile["left"] = tile["left"][::-1]
    tile["right"] = tile["right"][::-1]

    tile["full"] = flip_tile_vertical(tile["full"])


def connect_tiles(sides):
    placed_tiles = []
    sides[0]["coord"] = (0, 0)
    tiles_to_check = [sides[0]]

    while tiles_to_check:
        ttc_ids = [tile["id"] for tile in tiles_to_check]
        connecting_tiles = []
        for tile in tiles_to_check:
            pt_ids = [tile['id'] for tile in placed_tiles]
            for side in sides:
                c_ids = [tile['id'] for tile in connecting_tiles]
                s_id = side['id']
                if s_id not in ttc_ids and s_id not in pt_ids and s_id not in c_ids:
                    found_tile = place(tile, side)
                    if found_tile:
                        connecting_tiles.append(found_tile)

            placed_tiles.append(tile)

        tiles_to_check = connecting_tiles

    return placed_tiles


def combine_tiles(tiles):
    columns = []
    rows = []
    for tile in tiles:
        if len(columns) + 1 > 12:
            rows.append(columns)
            columns = []

        columns.append(tile)

    if columns:
        rows.append(columns)

    return rows


def create_big_tile(rows):
    big_tile = []
    for row in rows:
        for i in range(len(row[0]["full"])):
            big_tile.append("".join([c["full"][i] for c in row]))

    return big_tile


def print_coords(rows):
    for row in rows:
        print(str(len(row)) + ": " + " ".join([str(c["coord"]) for c in row]))


def find_matches(rows):
    second = re.compile("(#....##....##....###)")
    third = re.compile("(.#..#..#..#..#..#...)")
    patterns = [second, third]
    matches = 0
    for y in range(len(rows) - 2):
        for x in range(18, len(rows[y]) - 1):
            if rows[y][x] == "#":
                first_x = x
                first_y = y
                match = True
                for i, p in enumerate(patterns):
                    test_row = rows[first_y + i]
                    start_x = first_x - 18
                    test_string = test_row[start_x:start_x + 20]
                    if not re.match(p, test_string):
                        match = False
                        break

                if match:
                    matches += 1

    return matches


def sum_sqrs(tile):
    return len([c for row in tile for c in row if c == "#"])


def main():
    sides = setup()
    placed_tiles = connect_tiles(sides)
    placed_tiles.sort(key=lambda t: (t["coord"][1], t["coord"][0]))
    rows = combine_tiles(placed_tiles)
    big_tile = create_big_tile(rows)
    sqrs_per_monster = 15
    matches = []
    for i in range(4):
        if i == 1:
            big_tile = flip_tile_horisontal(big_tile)
        elif i == 2:
            big_tile = flip_tile_vertical(big_tile)
        elif i == 3:
            big_tile = flip_tile_horisontal(big_tile)

        for _ in range(4):
            matches.append(find_matches(big_tile))
            big_tile = rotate_tile(big_tile)

    matches.sort(reverse=True)

    return sum_sqrs(big_tile) - (matches[0] * sqrs_per_monster)


if __name__ == '__main__':
    print(main())
