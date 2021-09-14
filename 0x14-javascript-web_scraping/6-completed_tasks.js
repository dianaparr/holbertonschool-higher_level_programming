#!/usr/bin/node
const request = require("request");
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  } else {
    const dataJSON = JSON.parse(body);
    const newDict = {};
    for (const task of dataJSON) {
      if (task.completed === true) {
        newDict = newDict[task.userId];
        console.log(newDict);
      }
    }
  }
});
