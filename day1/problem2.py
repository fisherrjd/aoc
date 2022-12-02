# Day 1 for the December Advent of Code
import sys

data = open(sys.argv[1], "r").read()

values = data.split("\n")


most_calories = 0
current_total = 0


d = {}

counter = 0
for curr in values:
    print("Current Value: ", curr)
    if curr != "":
        current_total += int(curr)
    else:
        d[counter] = current_total
        current_total = 0
        counter += 1

d[counter] = current_total

sort = sorted(d.values(), reverse=True)

last = len(sort)

print(sum(sort[:3]))
