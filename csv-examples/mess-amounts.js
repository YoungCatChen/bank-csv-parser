#!/usr/bin/env node
fs = require('fs');

fileNames = process.argv.slice();
fileNames.shift();
fileNames.shift();

REPLACE_NUMS = genNumberSequence();

for (var i = 0, fileName; fileName = fileNames[i]; ++i) {
  fs.readFile(fileName, 'utf8', processFile.bind(null, fileName));
}


function processFile(fileName, err, content) {
  if (err) {
    return console.log(err);
  }
  var newContent = content.replace(/\d+\.\d\d/g, function(match) {
    var result = match.replace(/\d/g, function(digit) {
      return REPLACE_NUMS[parseInt(digit, 10)];
    });
    return result;
  });
  console.log(newContent);
}

function genNumberSequence() {
  var pool = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  var result = [0];
  while (pool.length) {
    var index = Math.floor(pool.length * Math.random());
    var drawn = pool.splice(index, 1);
    result.push(drawn[0]);
  }
  return result;
}
