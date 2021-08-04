#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dictValues = Object.entries(dict);
const result = {};
dictValues.forEach(([key, value]) => {
  if (result[value] === undefined) {
    result[value] = [key];
  } else {
    result[value].push(key);
  }
});
console.log(result);
