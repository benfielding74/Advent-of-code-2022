#! /usr/bin/env python3

import re

# turn the pairs in each line into arrays of numbers and see if one contains the other boolean response increments counter

with open("input.txt") as file:
        zones = [line.rstrip("\n") for line in file]
#zones is an array of strings

# total for assignment pairs that contain each other
pairs = 0
overlap = 0

# I want to extract the numbers and pass into arrays so I can carry out a comparison
for z in zones:	
	arr = re.split("\W", z)
	a, b, c, d = arr
	zone1 = set(range(int(a),int(b)+1))
	zone2 = set(range(int(c), int(d)+1))
	if zone1.intersection(zone2):
		overlap+= 1

	if (zone1.issubset(zone2) or zone2.issubset(zone1)):
		pairs+= 1


print(pairs)
print(overlap)	
