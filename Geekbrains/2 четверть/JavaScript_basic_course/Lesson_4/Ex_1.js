var car = {
    brand: 'Toyota',
    'number of doors': 5
}

// console.log(car)
// console.log(car.brand)
// console.log(car['number of doors'])
// console.log(car['brand'])

// console.log(Object.keys(car))
// console.log(Object.getOwnPropertyNames(car))

for (const prop in car) {
    console.log(prop)
}