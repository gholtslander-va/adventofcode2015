var helpers = require('./helpers');

function hasThreeVowels(string) {
  return helpers.findVowelsInString(string) >= 3;
}

function hasRepeatingLetter(string) {
  var repeatingLetters = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii',
                          'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr',
                          'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz'];

  return helpers.findOccurrencesOfManyStringsInString(repeatingLetters, string).length > 0;
}

function hasNaughtyStrings(string) {
  var naughtyStrings = ['ab', 'cd', 'pq', 'xy'];

  return helpers.findOccurrencesOfManyStringsInString(naughtyStrings, string).length > 0;
}

function isNice(string) {
  return hasThreeVowels(string) &&
        hasRepeatingLetter(string) &&
        !hasNaughtyStrings(string);
}

module.exports = {
  'hasThreeVowels': hasThreeVowels,
  'hasRepeatingLetter': hasRepeatingLetter,
  'hasNaughtyStrings': hasNaughtyStrings,
  'isNice': isNice
};
