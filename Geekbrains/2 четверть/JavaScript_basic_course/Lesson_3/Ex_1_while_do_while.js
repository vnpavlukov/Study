let i = 0;
while (i < 3) {
    console.log(i);
    i++;
}


let n = 0;
do {
    console.log(n)
    n++;
} while (n < 3);


let a = 55         // лок перем
for (let a = 0; a < 1; a++) {
    console.log(a)     // 0
}
console.log(a)         // 1


var b = 55        // глоб перем
for (var b = 0; b < 1; b++) {
    console.log(b)        // 0
}
console.log(b)        // 55