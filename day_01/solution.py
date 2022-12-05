import sys
from os import path

TOP_N_ELVES = 3


def solve_challenge(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        total_calories = convert_to_calories_by_elf(lines)
        max_calories = max(total_calories)

        return max_calories

def solve_second_challenge(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        total_calories = convert_to_calories_by_elf(lines)
        total_calories.sort(reverse=True)
        calories_sum = get_sum_of_top_elves(total_calories)

        return calories_sum


def convert_to_calories_by_elf(lines):
    total_calories = []
    single_elf_calories = 0

    for line in lines:
        if line.strip() == '':
            total_calories.append(single_elf_calories)
            single_elf_calories = 0
        else:
            single_elf_calories += int(line)
        
    total_calories.append(single_elf_calories)

    return total_calories


def get_sum_of_top_elves(sorted_calories):
    top_elves = sorted_calories[:TOP_N_ELVES]
    calories_sum = sum(top_elves)

    return calories_sum


if __name__ == '__main__':
    filename = sys.argv[2]
    file_path = path.abspath(__file__)
    dir_path = path.dirname(file_path)
    full_file_path = path.join(dir_path, filename)

    challenge_part = int(sys.argv[1])

    result = None

    if challenge_part == 1:
        result = solve_challenge(full_file_path)
    elif challenge_part == 2:
        result = solve_second_challenge(full_file_path)

    print(result)
