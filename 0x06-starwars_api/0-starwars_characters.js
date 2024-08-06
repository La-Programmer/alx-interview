#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;


async function getCharacters (url) {
  try {
    const response = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });
    const characters = JSON.parse(response).characters;
    return characters;
  } catch (error) {
    console.log(error);
  }
}


getCharacters(url)
.then(
  characters => {
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
  }
)