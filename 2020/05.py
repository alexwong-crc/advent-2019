import math

file = open("05.txt")

seats = []

for line in file:
    seats.append(line.strip())


def getSeatNum(letters, maxNum):
    seat = [0, maxNum]
    for letter in letters:
        half = math.ceil((seat[1] - seat[0]) / 2)
        if letter == "F" or letter == "L":
            seat[1] -= half
        else:
            seat[0] += half
    return seat[0]


highestSeat = 0

allSeatsById = {}
allSeats = []

for seat in seats:
    rowNum = getSeatNum(seat[:7], 127)
    colNum = getSeatNum(seat[-3:], 7)
    seatId = (rowNum * 8) + colNum
    allSeats.append(seatId)
    if seatId > highestSeat:
        highestSeat = seatId


allSeats.sort()
missingSeat = 0
for index in range(1, len(allSeats)):
    if allSeats[index - 1] + 1 != allSeats[index]:
        missingSeat = allSeats[index - 1] + 1


print("Part 1: ", highestSeat)
print("Part 2: ", missingSeat)
