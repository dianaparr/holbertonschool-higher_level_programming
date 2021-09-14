#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    return console.error(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', err => {
      if (err) {
        return console.error(err);
      }
    });
  }
});
