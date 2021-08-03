#!/usr/bin/node
exports.converter = function (base) {
  function toConverter (value) {
    return value.toString(base);
  }
  return toConverter;
};
