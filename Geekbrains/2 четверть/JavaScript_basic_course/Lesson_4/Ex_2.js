var car = {
    brand: 'Toyota',
    'number of doors': 5,
    [Symbol.iterator]: function* () {
        yield 'hi';
        yield 'hello';
    }
}


for (const prop in car) {
    console.log(prop)
}

for (const prop of car) {
    console.log(prop)
}