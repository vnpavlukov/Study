num_requests = int(input())
input_name_space = {}
for _i in range(num_requests):  # создаем новое пространство имён
    input_list = input().split()
    if len(input_list) == 1:  # if length = 1, то создаём key со значением None
        if input_list[0] in input_name_space:
            input_name_space[input_list[0]].append(None)
            # если ключ уже есть в пространстве, то добавляем None
        else:
            input_name_space[input_list[0]] = [None]
            # если ещё нет, то создаём новую пару ключ-значение
    else:
        for key in range(3, len(input_list) + 1):
            # если длинна > 1, то создаем ключи со значением input[0]
            if input_list[key - 1] in input_name_space.keys():
                input_name_space[input_list[key - 1]].append(input_list[0])
                # если ключ есть в пространстве, то добавляем значение по ключу
            else:
                input_name_space[input_list[key - 1]] = [input_list[0]]
                # если нет, добавляем нову пару ключ:значение


def is_key_value_in_name_space(name_space, keys, value_1):
    # находится ли значение в пространстве имён ключа
    # print('строка 7', 'key', key, 'value', value, )
    for one_of_key in keys:
        for key_in_space, values_in_space in name_space.items():
            # пройдем сразу по всему массиву и проверим есть ли такая пара
            if one_of_key == key_in_space and value_1 in values_in_space:
                # print('строка 11,', 'key:', key, 'value:', value,
                #       'есть такая же пара ключ значение')
                return print(value_1)  # если есть то просто возвращаем Yes
        # найдем кому вообще принадлежит это значение вверх по дереву
        # recount = 1  # необходим для подсчета итераций в тестах

        all_keys_above_value = {value_1}
        # сделаем множество и будем добавлять в него все ключи, что бы пройти
        # по всем веткам древа

        for _i in range(len(name_space)):
            for key_in_space, values_in_space in name_space.items():
                if one_of_key == key_in_space == value_1 or value_1 == values_in_space == one_of_key:
                    return print(value_1)
                elif all_keys_above_value.intersection(values_in_space):
                    all_keys_above_value.add(key_in_space)
                    if one_of_key in all_keys_above_value:
                        return print(value_1)


count_answers = int(input())
keys_list = [input()]  # все проверяемые имена будем записывать сюда как ключи
# если входное значение находится в пр.имён предыдущих, то его выводим на экран


for _i in range(count_answers - 1):
    input_check = input().split()
    if len(input_check) > 1:
        print('ERROR')
        print(is_key_value_in_name_space(
            input_name_space, input_check[0], input_check[1]))
    else:
        is_key_value_in_name_space(input_name_space, keys_list, input_check[0])
    keys_list.append(input_check[0])
