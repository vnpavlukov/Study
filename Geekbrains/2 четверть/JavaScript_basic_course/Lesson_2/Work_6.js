/*   Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation),
где arg1, arg2 – значения аргументов, operation – строка с названием операции. В зависимости от переданного значения
операции выполнить одну из арифметических операций (использовать функции из пункта 5) и вернуть полученное значение
(использовать switch). */

function sum(a, b) {
    return a + b
}

function difference(a, b) {
    return a - b
}

function multiply(a, b) {
    return a * b
}

function divide(a, b) {
    return a / b
}

function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case 'sum':
            return sum(arg1, arg2);
        case 'difference':
            return difference(arg1, arg2);
        case 'multiply':
            return multiply(arg1, arg2);
        case 'divide':
            return divide(arg1, arg2);

    }
}

console.log(mathOperation(5, 5, 'sum'));
console.log(mathOperation(5, 5, 'difference'));
console.log(mathOperation(5, 5, 'multiply'));
console.log(mathOperation(5, 5, 'divide'));
