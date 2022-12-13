#!/usr/bin/env python3

import re

starting_stack = {
	1: ["J", "H", "P", "M", "S", "F", "N", "V"],
	2: ["S", "R", "L", "M", "J", "D", "Q"],
	3: ["N", "Q", "D", "H", "C", "S", "W", "B"],
	4: ["R", "S", "C", "L"],
	5: ["M", "V", "T", "P", "F", "B"],
	6: ["T", "R", "Q", "N", "C"],
	7: ["G", "V", "R"],
	8: ["C", "Z", "S", "P", "D", "L", "R"],
	9: ["D", "S", "J", "V", "G", "P", "B", "F"]
	}

test_stack = {
	1: ["Z", "N"],
	2: ["M", "C", "D"],
	3: ["P"]
	}

with open("test_input.txt") as file:
	process = [line.rstrip("\n") for line in file]

for l in process:
	arr = re.split("[a-zA-Z]", l)
	print(arr)


