def get_groups():
    with open("files/day6input.txt") as my_file:
        lines = [line.strip() for line in my_file.readlines()]
    groups = []
    group = []
    for line in lines:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)

    if group:
        groups.append(group)

    return groups

def part_one():
    groups = get_groups()

    alfabet = "abcdefghijklmnopqrstuvwxyz"
    groups_score = []
    for group in groups:
        answer_dict = {c:False for c in alfabet}
        for person_answers in group:
            for answer in person_answers:
                if answer in answer_dict:
                    answer_dict[answer] = True
        score = [k for k, v in answer_dict.items() if v]
        groups_score.append(score)

    total = 0
    for score in groups_score:
        total += len(score)

    return total


def part_two():
    groups = get_groups()

    alfabet = "abcdefghijklmnopqrstuvwxyz"
    groups_score = []
    for group in groups:
        answer_dict = {c:True for c in alfabet}
        for person_answers in group:
            for character in answer_dict:
                if character not in person_answers:
                    answer_dict[character] = False
        score = [k for k, v in answer_dict.items() if v]
        groups_score.append(score)

    total = 0
    for score in groups_score:
        total += len(score)

    return total


if __name__ == "__main__":
    print(part_one())
    print(part_two())
