#!/usr/bin/env node

const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const res = JSON.parse(body);
  for (let i = 0; i < res.characters.length; i++) {
    const char = +res.characters[i].slice(37, -1);
    request.get(`https://swapi-api.hbtn.io/api/people/${char}`, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
