import sys

# a-z  priority  1-26
# A-Z  priority  27-52

# part 1

data = open(sys.argv[1], "r").read()
# groups = data.split("\n\n")
# values = [list(map(str, x.strip().split("\n"))) for x in data.split("\n\n")]
values = [x for x in data.strip().split("\n")]

total = 0
for n in values:
    mid = int(len(n) / 2)
    compartment1 = n[0:mid]
    compartment2 = n[mid : len(n)]

    current_item = set(compartment1) & set(compartment2)
    item = current_item.pop()

    if item.islower():
        total += ord(item) - ord("a") + 1
    else:
        total += ord(item) - ord("A") + 27

print(total)

# part 2

values = [x for x in data.strip().split("\n")]

grouping = 3

for i in range(0, len(values), grouping):
    print(values[i : i + grouping])
    commen_item = set(values[i : i + grouping])
    print(commen_item)
