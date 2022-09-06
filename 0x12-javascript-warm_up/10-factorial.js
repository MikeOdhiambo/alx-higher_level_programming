#!/usr/bin/node
const val = parseInt(process.argv[2]);
function fact (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  }
  return num * fact(num - 1);
}
console.log(fact(val));
