import re

file = open("04.txt")

passports = []

passport = {}

for line in file:
    if line == "\n":
        passports.append(passport)
        passport = {}
    else:
        line = line.strip().split(" ")
        for field in line:
            prop, val = field.split(":")
            passport[prop] = val

if bool(passport):
    passports.append(passport)

withValidKeys = 0
withValidKeyFields = 0
requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
schema = {
    "byr": {"type": "int", "min": 1920, "max": 2002},
    "iyr": {"type": "int", "min": 2010, "max": 2020},
    "eyr": {"type": "int", "min": 2020, "max": 2030},
    "hgt": {
        "type": "metric",
        "cm": {"min": 150, "max": 193},
        "in": {"min": 59, "max": 76},
    },
    "hcl": {"type": "hex"},
    "ecl": {
        "type": "enum",
        "options": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    },
    "pid": {"type": "string", "length": 9},
    "cid": {"type": "pass"},
}

for doc in passports:
    hasValidKeys = True
    for key in requiredKeys:
        if key not in doc:
            hasValidKeys = False
    if hasValidKeys:
        withValidKeys += 1
        hasValidFields = True
        for key in doc:
            if schema[key]["type"] == "int":
                value = int(doc[key])
                if value < schema[key]["min"] or value > schema[key]["max"]:
                    hasValidFields = False

            if schema[key]["type"] == "metric":
                metric = doc[key][-2:]
                if metric in schema[key]:
                    value = int(doc[key][:-2])
                    if (
                        value < schema[key][metric]["min"]
                        or value > schema[key][metric]["max"]
                    ):
                        hasValidFields = False
                else:
                    hasValidFields = False

            if schema[key]["type"] == "hex":
                regex = re.compile("^#[0-9a-f]{6}$")
                value = doc[key]
                if not regex.match(value):
                    hasValidFields = False

            if schema[key]["type"] == "enum":
                if doc[key] not in schema[key]["options"]:
                    hasValidFields = False

            if schema[key]["type"] == "string":
                regex = re.compile("^[0-9]{9}$")
                if not regex.match(doc[key]):
                    hasValidFields = False

        if hasValidFields:
            withValidKeyFields += 1

print("Part 1: ", withValidKeys)
print("Part 2: ", withValidKeyFields)
