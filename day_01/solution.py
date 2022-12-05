import sys
from os import path


def solve_challenge(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        total_calories = convert_to_calories_by_elf(lines)
        max_calories = max(total_calories)

        return max_calories


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


if __name__ == '__main__':
    filename = sys.argv[1]
    file_path = path.abspath(__file__)
    dir_path = path.dirname(file_path)
    full_file_path = path.join(dir_path, filename)

    result = solve_challenge(full_file_path)
    print(result)
