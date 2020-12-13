import re
def part_one():
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    with open("files/day4input.txt") as my_file:
        lines = [line.replace("\n", "") for line in my_file.readlines()]
    passports = []
    passport = {}
    for line in lines:
        if line == "":
            if validate_passport(passport, required_fields):
                passports.append(passport)

            passport = {}
        else:
            attributes = line.split()
            for attribute in attributes:
                key_and_value = attribute.split(":")
                passport[key_and_value[0]] = key_and_value[1]

    return passports



def validate_passport(passport, required_fields):
    for field in required_fields:
        if field not in passport:
            return False

    return True


def is_in_range(number, min, max):
    return min <= number <= max


def validate_height(height):
    if re.match("\d+(cm|in)", height):
        number_and_suffix = [item for item in re.split("(cm|in)", height) if item]
        h = int(number_and_suffix[0])
        if "cm" in number_and_suffix:
            if not is_in_range(h, 150, 193):
                return False
        else:
            if not is_in_range(h, 59, 76):
                return False

    else:
        return False

    return True


def validate_hair_color(hair_color):
    if re.match("#([0-9]|[a-f]){6}", hair_color) and len(hair_color) == 7:
        return True
    else:
        return False


def validate_eye_color(eye_color):
    if re.match("amb|blu|brn|gry|grn|hzl|oth", eye_color) and len(eye_color) == 3:
        return True
    else:
        return False

def validate_passport_id(passport_id):
    if re.match("\d{9}", passport_id) and len(passport_id) == 9:
        return True
    else:
        return False




def part_two(passports):
    valid_passports = []
    for passport in passports:
        if not is_in_range(int(passport['byr']), 1920, 2002):
            continue

        if not is_in_range(int(passport['iyr']), 2010, 2020):
            continue

        if not is_in_range(int(passport['eyr']), 2020, 2030):
            continue

        if not validate_height(passport['hgt']):
            continue

        if not validate_hair_color(passport['hcl']):
            continue

        if not validate_eye_color(passport['ecl']):
            continue

        if not validate_passport_id(passport['pid']):
            continue

        valid_passports.append(passport)

    return valid_passports


if __name__ == "__main__":
    passports = part_one()
    print(len(passports))
    print(len(part_two(passports)))