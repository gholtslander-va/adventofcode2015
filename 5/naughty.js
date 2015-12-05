var fs = require('fs');

// var advent5 = require('./advent5');
var advent5p2 = require('./advent5p2');

var fileContent = fs.readFileSync('./testinput.txt', { encoding: 'utf-8' });
var strings = fileContent.split('\n');

var niceStrings = 0;
for (var i = 0; i < strings.length; i++) {
  if (advent5p2.isNice(strings[i])) {
    niceStrings++;
  }
}

console.log('There were', niceStrings, 'nice strings');
