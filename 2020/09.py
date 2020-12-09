file = open("09.txt")

PREAMBLE = 25

numbers = []

for line in file:
    line = line.strip()
    numbers.append(int(line))


def canSumToTarget(set, target):
    canSum = False
    for index in range(0, len(set)):
        if index == len(set) - 1:
            break
        for subIndex in range(index + 1, len(set)):
            if set[index] + set[subIndex] == target:
                canSum = True
    return canSum


suspect = 0

for index in range(0, len(numbers)):
    preambleRange = numbers[index : index + PREAMBLE]
    target = numbers[index + PREAMBLE]
    if not canSumToTarget(preambleRange, target):
        suspect = target
        break

print("Part 1: ", suspect)

answer = 0
contiguousBoundary = ()

for index in range(0, len(numbers)):
    sum = numbers[index]
    for subIndex in range(index + 1, len(numbers)):
        sum += numbers[subIndex]
        if sum == suspect:
            contiguousBoundary = (index, subIndex)
        elif sum > suspect:
            break

contiguousSet = []

for index in range(contiguousBoundary[0], contiguousBoundary[1] + 1):
    contiguousSet.append(numbers[index])

contiguousSet.sort()

answer = contiguousSet[0] + contiguousSet[len(contiguousSet) - 1]

print("Part 2: ", answer)

