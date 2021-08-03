#!/usr/bin/node
// Loop forEach for arrays (loop )
exports.nbOccurences = function (list, searchElement) {
  let occurr = 0;
  list.forEach(index => {
    if (index === searchElement) {
      occurr += 1;
    }
  });
  return occurr;
};
