#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const idChar = 18;

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  } else {
    const dataJSON = (JSON.parse(body).results);
    let counter = 0;
    for (const film of dataJSON) {
      for (const character of film.characters) {
        if (character.includes(idChar)) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
