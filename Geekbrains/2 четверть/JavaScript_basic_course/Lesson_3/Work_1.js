//1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.


function primeNumber(n) {
    if (n === 1 || n === 1) return true;

    let i = 2;

    while (i < n) {
        if (n % i === 0) {
            return false
        }
        i++;
    }
    return true;
}

function consoleLogPrimeNumber(x) {
    let i = 1;

    while (i <= x) {
        if (primeNumber(i)) console.log(i);
        i++;
    }
}

consoleLogPrimeNumber(100)