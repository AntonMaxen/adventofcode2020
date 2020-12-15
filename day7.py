import re


def build_bag_dict():
    with open("files/day7input.txt") as my_file:
        rules = [rule.strip() for rule in my_file.readlines()]

    bag_dict = {}
    for rule in rules:
        bag, storage = rule.split("contain")
        bag = bag.replace("bags", "bag").replace("bag", "").strip()
        storages = storage.replace("bags", "bag").replace("bag", "").strip().split(",")
        bag_dict[bag] = {}
        for storage in storages:
            storage = storage.strip()

            match = re.match("([0-9])", storage, re.I)
            amount = int(match.group()) if match else 0

            words = re.split("\d+", storage)
            word = words[-1].replace(".", "").strip()
            if "no" not in word:
                bag_dict[bag][word] = amount

    return bag_dict

def part_one():
    bag_dict = build_bag_dict()

    final_parents = []
    wanted_words = ["shiny gold"]

    while wanted_words:
        found_parents = []
        for key in bag_dict.keys():
            for k, item in bag_dict[key].items():
                if k in wanted_words:
                    found_parents.append(key)

        wanted_words = found_parents.copy()
        final_parents.extend(found_parents)


    return len(set(final_parents))


def part_two():
    bag_dict = build_bag_dict()

    wanted_bags = ["shiny gold"]
    total_childs = 0
    while wanted_bags:
        found_childs = []
        for bag in wanted_bags:
            for k, v in bag_dict[bag].items():
                found_childs.extend([k for _ in range(v)])
                total_childs += v

        wanted_bags = found_childs.copy()

    return total_childs


if __name__ == '__main__':
    print(part_one())
    print(part_two())
