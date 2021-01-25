function a() {
    return {
        number: 5,
        sayNumber() {
            console.log(this.number)
        }
    }
}

const b = a()
console.log(b)
console.log(b.sayNumber())