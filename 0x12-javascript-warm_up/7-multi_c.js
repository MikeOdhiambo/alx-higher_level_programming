#!/usr/bin/node
const reps = Number(process.argv[2]);
const line = 'C is fun';
if (Number.isInteger(reps)) {
  for (let i = 0; i < reps; i++) {
    console.log(line);
  }
} else {
  console.log('Missing number of occurrences');
}
