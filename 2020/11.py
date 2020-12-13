file = open("11.txt")

arrangement = []

for line in file:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    arrangement.append(row)


def applyRuleOne(map, seatNumber):
    row, col = seatNumber
    rowRange = [row - 1, row, row + 1]
    colRange = [col - 1, col, col + 1]

    # If current space is not a seat, return as is
    if map[row][col] == ".":
        return "."

    # Get all co-ordinates of surrounding seats
    indexes = []
    for rowIndex in rowRange:
        # Check row range is within map
        if rowIndex >= 0 and rowIndex < len(map):
            for colIndex in colRange:
                # Check col range is within map
                if colIndex >= 0 and colIndex < len(map[0]):
                    # Remove co-ordinate of current seat
                    if seatNumber != [rowIndex, colIndex]:
                        indexes.append([rowIndex, colIndex])

    occupied = 0
    # Check all co-ordinates for occupied seats
    for index in indexes:
        rowIndex, colIndex = index
        if map[rowIndex][colIndex] == "#":
            occupied += 1

    # Apply the logic
    if map[row][col] == "L" and occupied == 0:
        return "#"
    elif map[row][col] == "#" and occupied >= 4:
        return "L"
    else:
        return map[row][col]


def totalOccupiedSeatOfFinalMap(map, rule):
    newMap = []
    occupied = 0
    same = True
    for rowIndex in range(0, len(map)):
        newRow = []
        for colIndex in range(0, len(map[rowIndex])):
            oldSeat = map[rowIndex][colIndex]
            newSeat = rule(map, [rowIndex, colIndex])
            # Create the new seats for the new row
            newRow.append(newSeat)

            # If the new seat does not match the old one, we know the new map is different
            if oldSeat != newSeat:
                same = False

            # If the map hasn't changed, add up all the occupied seats
            if same and newSeat == "#":
                occupied += 1
        # Add the new row ot the new map
        newMap.append(newRow)

    # Loop if the map is different
    if not same:
        return totalOccupiedSeatOfFinalMap(newMap, rule)
    else:
        return occupied


totalOccupiedSeats = totalOccupiedSeatOfFinalMap(arrangement, applyRuleOne)

print("Part 1: ", totalOccupiedSeats)


def applyRuleTwo(map, seatNumber):
    row, col = seatNumber
    visibleSeats = {}
    direction = {
        "n": [-1, 0],
        "ne": [-1, 1],
        "e": [0, 1],
        "se": [1, 1],
        "s": [1, 0],
        "sw": [1, -1],
        "w": [0, -1],
        "nw": [-1, -1],
    }

    for xy in direction:
        seatX, seatY = [row, col]
        x, y = direction[xy]
        seatX += x
        seatY += y
        while 0 <= seatX < len(map) and 0 <= seatY < len(map[x]):
            if map[seatX][seatY] != ".":
                visibleSeats[xy] = map[seatX][seatY]
                break
            else:
                seatX = seatX + x
                seatY = seatY + y

    occupied = 0
    for seat in visibleSeats:
        if visibleSeats[seat] == "#":
            occupied += 1

    # Apply the logic
    if map[row][col] == "L" and occupied == 0:
        return "#"
    elif map[row][col] == "#" and occupied >= 5:
        return "L"
    else:
        return map[row][col]


totalOccupiedSeats = totalOccupiedSeatOfFinalMap(arrangement, applyRuleTwo)

print("Part 2: ", totalOccupiedSeats)

