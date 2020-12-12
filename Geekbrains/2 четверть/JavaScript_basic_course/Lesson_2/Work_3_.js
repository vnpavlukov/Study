function aAndB(a, b) {
    if (a > 0 && b > 0) {
        return a - b
    } else if (a < 0 && b < 0) {
        console.log('hi')
        return a * b
    } else if ((a < 0 && b > -1) || (b < 0 && a > -1)) {
        return a + b
    }

}


console.log(aAndB(5, 5), 'положительные 5 5, вывести их разность');

console.log(aAndB(-5, -5), 'отрицательные -5 -5, вывести их произведение');

console.log(aAndB(5, -5), 'разных знаков -5 5, вывести их сумму');
