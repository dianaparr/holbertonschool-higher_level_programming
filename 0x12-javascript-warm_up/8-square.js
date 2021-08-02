#!/usr/bin/node
const params = process.argv[2];
const character = 'X';
if (parseInt(params)) {
  for (let i = 0; i < params; i++) {
    console.log(character.repeat(params));
  }
} else {
  console.log('Missing size');
}
