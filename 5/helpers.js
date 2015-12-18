function findOccurrencesInString(needle, haystack) {
  var count = 0;
  var pos = haystack.indexOf(needle);

  while (pos !== -1) {
    count++;
    pos = haystack.indexOf(needle, pos + 1);
  }

  return count;
}

function findOccurrencesInStringNoOverlap(needle, haystack) {
  var count = 0;
  var pos = haystack.indexOf(needle);

  while (pos !== -1) {
    count++;
    pos = haystack.indexOf(needle, pos + 2);
  }

  return count;
}

function findOccurrencesOfManyStringsInString(needles, haystack) {
  return needles.filter(function (needle) {
    return findOccurrencesInString(needle, haystack) > 0;
  });
}

function findRegexesInString(regexes, string) {
  return regexes.filter(function (regex) {
    return string.search(regex) >= 0;
  });
}

function findVowelsInString(haystack) {
  var vowelCount = 0;
  var vowels = ['a', 'e', 'i', 'o', 'u'];
  vowels.forEach(function(vowel) {
    vowelCount += findOccurrencesInString(vowel, haystack);
  });

  return vowelCount;
}

function parseRegexes(string) {
  return string.split('').map(function (letter) {
    return new RegExp(letter + '.' + letter);
  });
}

module.exports = {
  'findOccurrencesInString': findOccurrencesInString,
  'findOccurrencesInStringNoOverlap': findOccurrencesInStringNoOverlap,
  'findOccurrencesOfManyStringsInString': findOccurrencesOfManyStringsInString,
  'findRegexesInString': findRegexesInString,
  'findVowelsInString': findVowelsInString,
  'parseRegexes': parseRegexes
};
