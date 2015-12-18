function calculateDistance(coords) {
  var realFrom = coords.from.split(',').map((item) => parseInt(item));
  var realTo = coords.to.split(',').map((item) => parseInt(item));
  return {
    x: realTo[0] - realFrom[0],
    y: realTo[1] - realFrom[1]
  }
}

function changeLights(lights, from, distances, imperative) {
  var intFrom = from.split(',').map((item) => parseInt(item));
  var startingX = intFrom[0];
  var startingY = intFrom[1];
  var coords = [];
  var status = imperative === 'turn on' ? 'on' : imperative === 'turn off' ? 'off' : 'toggle';

  for (var i = startingX; i <= startingX + distances.x; i++) {
    for (var j = startingY; j <= startingY + distances.y; j++) {
      var coord = i + ',' + j;
      coords[coord] = status !== 'toggle' ? status : toggle(lights[coord]);
    }
  }
  return coords;
}

function getCoords(instruction, imperative) {
  var coordinates = instruction.substring(imperative.length);
  coordinates = coordinates.split(' through ');
  return {
    from: coordinates[0].trim(),
    to: coordinates[1].trim()
  }
}

function getImperative(instruction) {
  if (stringStartsWith(instruction, 'turn on')) {
    return 'turn on';
  } else if (stringStartsWith(instruction, 'turn off')) {
    return 'turn off';
  } else {
    return 'toggle';
  }
}

function toggle(lightStatus, coordString) {
  return lightStatus === 'on' ? 'off' : 'on';
}

module.exports = {
  'calculateDistance': calculateDistance,
  'changeLights': changeLights,
  'getCoords': getCoords,
  'getImperative': getImperative,
  'toggle': toggle
};

function stringStartsWith(string, prefix) {
    return string.slice(0, prefix.length) == prefix;
}
