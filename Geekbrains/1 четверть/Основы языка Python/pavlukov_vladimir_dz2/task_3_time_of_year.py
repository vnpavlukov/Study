"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

# num_input = int(input())
num_input = int('3')


def season_in_list(num):
    list_of_month = [
        {(1, 2, 12): 'зима'},
        {(3, 4, 5): 'весна'},
        {(6, 7, 8): 'лето'},
        {(9, 10, 11): 'осень'}
    ]
    for i in list_of_month:
        for key, val in i.items():
            if num in key:
                return val
    return 'число задано не верно'


def season_in_dict(num):
    dict_of_month = {
        1: 'зима', 2: 'зима', 12: 'зима',
        3: 'весна', 4: 'весна', 5: 'весна',
        6: 'лето', 7: 'лето', 8: 'лето',
        9: 'осень', 10: 'осень', 11: 'осень',
    }
    return dict_of_month.get(num, 'there is no such month')


print(season_in_list(num_input))
print(season_in_dict(num_input))

tests = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in tests:
    print(season_in_list(num_input) == season_in_dict(num_input))
