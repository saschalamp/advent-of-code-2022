from enum import Enum

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

opponent_map = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS
}

your_map = {
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS
}

def get_outcome_score(you, opponent):
    if you == opponent:
        return 3
    if you.value > opponent.value \
        and (you != Shape.SCISSORS or opponent != Shape.ROCK) \
        or (you == Shape.ROCK and opponent == Shape.SCISSORS):
        return 6
    return 0
    

def get_round_score(you, opponent):
    return get_outcome_score(you, opponent) + you.value

def get_total_score(games):
    total_score = 0
    for game in games:
        opponent = opponent_map[game[0]]
        you = your_map[game[2]]
        total_score += get_round_score(you, opponent)
    return total_score

expected_result_map = {
    "X": -1,
    "Y": 0,
    "Z": 1
}

def pick(opponent, expected_result):
    diff = expected_result_map[expected_result]
    normalized_opponent_value = opponent.value - 1
    normalized_value_to_pick = (normalized_opponent_value + diff) % 3
    value_to_pick = normalized_value_to_pick + 1
    return Shape(value_to_pick)

def get_total_score_2(games):
    total_score = 0
    for game in games:
        opponent = opponent_map[game[0]]
        you = pick(opponent, game[2])
        total_score += get_round_score(you, opponent)
    return total_score

if __name__ == "__main__":
    with open("input", "r") as f:
        print(get_total_score(f))
    with open("input", "r") as f:
        print(get_total_score_2(f))