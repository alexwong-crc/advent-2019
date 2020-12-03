file = open("02.txt")

db = []

for line in file:
    db.append(line.split())


def isPasswordCountValid(policy, letter, password):
    minOcc, maxOcc = policy.split("-")
    character = letter[0]
    occurrences = password.count(character)
    if occurrences >= int(minOcc) and occurrences <= int(maxOcc):
        return True
    return False


def isPasswordIndexValid(policy, letter, password):
    numOne, numTwo = policy.split("-")
    character = letter[0]

    indexOne = int(numOne) - 1
    indexTwo = int(numTwo) - 1

    isValid = False

    if indexOne <= len(password) and password[indexOne] == character:
        isValid = True

    if indexTwo <= len(password) and password[indexTwo] == character:
        isValid = True if isValid == False else False

    return isValid


passwordValidCount = 0
passwordValidIndex = 0

for row in db:
    policy, letter, password = row
    if isPasswordCountValid(policy, letter, password):
        passwordValidCount += 1
    if isPasswordIndexValid(policy, letter, password):
        passwordValidIndex += 1

print("Part 1: ", passwordValidCount)
print("Part 2: ", passwordValidIndex)

