#!/usr/bin/node
const params = process.argv[2];
if (parseInt(params)) {
  for (let i = 0; i < params; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
