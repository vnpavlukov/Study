"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой."""


def user_data(**kwargs):
    answer = list()
    for key, val in kwargs.items():
        answer.append(f'{key}: {val}')
    return ', '.join(answer)


print(user_data(
    first_name='Петров', last_name='Сергей', year_birth=1945, city='Москва', email='petr@msil.ru', phone=89235678854))
