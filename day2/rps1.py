#!/usr/bin/env python3

my_score = 0
game_outcomes = {
        "X": {"A": 3, "B": 0, "C": 6},
        "Y": {"A": 6, "B": 3, "C": 0},
        "Z": {"A": 0, "B": 6, "C": 3}
        }

weapon_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
        }

strategy_file = (open("input.txt", "r"))

for line in strategy_file:
    game = line.split()
    if len(game) < 2:
        pass
    else:
        my_score+= (game_outcomes[game[1]][game[0]] + weapon_scores[game[1]])

print(my_score)

