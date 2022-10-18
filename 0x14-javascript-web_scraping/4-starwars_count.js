#!/usr/bin/env node

const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/`, function (error, response, body) {
  if (error) {
    console.log(error);
  };
  const wedge = "https://swapi-api.hbtn.io/api/people/18/";
  const res = JSON.parse(body);
  let count = 0
  const resArray = res["results"];
  //console.log(resArray[0]);
  for (let i = 0; i < resArray.length; i++) {
	  //console.log(resArray[i]["characters"]);
	  if ((resArray[i]["characters"].includes(wedge))) {
		  count += 1
	  }
  };
  console.log(count);
});
