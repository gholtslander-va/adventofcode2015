var advent5 = require('../advent5');

describe('Nice string', function () {
  describe('has three vowels', function () {
    it('should return true for a string with three vowels', function () {
      expect(advent5.hasThreeVowels('aaa')).toBe(true);
    });

    it('should return false for a string with zero to two vowels', function () {
      expect(advent5.hasThreeVowels('aa')).toBe(false);
      expect(advent5.hasThreeVowels('a')).toBe(false);
      expect(advent5.hasThreeVowels('bcd')).toBe(false);
    });
  });

  describe('has at least one repeating letter', function () {
    it('should return true for a string with repeating letters', function () {
      expect(advent5.hasRepeatingLetter('aaosijvoaim')).toBe(true);
    });

    it('should return false for a string with no repeating letters', function () {
      expect(advent5.hasRepeatingLetter('abcdefghijk')).toBe(false);
    })
  });

  describe('does not contain any naughty strings', function () {
    it('should return false if a string has no naughty strings within it', function () {
      expect(advent5.hasNaughtyStrings('aaaaaa')).toBe(false);
    });

    it('should return true if a string has naughty strings within it', function () {
      expect(advent5.hasNaughtyStrings('abcdefghijk')).toBe(true);
    });
  });

  it('should find not-nice strings', function () {
    expect(advent5.isNice('jchzalrnumimnmhp')).toBe(false);
    expect(advent5.isNice('haegwjzuvuyypxyu')).toBe(false);
    expect(advent5.isNice('dvszwmarrgswjxmb')).toBe(false);
  });

  it('should find aaa to be a nice string', function () {
    expect(advent5.isNice('aaa')).toBe(true);
  });
});
