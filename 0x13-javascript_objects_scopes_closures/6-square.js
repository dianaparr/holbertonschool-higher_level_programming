#!/usr/bin/node
const Square = require('./5-square');
class SquareC extends Square {
  charPrint(c) {
    if (c === undefined) {
      this.print();
    }
    else {
      const character = 'C';
      for (let i = 0; i < this.height; i++) {
          console.log(character.repeat(this.width));
      }
    }
  }
}
module.exports = SquareC;
