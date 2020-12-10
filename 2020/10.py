file = open("10.txt")

adapters = []

OUTLET_JOLTAGE = 0

adapters.append(OUTLET_JOLTAGE)

for line in file:
    adapters.append(int(line))

adapters.sort()

adapters.append(adapters[len(adapters) - 1] + 3)

one = 0
three = 0

for index in range(0, len(adapters)):
    if index == len(adapters) - 1:
        break
    diff = adapters[index + 1] - adapters[index]
    if diff == 3:
        three += 1
    if diff == 1:
        one += 1

print("Part 1: ", one * three)

parallelPoints = {adapters[-1]: 1}

for index in range(len(adapters) - 2, -1, -1):
    nodeValue = 0
    node = adapters[index]

    maxPoint = node + 3
    targetIndex = 1

    while node + 3 >= adapters[index + targetIndex]:
        nodeValue += 1 * parallelPoints[adapters[index + targetIndex]]
        targetIndex += 1
        if (index + targetIndex) > len(adapters) - 1:
            break

    parallelPoints[node] = nodeValue

print("Part 2: ", parallelPoints[0])

