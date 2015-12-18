var fs = require('fs');

var advent6 = require('./advent6p2');
// var advent6 = require('./advent6');
// var advent5p2 = require('./advent5p2');

var fileContent = fs.readFileSync('./testinput.txt', { encoding: 'utf-8' });
var instructions = fileContent.split('\n');

var lightArray = [];

for (var i = 0; i < instructions.length; i++) {
  if (instructions[i] === '') { break; }
  var imperative = advent6.getImperative(instructions[i]);
  var coords = advent6.getCoords(instructions[i], imperative);
  var distances = advent6.calculateDistance(coords);
  console.log(i + ':', imperative, coords, distances, '{ changes: ' + parseInt(distances.x) * parseInt(distances.y) + ' }');
  var lightChanges = advent6.changeLights(lightArray, coords.from, distances, imperative);
  var lightChangesCoords = Object.keys(lightChanges);
  for (var j = 0; j < lightChangesCoords.length; j++) {
    if (lightArray[lightChangesCoords[j]] === undefined) {
      lightArray[lightChangesCoords[j]] = 0;
    }

    lightArray[lightChangesCoords[j]] += lightChanges[lightChangesCoords[j]];
    if (lightArray[lightChangesCoords[j]] === -1) {
      lightArray[lightChangesCoords[j]] = 0;
    }
  }
  // console.log(lightArray);
}

var lightCoords = Object.keys(lightArray);
var lightsOn = 0;
for (var i = 0; i < lightCoords.length; i++) {
  lightsOn += lightArray[lightCoords[i]];
}
console.log('Total brightness: ' + lightsOn);
