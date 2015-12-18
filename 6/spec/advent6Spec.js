var advent6 = require('../advent6');

describe('Toggling a light', function () {
  it('should turn a light on if it does not exist', function () {
    var lights = new Map();
    lights['1,1'] = advent6.toggle(lights['1,1']);
    expect(lights['1,1']).toBe('on');
  });

  it('should turn a light on if it is off', function () {
    var lights = new Map();
    lights['1,1'] = 'off';
    lights['1,1'] = advent6.toggle(lights['1,1']);
    expect(lights['1,1']).toBe('on');
  })

  it('should turn a light off if it is on', function () {
    var lights = new Map();
    lights['1,1'] = 'on';
    lights['1,1'] = advent6.toggle(lights['1,1']);
    expect(lights['1,1']).toBe('off');
  })
});

describe('Parse lighting instructions', function () {
  it('should get the imperative for the task', function () {
    var instruction = 'turn off 150,300 through 213,740';
    var imperative = advent6.getImperative(instruction);
    expect(imperative).toBe('turn off');
    var instruction = 'turn on 150,300 through 213,740';
    var imperative = advent6.getImperative(instruction);
    expect(imperative).toBe('turn on');
    var instruction = 'toggle 150,300 through 213,740';
    var imperative = advent6.getImperative(instruction);
    expect(imperative).toBe('toggle');
  });

  it('should parse coordinates to calculate on', function () {
    var instruction = 'turn off 150,300 through 213,740';
    var coords = advent6.getCoords(instruction, advent6.getImperative(instruction));
    expect(coords.from).toBe('150,300');
    expect(coords.to).toBe('213,740');
  });

  it('should calculate the distance between points', function () {
    var distance = advent6.calculateDistance({from: '150,300', to: '213,740'});
    expect(distance.x).toBe(63);
    expect(distance.y).toBe(440);
  });
});

describe('Change lights', function () {
  it('should change lights as instructed by the imperative', function () {
    
  });
});
