#!/usr/bin/env python3

my_score = 0
game_outcomes = {
        "X": {"A": 3, "B": 1, "C": 2},
        "Y": {"A": 1, "B": 2, "C": 3},
        "Z": {"A": 2, "B": 3, "C": 1}
        }

strategy_file = (open("input.txt", "r"))

for line in strategy_file:
    game = line.split()
    if len(game) < 2:
        pass
    elif game[1] == "X":
        score = game_outcomes["X"][game[0]]
        my_score+= score
    elif game[1] == "Y":
        score = game_outcomes["Y"][game[0]]
        my_score+= (3 + score)
    elif game[1] == "Z":
        score = game_outcomes["Z"][game[0]]
        my_score+= (6 + score)

print(my_score)

