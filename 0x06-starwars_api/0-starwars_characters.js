#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];
const url = `https://swapi-api.alx-tolls.com/api/films/${movie_id}`;

function getCharacters(url) {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log("Response: ", response.statusCode);
      console.log("Response body: ", body);
    }
  })
}

getCharacters(url);
