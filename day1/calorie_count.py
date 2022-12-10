#!/usr/bin/env python3

file = (open("input.txt", "r"))
arr = []
arr_total = []
total = 0

for line in file:
	if line == '\n':
		arr_total.append(total)
		total = 0
	else:
		total = total + int(line)	
		arr.append(int(line))

arr_total.append(total)
print(max(arr_total))

# part two for top 3

arr_total.sort(reverse=True)
top3 = 0
for num in range(0, 3):
    top3+= arr_total[num]

print(top3)

