/*
2.Продолжить работу с интернет-магазином:
2.1. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими объектами можно заменить их элементы?

2.2. Реализуйте такие объекты.

2.3. Перенести функционал подсчета корзины на объектно-ориентированную базу.
*/

const basket = {
    products: [
        [1, 'Груши', 99.90, 0.5],
        [2, 'Сникерс', 48, 1],
        [3, 'Йогурт', 23.90, 4],
        [4, 'Чай липтон', 199.90, 1],
        [5, 'Гранат', 119.90, 1.750],
    ],

    countBasketPrice() {
        return this.products.reduce((totalPrice, cartItem) => totalPrice += cartItem[2] * cartItem[3], 0).toFixed(2);
    },

    countProductPositions() {
        return this.products.length;
    },

    countListOfProducts() {
        const list = []
        this.products.forEach((item) => {
            list.push(item[1])
        })
        return list
    }
}

console.log(basket.countBasketPrice())
console.log(basket.countProductPositions())
console.log(basket.countListOfProducts())