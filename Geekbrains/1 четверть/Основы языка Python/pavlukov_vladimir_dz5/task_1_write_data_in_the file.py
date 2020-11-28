"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.."""
import random

random_file_name = str(random.randint(1, 1000)) + '.txt'


def collected_data(file_name):
    file = open(file_name, 'w')
    while True:
        new_string = input()
        if not new_string:
            break
        file.writelines(new_string + '\n')
    print('your data is write into file:', file_name)
    file.close()


if __name__ == '__main__':
    collected_data(random_file_name)
