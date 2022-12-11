#!/usr/bin/env python3

#part one
total = 0
badge_total = 0
#input is a file of 'rucksacks'
file = (open("input.txt", "r"))
#each line is a string which represents items in both of the compartments of the rucksack
#each string can be split exactly in half
for line in file:
    l = len(line)
    str1 = line[0:l//2]
    str2 = line[l//2:]

#find the common item in both halfs of the string
    char = ' '.join(list(set(str1)&set(str2)))
    
#lower case letters a-z have value 1-26
#upper case letters A-Z have value 27 - 52
#convert the common items using some sort of ascii conversion then adding to a total
#uppercase A is 65 lowercase a is 97
    if char.islower():
        total+=(ord(char) - 96)
    else:
        total+=(ord(char) - 38)

print(total)

#part two

#need to handle 3 lines at a time use the common item method and then carry out ascii conversion to add to total
with open("input.txt") as file:
    rucksacks = [line.rstrip("\n") for line in file]
    
# how to compare 3 arrays at a time. take first 3 then increment index and take next 3 etc

def badge_counter(a, b, c):
    '''method to find common characters and convert into numbers'''
    badge = ' '.join(list(set(a)&set(b)&set(c)))
    if badge.islower():
        num = (ord(badge) - 96)
    else:
        num = (ord(badge) - 38)
    return num

for ruck in range(0, len(rucksacks), 3):
    var = badge_counter(*rucksacks[ruck:ruck+3])
    badge_total += var

print(badge_total)

