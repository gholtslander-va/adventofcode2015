// Bit functions
function and(op1, op2) {
  return parseInt(op1) & parseInt(op2);
}

function lshift(op1, bitsToShift) {
  return parseInt(op1) << parseInt(bitsToShift);
}

function not(op1) {
  return ~ parseInt(op1);
}

function or(op1, op2) {
  return parseInt(op1) | parseInt(op2);
}

function rshift(op1, bitsToShift) {
  return parseInt(op1) >> parseInt(bitsToShift);
}

module.exports = {
  'and': and,
  'lshift': lshift,
  'not': not,
  'or': or,
  'rshift': rshift
};
