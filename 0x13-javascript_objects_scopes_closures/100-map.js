#!/usr/bin/node
const list = require('./100-data.js').list;
let index = 0;
const arrayMul = list.map(x => x * index++);
console.log(list);
console.log(arrayMul);
