#!/usr/bin/node
const paramTwo = process.argv[2];
const paramThree = process.argv[3];
if (!parseInt(paramTwo) || !parseInt(paramThree)) {
  console.log(0);
} else {
  let index = 0;
  const arr = [];
  const length = process.argv.length;
  for (let i = 2; i < length; i++) {
    arr[index++] = parseInt(process.argv[i]);
  }
  arr.sort(function (a, b) { return a - b; }); // Sort the numbers in ascending order
  console.log(arr[arr.length - 2]);
}
