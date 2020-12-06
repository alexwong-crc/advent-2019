file = open("06.txt")

surveys = []
group = {"count": 0, "response": []}

for line in file:
    if line == "\n":
        surveys.append(group)
        group = {"count": 0, "response": []}
    else:
        group["response"] += list(line.strip())
        group["count"] += 1

if bool(group):
    surveys.append(group)
    group = []

anyoneYes = 0
everyoneYes = 0

for survey in surveys:
    obj = {}
    for letter in survey["response"]:
        if letter in obj:
            obj[letter] += 1
        else:
            obj[letter] = 1
    anyoneYes += len(obj.keys())

    for response in obj:
        if obj[response] == survey["count"]:
            everyoneYes += 1

print("Part 1: ", anyoneYes)
print("Part 2: ", everyoneYes)
