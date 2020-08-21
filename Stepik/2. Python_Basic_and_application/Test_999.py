count_space = int(input())

input_name_space = {}

for i in range(count_space):
    input_list = [n for n in input().split()]
    if len(input_list) == 1:
        """если длинна списка == 1, то создаём ключ со значением None"""
        input_name_space[input_list[0]] = [None]
    else:
        """если длинна больше 1го то создаем ключи со значением input[0]"""
        for key in range(3, len(input_list) + 1):
            '''если ключ есть в пространстве, то добавляем значение по ключу'''
            if input_list[key - 1] in input_name_space.keys():
                input_name_space[input_list[key - 1]].append(input_list[0])
            else:
                """если нет, добавляем нову пару ключ:значение"""
                input_name_space[input_list[key - 1]] = [input_list[0]]

count_answers = int(input())

for i in range(count_answers):
    input_list = [n for n in input().split()]
    print(input_list)
