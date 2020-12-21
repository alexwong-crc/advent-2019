import time


file = open("13.txt")

timeOfArrival = 0
busIds = []

for line in file:
    line = line.strip()
    if line.find(",") != -1:
        busIds = line.split(",")
    else:
        timeOfArrival = int(line)

timetable = {}
bus = {"closestArrivalTime": False, "minsToWait": 0}

for id in busIds:
    if id == "x":
        continue
    id = int(id)
    minsPastArrival = timeOfArrival % id
    minsTillNextBus = id - minsPastArrival
    timeOfNextArrival = timeOfArrival + minsTillNextBus
    timetable[timeOfNextArrival] = id
    if bus["closestArrivalTime"] == False:
        bus["closestArrivalTime"] = timeOfNextArrival
        bus["minsToWait"] = minsTillNextBus
    elif timeOfNextArrival < bus["closestArrivalTime"]:
        bus["closestArrivalTime"] = timeOfNextArrival
        bus["minsToWait"] = minsTillNextBus

answer = timetable[bus["closestArrivalTime"]] * bus["minsToWait"]

print("Part 1: ", answer)


match = False

highestId = {"index": 0, "value": 0}

for index in range(0, len(busIds)):
    if busIds[index] == "x":
        continue
    if int(busIds[index]) > highestId["value"]:
        highestId["value"] = int(busIds[index])
        highestId["index"] = index

timestamp = highestId["value"] - highestId["index"]
interval = highestId["value"]

# while not match:
#     allMatch = True
#     for id in busIds:
#         if id == "x":
#             continue
#         modular = timestamp % int(id)
#         index = 0 if busIds.index(id) == 0 else int(id) - busIds.index(id)
#         if modular != index:
#             allMatch = False
#             break

#     if allMatch:
#         match = True
#     timestamp += interval

# timestamp = highestId["index"]

# while not match:
#     # help = {}
#     print(timestamp)
#     allMatch = True
#     for id in busIds:
#         if id == "x":
#             continue
#         modular = timestamp % int(id)
#         index = 0 if busIds.index(id) == 0 else int(id) - busIds.index(id)
#         # help[id] = modular
#         if modular != index:
#             allMatch = False
#             # break

#     if allMatch:
#         match = True
#     timestamp += 59
#     # print(help)


# print("Part 2: ", timestamp)

timestamp = 1068775

while True:
    arr = []
    for index in range(0, len(busIds)):
        if busIds[index] == "x":
            arr.append(busIds[index])
        else:
            arr.append(timestamp % int(busIds[index]))
    time.sleep(0.1)
    print(timestamp, arr)
    timestamp += 1

