#!/usr/bin/env node

const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
  const res = JSON.parse(body);
  let count = 0;
  const resArray = res.results;
  for (let i = 0; i < resArray.length; i++) {
    if ((resArray[i].characters.includes(wedge))) {
      count += 1;
    }
  }
  console.log(count);
});
