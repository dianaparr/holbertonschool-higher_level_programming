#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  // display the status code. Alternativa: http module [http.STATUS_CODES]
  console.log('code:', response.statusCode);
});
