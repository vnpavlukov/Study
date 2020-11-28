"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
import random

file_name_task_5 = 'task_5.txt'


def data_from_txt(file_name):
    file = open(file_name, encoding="utf8")
    data = file.read()
    file.close()
    return data


def data_to_txt(file_name, data):
    file = open(file_name, 'w', encoding="utf8")
    file.write(data)
    file.close()


def random_floats_in_str():
    numbers = [str(random.uniform(0, 9, )) for _ in range(random.randint(10, 20))]
    all_numbers_in_str = ' '.join(numbers)
    return all_numbers_in_str


def sum_floats_from_str(string):
    split_numbers = string.split()
    sum_data = 0
    for num in split_numbers:
        sum_data += float(num)
    return sum_data


answer = int(input('Do you want write or read and count? (1/2): '))
if answer == 1:
    data_to_file = random_floats_in_str()
    data_to_txt(file_name_task_5, data_to_file)
else:
    try:
        data_from_file = data_from_txt(file_name_task_5)
        print(sum_floats_from_str(data_from_file))
    except FileNotFoundError:
        print('скорее всего файл ещё не создан =)')
