# Day 1 for the December Advent of Code
import sys


most_calories = 0
current_total = 0

data = open(sys.argv[1], "r").read()

values = data.split("\n")

for curr in values:
    if curr != "":
        current_total += int(curr)
    else:
        current_total = 0

    if current_total > most_calories:
        most_calories = current_total

print(most_calories)
