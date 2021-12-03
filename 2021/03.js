const fs = require("fs");

const rawData = fs.readFileSync("./03.txt", "utf8");
const data = rawData.split("\n");
data.pop();

const convertBinaryToDigit = (binary) => {
  return String(binary)
    .split("")
    .reverse()
    .reduce((acc, digit, index) => {
      return acc + Number(digit) * 2 ** index;
    }, 0);
};

const binarySum = [];
const totalBinaries = data.length;

data.forEach((binary) => {
  for (let index in binary) {
    const digit = binary[index];

    binarySum[index] =
      binarySum[index] !== undefined
        ? binarySum[index] + Number(digit)
        : Number(digit);
  }
});

let gamma = "";
let epsilon = "";

binarySum.forEach((binary) => {
  if (binary > totalBinaries / 2) {
    gamma += "1";
    epsilon += "0";
  } else {
    gamma += "0";
    epsilon += "1";
  }
}, "");

console.log("Part 1");
console.log(
  "Answer: ",
  convertBinaryToDigit(gamma) * convertBinaryToDigit(epsilon)
);

console.log("\nPart 2");
const getFinalBinary = (binaryCollection, index, type) => {
  if (binaryCollection.length === 1) return binaryCollection[0];

  const oneTotal = [];
  const zeroTotal = [];
  binaryCollection.forEach((binary) => {
    if (binary[index] == 1) {
      oneTotal.push(binary);
    } else {
      zeroTotal.push(binary);
    }
  });

  if (type === "oxygen") {
    if (oneTotal.length >= zeroTotal.length) {
      return getFinalBinary(oneTotal, index + 1, type);
    } else {
      return getFinalBinary(zeroTotal, index + 1, type);
    }
  } else {
    if (zeroTotal.length <= oneTotal.length) {
      return getFinalBinary(zeroTotal, index + 1, type);
    } else {
      return getFinalBinary(oneTotal, index + 1, type);
    }
  }
};

const oxygenRating = getFinalBinary(data, 0, "oxygen");
const co2Rating = getFinalBinary(data, 0, "co2");

console.log(
  "Answer: ",
  convertBinaryToDigit(oxygenRating) * convertBinaryToDigit(co2Rating)
);
