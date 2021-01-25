/* 1. Написать функцию, преобразующую число в объект. Передавая на вход число от 0 до 999, мы должны получить
на выходе объект, в котором в соответствующих свойствах описаны единицы, десятки и сотни. Например, для числа 245
мы должны получить следующий объект: {‘единицы’: 5, ‘десятки’: 4, ‘сотни’: 2}. Если число превышает 999, необходимо
выдать соответствующее сообщение с помощью console.log и вернуть пустой объект.
*/


function primeNumber(n) {
    if (n > 999 || n < 0) {
        console.log('Enter number from 0 to 999');
        return undefined;
    }

    const hundreds = parseInt(n / 100 % 10);
    const tens = parseInt(n / 10 % 10);
    const units = n % 10;

    return {'единицы': units, 'десятки': tens, 'сотни': hundreds}
}


const tests = [-1, 1000, 5, 56, 347]

for (const test of tests) {
    console.log(primeNumber(test), '\n');
}