var advent7 = require('../advent7');

describe('Parsing instructions', function () {
  it('should calculate operation and destination', function () {
    var instruction = advent7.parseInstruction('af AND ah -> ai');
    expect(instruction.operation).toBe('af AND ah');
    expect(instruction.destination).toBe('ai');
  });
});

describe('Parsing operations', function () {
  it('should work with NOT operations', function () {
    var instruction = advent7.parseInstruction('NOT lk -> ll');
    var operation = advent7.parseOperation(instruction.operation);
    expect(operation.operator).toBe('NOT');
    expect(operation.operands[0]).toBe('lk');
  });

  it('should work with AND operations', function () {
    var instruction = advent7.parseInstruction('af AND ah -> ai');
    var operation = advent7.parseOperation(instruction.operation);
    expect(operation.operator).toBe('AND');
    expect(operation.operands[0]).toBe('af');
    expect(operation.operands[1]).toBe('ah');
  });

  it('should work with LSHIFT operations', function () {
    var instruction = advent7.parseInstruction('af LSHIFT 2 -> ai');
    var operation = advent7.parseOperation(instruction.operation);
    expect(operation.operator).toBe('LSHIFT');
    expect(operation.operands[0]).toBe('af');
    expect(operation.operands[1]).toBe('2');
  });

  it('should work with RSHIFT operations', function () {
    var instruction = advent7.parseInstruction('af RSHIFT 2 -> ai');
    var operation = advent7.parseOperation(instruction.operation);
    expect(operation.operator).toBe('RSHIFT');
    expect(operation.operands[0]).toBe('af');
    expect(operation.operands[1]).toBe('2');
  });

  it('should work with OR operations', function () {
    var instruction = advent7.parseInstruction('af OR 2 -> ai');
    var operation = advent7.parseOperation(instruction.operation);
    expect(operation.operator).toBe('OR');
    expect(operation.operands[0]).toBe('af');
    expect(operation.operands[1]).toBe('2');
  });

  it('should work with assignment operations', function () {
    var instruction = advent7.parseInstruction('2 -> ai');
    var operation = advent7.parseOperation(instruction.operation);
    expect(operation.operator).toBe('');
    expect(operation.operands[0]).toBe('2');
    // More than one character
    var instruction = advent7.parseInstruction('14146 -> b');
    var operation = advent7.parseOperation(instruction.operation);
    expect(operation.operator).toBe('');
    expect(operation.operands[0]).toBe('14146');
  })
});
