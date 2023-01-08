import sys
from os import path

from constants import *


def solve_challenge(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        score = calculate_score(lines)

        return score


def solve_second_challenge(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        score = calculate_guide_score(lines)

        return score


def calculate_score(lines):
    total_score = 0

    for line in lines:
        opposing_encoded_shape = line[0]
        my_encoded_shape = line[2]

        my_shape = get_shape_from_encoded(my_encoded_shape)
        opposing_shape = get_shape_from_encoded(opposing_encoded_shape)

        outcome = get_outcome(my_shape, opposing_shape)
        outcome_points = result_score_table[outcome]

        total_score += my_shape.POINTS
        total_score += outcome_points

    return total_score


def calculate_guide_score(lines):
    total_score = 0

    for line in lines:
        opposing_encoded_shape = line[0]
        encoded_round_result = line[2]

        opposing_shape = get_shape_from_encoded(opposing_encoded_shape)
        round_result = decode_round_result(encoded_round_result)
        my_shape = reverse_engineer_shape(opposing_shape, round_result)

        total_score += my_shape.POINTS
        total_score += result_score_table[round_result]

    return total_score


def get_shape_from_encoded(encoded_shape):
    decoded_shape = rps_dictionary[encoded_shape]

    if decoded_shape == ROCK:
        return Rock()

    if decoded_shape == PAPER:
        return Paper()

    if decoded_shape == SCISSORS:
        return Scissors()


def decode_round_result(encoded_result):
    return encoded_result_dictionary[encoded_result]


def reverse_engineer_shape(opposing_shape, desired_outcome):
    for shape in shape_class_list:
        my_shape = shape()

        outcome = get_outcome(my_shape, opposing_shape)

        if outcome == desired_outcome:
            return my_shape

    return None


def get_outcome(my_shape, opposing_shape):
    return my_shape.against(opposing_shape)


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
