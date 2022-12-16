#!/usr/bin/env python3

starting_stack = {
	"1": ["J", "H", "P", "M", "S", "F", "N", "V"],
	"2": ["S", "R", "L", "M", "J", "D", "Q"],
	"3": ["N", "Q", "D", "H", "C", "S", "W", "B"],
	"4": ["R", "S", "C", "L"],
	"5": ["M", "V", "T", "P", "F", "B"],
	"6": ["T", "R", "Q", "N", "C"],
	"7": ["G", "V", "R"],
	"8": ["C", "Z", "S", "P", "D", "L", "R"],
	"9": ["D", "S", "J", "V", "G", "P", "B", "F"]
	}

test_stack = {
	"1": ["Z", "N"],
	"2": ["M", "C", "D"],
	"3": ["P"]
	}

with open("input.txt") as file:
	process = [line.rstrip("\n") for line in file]

for l in process:
    move_arr = []
    arr = l.split(' ')
    for i in arr:
        if i.isdigit():
            move_arr.append(i)
    move, fr, to = move_arr
    # move times take an element from key fr to key to
    for crane in range(int(move)):
        crate = starting_stack[fr][-1]
        starting_stack[fr].pop()
        starting_stack[to].append(crate)
print(starting_stack)
