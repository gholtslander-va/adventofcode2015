var helpers = require('./helpers');

function hasRepeatingLetterPair(string) {
  for(var i = 0; i < string.length; i++) {
    if (helpers.findOccurrencesInStringNoOverlap(string[i] + string[i+1], string) >= 2) {
      return true;
    }
  }
  return false;
}

function hasRepeatingLetterWithCharBetween(string) {
  return helpers.findRegexesInString(helpers.parseRegexes(string), string).length > 0;
}

function isNice(string) {
  return hasRepeatingLetterPair(string) && hasRepeatingLetterWithCharBetween(string);
}

module.exports = {
  'hasRepeatingLetterWithCharBetween': hasRepeatingLetterWithCharBetween,
  'hasRepeatingLetterPair': hasRepeatingLetterPair,
  'isNice': isNice
};
