#!/usr/bin/node

const myVar = 'C is fun';

for (let i = 0; i < process.argv[2]; i++) {
  console.log(myVar);
}
