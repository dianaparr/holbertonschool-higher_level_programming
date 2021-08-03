#!/usr/bin/node
const SquareC = require('./5-square');
class Square extends SquareC {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      const character = 'C';
      for (let i = 0; i < this.height; i++) {
        console.log(character.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
