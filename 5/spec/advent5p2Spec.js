var advent5p2 = require('../advent5p2');

describe('The second version of what makes a nice string', function () {
  it('should have a letter pair that repeats without overlap', function () {
    expect(advent5p2.hasRepeatingLetterPair('aabaa')).toBe(true);
    expect(advent5p2.hasRepeatingLetterPair('aaa')).toBe(false);
    expect(advent5p2.hasRepeatingLetterPair('xyxy')).toBe(true);
    expect(advent5p2.hasRepeatingLetterPair('uurcxstgmygtbstg')).toBe(true);
  });

  it('should have a letter that repeats with exactly one character between it', function () {
    expect(advent5p2.hasRepeatingLetterWithCharBetween('ana')).toBe(true);
    expect(advent5p2.hasRepeatingLetterWithCharBetween('qjhvhtzxzqqjkmpb')).toBe(true);
    expect(advent5p2.hasRepeatingLetterWithCharBetween('acb')).toBe(false);
    expect(advent5p2.hasRepeatingLetterWithCharBetween('biovjamenq')).toBe(false);
  });
});
