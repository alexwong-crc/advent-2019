file = open("03.txt")

map = []

for line in file:
    map.append(line)

patternLength = len(map[0].strip())


def runDirection(right, down):
    treeCount = 0
    currentStep = 0
    for index in range(1, len(map)):
        if index % down == 0:
            currentStep += right
            if map[index][currentStep % patternLength] == "#":
                treeCount += 1
    return treeCount


print("Part 1: ", runDirection(3, 1))


directionRules = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

treeMultipleTotal = 1

for rule in directionRules:
    runTreeTotal = runDirection(rule[0], rule[1])
    treeMultipleTotal *= runTreeTotal

print("Part 2: ", treeMultipleTotal)
