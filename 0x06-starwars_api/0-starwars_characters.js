#!/usr/bin/node

const request = require('request');
const printOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], (err, res, body) => {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    printOrder(actors, x + 1);
  });
};

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, res, body) => {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  printOrder(actors, 0);
});
