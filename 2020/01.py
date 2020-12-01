from functools import reduce

file = open("01.txt")

nums = []

for line in file:
    nums.append(int(line))

numCount = len(nums)

# Part 1
partOne = []

for index in range(numCount - 1):
    numOne = nums[index]
    for indexOne in range(index + 1, numCount):
        numTwo = nums[indexOne]
        if numOne + numTwo == 2020:
            partOne = [numOne, numTwo]

print("Part 1", reduce((lambda x, y: x * y), partOne))


# Part 2
partTwo = []

for index in range(numCount - 2):
    numOne = nums[index]
    for indexOne in range(index + 1, numCount - 1):
        numTwo = nums[indexOne]
        for indexTwo in range(index + 2, numCount):
            numThree = nums[indexTwo]
            if numOne + numTwo + numThree == 2020:
                partTwo = [numOne, numTwo, numThree]

print("Part 2", reduce((lambda x, y: x * y), partTwo))
