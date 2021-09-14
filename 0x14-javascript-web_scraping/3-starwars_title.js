#!/usr/bin/node
const request = require('request');
const idFilm = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + idFilm;

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
