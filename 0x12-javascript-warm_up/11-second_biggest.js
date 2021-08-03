#!/usr/bin/node
const paramTwo = process.argv[2];
const paramThree = process.argv[3];
if (!parseInt(paramTwo) || !parseInt(paramThree)) {
  console.log(0);
} else {
  const arr = [];
  arr.sort();
  const length = arr.length;
  for (let i = length - 2; i >= 0; i--) {
    if (arr[i] === arr[length - 1]) {
      console.log(arr[i]);
      return;
    }
  }
}
