ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

LOSS = 'loss'
DRAW = 'draw'
WIN = 'win'

rps_dictionary = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS
}

encoded_result_dictionary = {
    'X': LOSS,
    'Y': DRAW,
    'Z': WIN
}

result_score_table = {
    LOSS: 0,
    DRAW: 3,
    WIN: 6
}


class Rock:
    POINTS = 1

    def against(self, shape):
        if isinstance(shape, Rock):
            return DRAW

        if isinstance(shape, Paper):
            return LOSS

        if isinstance(shape, Scissors):
            return WIN


    def __init__(self):
        self.points = 1

    def __str__(self):
        return ROCK
            

class Paper:
    POINTS = 2

    def against(self, shape):
        if isinstance(shape, Rock):
            return WIN

        if isinstance(shape, Paper):
            return DRAW

        if isinstance(shape, Scissors):
            return LOSS


    def __init__(self):
        self.points = 2

    def __str__(self):
        return PAPER


class Scissors:
    POINTS = 3

    def against(self, shape):
        if isinstance(shape, Rock):
            return LOSS

        if isinstance(shape, Paper):
            return WIN

        if isinstance(shape, Scissors):
            return DRAW


    def __init__(self):
        self.points = 3

    def __str__(self):
        return SCISSORS


shape_class_list = [Rock, Paper, Scissors]
