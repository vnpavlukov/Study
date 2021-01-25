let a = 10 / 0;
console.log(a);

let b = '3.14';
console.log(typeof b);
console.log();

b = 2 + b;
console.log(b);

b = b + 2;
console.log(b);  // полная вакханалия!


console.log(parseInt(b));  // преобразование в инт
console.log(parseFloat(b));  // преобразование в флоат
console.log(Number(b));  // преобразование в число
console.log();

console.log(2e3);
console.log();

let new_dict = {
    name: 'Vova',
    age: 31,
};
console.log(new_dict.name);
console.log(new_dict['name']);
let select = 'name';
console.log(new_dict[select]);

