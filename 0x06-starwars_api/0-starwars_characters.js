#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const characters = getCharacters(url);

for (const character in characters) {
  request(character, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const responseBody = JSON.parse(body);
      const characterName = responseBody.name;
      console.log(characterName);
    }
  });
}

function getCharacters (url) {
  try {
    const response = request(url, (error, response, body) => {
      if (error) {
        console.log(error);
        return error;
      } else {
        return body;
      }
    });
    const characters = JSON.parse(response).characters;
    return characters;
  } catch (error) {
    console.log(error);
  }
}
