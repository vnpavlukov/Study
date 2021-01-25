"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

old_rating = [7, 5, 3, 3, 2]
input_number = 1


def add_number(rating, number):
    if number > rating[0]:
        rating.insert(0, number)
    elif number < rating[-1]:
        rating.append(number)
    else:
        for index in range(len(rating)):
            if number > rating[index]:
                rating.insert(index, number)
                return rating
        rating.append(number)
    return rating


print(add_number(old_rating, input_number))
