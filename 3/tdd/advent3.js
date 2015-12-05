

function updateCoord(currentCoord, direction) {
  if (direction === '>') {
    // Go right
    currentCoord[0] += 1;
  } else if (direction === '^') {
    // Go up
    currentCoord[1] += 1;
  } else if (direction === 'v') {
    // Go down
    currentCoord[1] -= 1;
  } else {
    // Go left
    currentCoord[0] -= 1;
  }

  return currentCoord;
}

module.exports = {
  'updateCoord': updateCoord
}
