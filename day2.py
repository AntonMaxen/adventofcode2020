def part_one(content):
    correct_password = []
    for line in content:
        d = split_string(line)

        amount_of_matches = len([c for c in d['password'] if c == d['character']])
        if d['min'] <= amount_of_matches <= d['max']:
            correct_password.append(d['password'])

    return len(correct_password)

def part_two(content):
    correct_passwords = []
    for line in content:
        password_correct = False
        d = split_string(line)
        min = d['min']
        max = d['max']
        character = d['character']
        password = d['password']
        if len(password) > min - 1 and len(password) > max - 1:
            if character == password[min - 1]:
                password_correct = not password_correct

            if character == password[max - 1]:
                password_correct = not password_correct

        if password_correct:
            correct_passwords.append(d['password'])

    return len(correct_passwords)




def split_string(line):
    sub_strings = line.split(" ")
    first = sub_strings[0].split("-")
    second = sub_strings[1].split(":")
    return {
        "min": int(first[0]),
        "max": int(first[1]),
        "character": second[0],
        "password": sub_strings[2]
    }


if __name__ == '__main__':
    with open("files/day2input.txt") as my_file:
        content = [line.replace("\n", "") for line in my_file.readlines()]

    print(part_two(content))
