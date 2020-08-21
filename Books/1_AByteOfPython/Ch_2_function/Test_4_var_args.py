'''
* - создаем список
** - создает кортеж
'''


def total(a=5, *numbers, **phonebook):
    print('a', a)

    # проход по всем элементам кордежа numbers
    for item in numbers:
        print('item: ', item)

    # проход по всем элементам словаря phonebook)
    for key, element in phonebook.items():
        print(key, element)


total(10, 1, 2, 3, Jack=1123, Inge=1560)
