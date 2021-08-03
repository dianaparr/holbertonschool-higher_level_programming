#!/usr/bin/node
// Function prototype method call()
exports.addMeMaybe = function (number, theFunction) {
  theFunction.call(this, ++number); // prefix increment
};
