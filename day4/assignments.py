#! /usr/bin/env python3

# turn the pairs in each line into arrays of numbers and see if one contains the other boolean response increments counter

with open("input.txt") as file:
        zones = [line.rstrip("\n").split(",") for line in file]

for z in zones:
    print(z)

