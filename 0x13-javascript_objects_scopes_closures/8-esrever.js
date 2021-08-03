#!/usr/bin/node
// use of the array push method
exports.esrever = function (list) {
  const length = list.length;
  const arrayReverse = [];
  for (let i = length - 1; i >= 0; i--) { // loop traversing array in reverse
    arrayReverse.push(list[i]);
  }
  return arrayReverse;
};
