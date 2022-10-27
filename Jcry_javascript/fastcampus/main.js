import getType from './getType'

// console.log(typeof 'Hello world!');
// console.log(typeof 123);
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof {});
console.log(typeof []);

function getType(data){
    return Object.prototype.toString.call(data)
}

console.log(getType(123))