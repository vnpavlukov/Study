"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
import random

list_of_numbers = [random.randint(0, 500) for num in range(random.randint(10, 100))]
print(list_of_numbers)


def list_of_larger_numbers(input_list):
    new_list = list()
    for n, num in enumerate(input_list):
        if n + 1 < len(input_list):
            if input_list[n] < input_list[n + 1]:
                new_list.append(input_list[n + 1])
    return new_list


print(list_of_larger_numbers(list_of_numbers))

print('\nCheck list:')
check_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list_of_larger_numbers(check_list))
