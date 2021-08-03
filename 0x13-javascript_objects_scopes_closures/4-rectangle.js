#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { // if w or h is a positive integer create a object
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const character = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }

  rotate () {
    const forChange = this.height;
    this.height = this.width;
    this.width = forChange;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
