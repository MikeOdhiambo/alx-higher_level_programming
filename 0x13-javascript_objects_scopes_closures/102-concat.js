#!/usr/bin/node
const fs = require('fs');
const mrgd = process.argv[4];
const cntA = fs.readFileSync(process.argv[2], 'utf8');
const cntB = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(mrgd, cntA + cntB);
