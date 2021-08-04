#!/usr/bin/node
// const path = process.argv;
const file = require('fs');
file.readFile(process.argv[2], 'utf8', function (error1, dataOne) {
  file.readFile(process.argv[3], 'utf8', function (error2, dataTwo) {
    const concatData = dataOne + dataTwo;
    file.writeFile(process.argv[4], concatData, function () {});
  });
});
