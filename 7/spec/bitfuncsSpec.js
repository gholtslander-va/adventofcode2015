var bitfuncs = require('../bitfuncs');
describe('Bitwise operation wrappers', function () {
  it('should be able to AND two vars', function () {
    expect(bitfuncs.and(1, 2)).toBe(0);
  });

  it('should be able to OR two vars', function () {
    expect(bitfuncs.or(1, 2)).toBe(3);
  });

  it('should be able to left shift a variable', function () {
    expect(bitfuncs.lshift(10, 1)).toBe(20);
    expect(bitfuncs.lshift(10, 3)).toBe(80);
  });

  it('should be able to right shift a variable', function () {
    expect(bitfuncs.rshift(10, 1)).toBe(5);
    expect(bitfuncs.rshift(10, 3)).toBe(1);
  });

  it('should be able to NOT a variable', function () {
    expect(bitfuncs.not(3)).toBe(-4);
  })
});
