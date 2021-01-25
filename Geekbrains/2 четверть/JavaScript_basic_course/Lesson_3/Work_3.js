/*
2. С этого урока начинаем работать с функционалом интернет-магазина. Предположим, есть сущность корзины. Нужно реализовать функционал подсчета стоимости корзины в зависимости от находящихся в ней товаров. Товары в корзине хранятся в массиве. Задачи:
a) Организовать такой массив для хранения товаров в корзине;
b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины.
*/

let cart = [
    {id: 1, name: 'Груши', price: 99.90, quantity: 0.5},
    {id: 2, name: 'Сникерс', price: 48, quantity: 1},
    {id: 3, name: 'Йогурт', price: 23.90, quantity: 4},
    {id: 4, name: 'Чай липтон', price: 199.90, quantity: 1},
    {id: 5, name: 'Гранат', price: 119.90, quantity: 1.750}
]

function countBasketPrice(cart) {
    return cart.reduce((totalPrice, cartItem) => totalPrice += cartItem.price * cartItem.quantity, 0);  //0 откуда стартует новая переменная totalPrice
}


console.log(countBasketPrice(cart))
console.log(countBasketPrice(cart))