var Wire = function (computation, source, port) {
  this.computation = computation;
  this.source = source;
  this.port = port;
}

Wire.prototype.getValue = function (wires) {

}

Wire.prototype.sources = function () {
  return this.source;
}

Wire.prototype.sourcesReady = function (wires) {
  if (this.source.length === 1) {
    return parseInt(this.source[0]) !== NaN ? true : false;
  }
  for (var i = 0; i < this.source.length; i++) {
    if (wires[this.source[i]] === undefined) {
      return false;
    }
  }
  return true;
}

Wire.prototype.compute = function (wires) {
  return this.computation(wires);
}

module.exports = Wire;
