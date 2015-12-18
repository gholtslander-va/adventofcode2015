var bitfuncs = require('./bitfuncs');

function parseInstruction(instruction) {
  var instructions = instruction.split(' -> ');
  return {
    operation: instructions[0],
    destination: instructions[1]
  }
}

function parseOperation(operation) {
  var splitOps = operation.split(' ');

  if (stringStartsWith(operation, 'NOT')) {
    return {
      operator: 'NOT',
      operands: [splitOps[1]]
    }
  } else if (splitOps.length === 3) {
    // AND, LSHIFT, RSHIFT, OR are possibilities now
    return {
      operator: splitOps[1],
      operands: [splitOps[0], splitOps[2]]
    }
  } else {
    // Straight up assignment?
    return {
      operator: '',
      operands: splitOps
    }
  }
}

module.exports = {
  'parseInstruction': parseInstruction,
  'parseOperation': parseOperation
}

function stringStartsWith(string, prefix) {
    return string.slice(0, prefix.length) == prefix;
}
