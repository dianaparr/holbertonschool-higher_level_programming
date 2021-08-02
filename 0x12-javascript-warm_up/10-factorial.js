#!/usr/bin/node
function isFactorial (num) {
  if (!num) { // if num is equal to zero
    return (1);
  } else {
    return (num * isFactorial(num - 1));
  }
}
console.log(isFactorial(process.argv[2]));
