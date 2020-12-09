import re

file = open("07.txt")

bagRules = {}

for line in file:
    line = line.strip()
    mainBagRegex = re.compile("\w+\s*\w+(?=\sbag)")
    otherBagsRegex = re.compile("(\d)\s(\w+\s*\w+)(?=\sbag)")
    mainBag = mainBagRegex.match(line)
    otherBags = otherBagsRegex.findall(line)
    if mainBag:
        bags = []
        for bag in otherBags:
            bags.append({"colour": bag[1], "count": int(bag[0])})
        bagRules[mainBag.group()] = bags

MY_BAG = "shiny gold"

total = 0

ruleApplied = []
bagCount = []


def bagLookup(bags):
    global total
    if len(bags) > 1:
        currentBag, *others = bags
    else:
        currentBag = bags[0]
        others = []

    for mainBag in bagRules:
        if mainBag not in ruleApplied:
            for bag in bagRules[mainBag]:
                if currentBag in bag["colour"]:
                    total += 1
                    others.append(mainBag)
                    ruleApplied.append(mainBag)
    if len(others) > 0:
        bagLookup(others)


bagLookup([MY_BAG])

print("Part 1: ", total)


totalBags = 1


class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.colour = ""


# root = Tree(1)
# root.children.append(Tree(1))
# root.children.append(Tree(2))
# root.children[0].children.append(Tree(3))
# root.children[0].children.append(Tree(4))
# root.children[1].children.append(Tree(5))
# root.children[1].children.append(Tree(6))


def createTree(tree, bag):
    tree.colour = bag
    for rule in bagRules[bag]:
        newTree = Tree(rule["count"])
        tree.children.append(newTree)
        createTree(newTree, rule["colour"])


root = Tree(1)

createTree(root, MY_BAG)


answer = 0
subTotal = 0


def getTree(tree):
    print(tree.colour)
    for branch in tree.children:
        getTree(branch)


getTree(root)

print("Part 2: ", answer)

