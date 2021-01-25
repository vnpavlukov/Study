'use strict';

var a = 1;                      // глобальная переменная (если объявлена внутри функции, то её видно вне функции)
let b = 1;                      // локальная переменная (не видна вне функций)
let c = 'Hello world'
const d = 3;                    // локальная переменная

/*
camelCaseVariable in variable
CamelCaseClass in classes
MY_CONST in constants
*/

var a = 1;
console.log(a);              // вывод на экран

a = 5;
console.log(a);

let name = prompt('What is your name?'); // запрос данных у пользователя

function foo(prop = 0) {
    return prop + 1;
};

let name = 'Vasya';
let greeting = 'Hello ${name}';
console.log(greeting)