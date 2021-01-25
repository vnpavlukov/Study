/*
2.Продолжить работу с интернет-магазином:
2.1. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими объектами можно заменить их элементы?

2.2. Реализуйте такие объекты.

2.3. Перенести функционал подсчета корзины на объектно-ориентированную базу.

*/

let cart = [
    [1, 'Груши', 99.90, 0.5],
    [2, 'Сникерс', 48, 1],
    [3, 'Йогурт', 23.90, 4],
    [4, 'Чай липтон', 199.90, 1],
    [5, 'Гранат', 119.90, 1.750],

]

function cartFunc(cart) {
    return {
        countBasketPrice() {
            return cart.reduce((totalPrice, cartItem) => totalPrice += cartItem[2] * cartItem[3], 0).toFixed(2);
        },
        countProductPositions() {
            return cart.length;
        },

        countListOfProducts() {
            const list = []
            cart.forEach((item) => {
                list.push(item[1])
            })
            return list
        }
    }


}

const new_cart = cartFunc(cart)

console.log(new_cart.countBasketPrice())
console.log(new_cart.countProductPositions())
console.log(new_cart.countListOfProducts())