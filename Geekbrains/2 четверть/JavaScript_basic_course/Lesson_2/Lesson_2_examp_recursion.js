function recursion(x) {
    if (x <= 0 || !Number.isInteger(x)) return 'Задайте целое число больше 0';

    if (x === 1) return 1;

    return recursion(x - 1) + ' ' + x;

}


console.log(recursion(10));