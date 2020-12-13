import math

file = open("12.txt")


map = {
    "N": 0,
    "E": 1,
    "S": 2,
    "W": 3,
}

turn = {
    "L": -1,
    "R": 1,
}

coord = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
}

face = 1

for line in file:
    # Clean input
    command = line.strip()

    # Separate the command
    move = command[0]
    length = int(command[1:])

    # Deal with F
    if move == "F":
        coord[face] += length

    # Deal with Compass
    elif move in map:
        coord[map[move]] += length

    elif move in turn:
        newFace = face + (turn[move] * (length / 90))
        face = newFace % len(coord)


def calcManhattanDistance(coord):
    return abs(coord[0] - coord[2]) + abs(coord[1] - coord[3])


print("Part 1: ", calcManhattanDistance(coord))

file = open("12.txt")


waypoint = {0: 1, 1: 10, 2: 0, 3: 0}

coord = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
}


def moveWayPoint(waypoint):
    newWayPoint = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
    }
    ns = waypoint[0] - waypoint[2]
    ew = waypoint[1] - waypoint[3]

    if ns > 0:
        newWayPoint[0] = abs(ns)
    else:
        newWayPoint[2] = abs(ns)

    if ew > 0:
        newWayPoint[1] = abs(ew)
    else:
        newWayPoint[3] = abs(ew)

    return newWayPoint


def turnWayPoint(turn, waypoint):
    newWayPoint = {}
    for direction in waypoint:
        newDirection = math.trunc((direction + turn) % len(waypoint))
        newWayPoint[newDirection] = waypoint[direction]
    return newWayPoint


for line in file:
    # Clean input
    command = line.strip()

    # Separate the command
    move = command[0]
    length = int(command[1:])

    if move == "F":
        for direction in waypoint:
            coord[direction] += waypoint[direction] * length

    elif move in map:
        waypoint[map[move]] += length
        waypoint = moveWayPoint(waypoint)

    elif move in turn:
        waypoint = turnWayPoint(turn[move] * (length / 90), waypoint)


print("Part 2: ", calcManhattanDistance(coord))
