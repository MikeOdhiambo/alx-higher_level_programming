#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, res, body) {
  const tasks = {};
  const total = JSON.parse(body);
  if (res.statusCode === 200) {
    for (let i = 0; i < total.length; i++) {
      if (total[i].completed) {
        if ((total[i].userId in tasks)) {
          tasks[total[i].userId] += 1;
        } else {
          tasks[total[i].userId] = 1;
        }
      }
    }
    console.log(tasks);
  } else if (err) {
    console.log(err);
  }
});
