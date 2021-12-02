const fs = require("fs");

const rawData = fs.readFileSync("./02.txt", "utf8");
const data = rawData.split("\n");
data.pop();

// Part 1
console.log("Part 1");
const instructionHandlerBasic = (instruction, [x, y]) => {
  let [direction, unit] = instruction.split(" ");
  unit = parseInt(unit);
  switch (direction) {
    case "up":
      return [x, y - unit];
    case "down":
      return [x, y + unit];
    case "forward":
      return [x + unit, y];
  }
};

let coords = [0, 0];

data.forEach((instruction) => {
  coords = instructionHandlerBasic(instruction, coords);
});

console.log("Answer is:", coords[0] * coords[1]);

// Part 2
console.log("\nPart 2");
const instructionHandlerAdvance = (instruction, [x, y], aim) => {
  let [direction, unit] = instruction.split(" ");
  unit = parseInt(unit);
  switch (direction) {
    case "up":
      return [[x, y], aim - unit];
    case "down":
      return [[x, y], aim + unit];
    case "forward":
      return [[x + unit, y + aim * unit], aim];
  }
};

coords = [0, 0];
let aim = 0;
data.forEach((instruction) => {
  [coords, aim] = instructionHandlerAdvance(instruction, coords, aim);
});

console.log("Answer is:", coords[0] * coords[1]);
