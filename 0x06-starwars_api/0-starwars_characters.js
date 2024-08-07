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
    // console.log(characters);
    return characters;
  } catch (error) {
    console.log(error);
  }
}

async function getCharacter (endpoint) {
  try {
    const response = await new Promise((resolve, reject) => {
      request(endpoint, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });
    const name = JSON.parse(response).name;
    console.log(name);
  } catch (error) {
    console.log(error);
  }
}

const reduceApiEndpoints = async (previous, endpoint) => {
  await previous;
  return getCharacter(endpoint);
};

getCharacters(url)
  .then(characters => {
    // console.log(characters)
    characters.reduce(reduceApiEndpoints, Promise.resolve());
  });
