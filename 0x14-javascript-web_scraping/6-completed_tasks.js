#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  } else {
    const dataJSON = JSON.parse(body);
    const newDict = {};
    for (const task of dataJSON) {
      const taskCompleted = task.completed;
      const emploId = task.userId;
      // if taskCompleted is true
      if (taskCompleted === true) {
        // if emploId exists, sum one more (loop), the otherwise put one (first thing to do)
        if (newDict[emploId]) {
          newDict[emploId] += 1;
        } else {
          newDict[emploId] = 1;
        }
      }
    }
    console.log(newDict);
  }
});
