let a = 1;


function inc(a) {
    ++a;
    console.log(a);
}

console.log(a)
inc(a)
console.log(a)


let b = {
    num: 5
};


function inc(b) {
    b.num++;
}

console.log(b)
inc(b)
console.log(b)

const obj = {
    num: 5,
};
console.log(obj?.num)
console.log(obj?.letter || 10)