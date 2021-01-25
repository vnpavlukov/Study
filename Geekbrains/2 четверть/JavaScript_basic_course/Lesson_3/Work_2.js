/*
2. С этого урока начинаем работать с функционалом интернет-магазина. Предположим, есть сущность корзины. Нужно реализовать функционал подсчета стоимости корзины в зависимости от находящихся в ней товаров. Товары в корзине хранятся в массиве. Задачи:
a) Организовать такой массив для хранения товаров в корзине;
b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины.
*/

let cart = [
    [1, 'Груши', 99.90, 0.5],
    [2, 'Сникерс', 48, 1],
    [3, 'Йогурт', 23.90, 4],
    [4, 'Чай липтон', 199.90, 1],
    [5, 'Гранат', 119.90, 1.750],

]

function countBasketPrice(cart) {
    let cartSumm = 0;

    cart.forEach((product) => {
        let price = product[2]
        let count = product[3]
        cartSumm += (price * count)
    })
    return cartSumm
}

function countBasketPrice_2(cart) {
    return cart.reduce((totalPrice, cartItem) => totalPrice += cartItem[2] * cartItem[3], 0);  //0 откуда стартует новая переменная totalPrice
}


console.log(countBasketPrice(cart))
console.log(countBasketPrice_2(cart))
