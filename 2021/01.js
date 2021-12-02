const fs = require("fs");

const rawData = fs.readFileSync("./01.txt", "utf8");

// Part 1
console.log("Part 1");
const data = rawData.split("\n").map((num) => parseInt(num));
data.pop();

let result = 0;

data.forEach((num, index, arr) => {
  if (num && arr[index - 1] && num > arr[index - 1]) result += 1;
});

console.log("The answer is:", result);

// Part 2
console.log("\nPart 2");
let result2 = 0;
data.forEach((num, index, arr) => {
  if (index < 3) return;
  let set1 = arr[index - 3] + arr[index - 2] + arr[index - 1];
  let set2 = arr[index - 2] + arr[index - 1] + num;
  if (set2 > set1) result2 += 1;
});

console.log("The answer is:", result2);
