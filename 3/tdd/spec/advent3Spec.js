advent3 = require('../advent3');

describe('Directions', function () {
  it('should increment y if direction is ^', function () {
    var coord = [0, 0];
    var newCoord = advent3.updateCoord(coord, '^');
    expect(newCoord[1]).toBe(1);
  });

  it('should decrement y if direction is v', function () {
    var coord = [0, 0];
    var newCoord = advent3.updateCoord(coord, 'v');

    expect(newCoord[1]).toBe(-1);
  });

  it('should increment x if direction is >', function () {
    var coord = [0, 0];
    var newCoord = advent3.updateCoord(coord, '>');

    expect(newCoord[0]).toBe(1);
  });

  it('should decrement x if direction is <', function () {
    var coord = [0, 0];
    var newCoord = advent3.updateCoord(coord, '<');

    expect(newCoord[0]).toBe(-1);
  });
});
