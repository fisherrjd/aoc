import sys

data = open(sys.argv[1], "r").read()

shapes = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

# Get a list of every turn
turns = [[shapes[shape] for shape in turn.split(" ")] for turn in data.split("\n")[:-1]]


# Part 1
total = 0
for turn in turns:
    first = turn[1]
    second = turn[0]

    # Win
    if (
        (first == 2 and second == 1)
        or (first == 3 and second == 2)
        or (first == 1 and second == 3)
    ):
        total += 6

    # Draw
    elif first == second:
        total += 3

    # Loose
    else:
        total += 0
        # Yes I know it's useless

    total += first

print(f"Part 1 : {total}")


# Part 2
win = {1: 2, 2: 3, 3: 1}
draw = {1: 1, 2: 2, 3: 3}
loose = {1: 3, 2: 1, 3: 2}

total = 0
for turn in turns:
    second = turn[0]
    end = turn[1]

    # first looses
    if end == 1:
        total += loose[second]
        total += 0

    # draw
    if end == 2:
        total += draw[second]
        total += 3

    # first win
    if end == 3:
        total += win[second]
        total += 6

print(f"Part 2 : {total}")
