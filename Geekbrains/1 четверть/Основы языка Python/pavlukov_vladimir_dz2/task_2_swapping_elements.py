"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input()."""


def swap_elements(elements):
    for i in range(0, len(elements) - 1, 2):
        elements[i], elements[i + 1] = elements[i + 1], elements[i]
    return elements


# input_data = input().split()
# print(swap_elements(input_data))

first_data = [1, 2, 3, 4], [1, 2, 3, 4, 5]

for data in first_data:
    print(swap_elements(data))
