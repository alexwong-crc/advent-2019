file = open("08.txt")

instructions = []

for line in file:
    line = line.strip()
    instructions.append(line)

acc = 0
ranLines = []
index = 0

while index < len(instructions):
    if index in ranLines:
        break

    ranLines.append(index)
    type, count = instructions[index].split(" ")

    if type == "jmp":
        index += int(count)
    elif type == "acc":
        acc += int(count)
        index += 1
    elif type == "nop":
        index += 1

print("Part 1: ", acc)


def isLooped(initialIndex, newInstructions):
    index = initialIndex
    linesDone = []
    remainingAcc = 0
    isLoop = False
    while index < len(newInstructions):
        if index in linesDone:
            isLoop = True
            break
        linesDone.append(index)
        type, count = newInstructions[index].split(" ")
        if type == "jmp":
            index += int(count)
        elif type == "acc":
            remainingAcc += int(count)
            index += 1
        elif type == "nop":
            index += 1
    return isLoop if isLoop else remainingAcc


acc = 0
index = 0


while index < len(instructions):
    print(index)
    type, count = instructions[index].split(" ")

    if type == "acc":
        acc += int(count)
        index += 1
    else:
        if type == "jmp":
            newType = "nop"
        else:
            newType = "jmp"

        newInstructions = [*instructions]
        newInstructions[index] = f"{newType} {count}"
        loop = isLooped(index, newInstructions)
        if loop != True:
            acc += loop
            break
        elif type == "jmp":
            index += int(count)
        else:
            index += 1


print("Part 2: ", acc)
