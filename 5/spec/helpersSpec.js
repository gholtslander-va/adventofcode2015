var helpers = require('../helpers');

describe('Nice string helper functions', function () {
  describe('find occurrences of a string in a string', function () {
    it('should return 3 when looking for a in aaa', function () {
      expect(helpers.findOccurrencesInString('a', 'aaa')).toBe(3);
    });

    it('should return 2 when looking for aa in aaa', function () {
      expect(helpers.findOccurrencesInString('aa', 'aaa')).toBe(2);
    });

    it('should return 1 when looking for ss in lrpprussbesniilv', function () {
      expect(helpers.findOccurrencesInString('ss', 'lrpprussbesniilv')).toBe(1);
    });
  });

  describe('find occurrences of a string in a string with no overlap', function () {
    it('should return 3 when looking for a in aaa', function () {
      expect(helpers.findOccurrencesInStringNoOverlap('aa', 'aaa')).toBe(1);
    });

    it('should return 1 when looking for ss in lrpprussbesniilv', function () {
      expect(helpers.findOccurrencesInString('ss', 'lrpprussbesniilv')).toBe(1);
    });
  });

  describe('find vowels in a string', function () {
    it('should return count of all vowels in a string', function () {
      expect(helpers.findVowelsInString('lrpprussbesniilv')).toBe(4);
    });

    it('should return 0 if no vowels found in string', function () {
      expect(helpers.findVowelsInString('lrpprssbsnlv')).toBe(0);
    });
  });

  describe('find regexes in string', function () {
    it('should find aba in abavosi', function () {
      expect(helpers.findRegexesInString([new RegExp('a.a')], 'abavosi').length).toBe(1);
    });

    it('should find sms in bivoiajsms', function () {
      expect(helpers.findRegexesInString([new RegExp('s.s')], 'bivoiajsms').length).toBe(1);
    });

    it('should find nothing in bivoiajsms', function () {
      expect(helpers.findRegexesInString([new RegExp('s.s')], 'bivoiajsms').length).toBe(1);
    });
  })

  describe('parseRegexes', function () {
    it('should return a regex for every letter in the provided string', function () {
      expect(helpers.parseRegexes('boom').length).toBe(4);
    });
  })

  describe('find list of strings in string', function () {
    it('should return the list of strings that were found', function () {
      var matches = helpers.findOccurrencesOfManyStringsInString(['a', 'b', 'c', 'd'], 'abcd');
      expect(matches.length).toBe(4);
      expect(matches).toContain('a');
    });

    it('should return an empty list if no strings matched', function () {
      var matches = helpers.findOccurrencesOfManyStringsInString(['z', 'x'], 'abcd');
      expect(matches.length).toBe(0);
    })
  });

  describe('find regex in string', function () {

  })
});
