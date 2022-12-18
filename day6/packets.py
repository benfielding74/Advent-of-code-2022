#! /usr/bin/env python3

from collections import Counter

file = open("input.txt", "r").read() 

m = 0
ind = m+4
for i in file:
    x = file[m:ind]
    freq = Counter(x)
    if(len(freq) == len(x)):
            print(ind)
            break
    m+= 1
    ind+= 1

# part two
msg = 0
mark = msg+14
for i in file:
    x = file[msg:mark]
    freq = Counter(x)
    if(len(freq) == len(x)):
        print(mark)
        break
    msg+= 1
    mark+=1

