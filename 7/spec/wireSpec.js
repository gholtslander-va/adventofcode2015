var Wire = require('../wire');
var bitfuncs = require('../bitfuncs');

describe('Wire', function () {
  var wires = [];

  beforeEach(function () {
    wires['x'] = 123;
    wires['y'] = 456;
  });

  it('should know it\'s port', function () {
    var mywire = new Wire(function() {}, [], 'af');
    expect(mywire.port).toBe('af');
  })

  it('should know about it\'s source', function () {
    var mywire = new Wire(function (wires) { return bitfuncs.and(wires['x'], wires['y']); }, ['x', 'y']);
    expect(mywire.sources()).toEqual(['x', 'y']);
  });

  it('should check if it\'s sources are fulfilled before running computation', function () {
    var mywire = new Wire(function () { return wires['z'] }, ['z']);
    expect(mywire.sourcesReady(wires)).toBe(false);
    wires['z'] = 1;
    expect(mywire.sourcesReady(wires)).toBe(true);
  });

  it('should compute it\'s value', function () {
    var mywire = new Wire(function (wires) { return bitfuncs.and(wires['x'], wires['y']); }, ['x', 'y']);
    expect(mywire.compute(wires)).toBe(72);
    wires['z'] = 12;
    var mywire2 = new Wire(function (wires) { return bitfuncs.or(wires['x'], wires['z']); }, ['x', 'z']);
    expect(mywire2.compute(wires)).toBe(127);
  });
});
