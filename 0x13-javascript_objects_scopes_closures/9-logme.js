#!/usr/bin/node
let posItem = 0;
exports.logMe = function (item) {
  console.log(`${posItem}: ${item}`);
  posItem += 1;
};
