import json

# input_json_data = input()
input_json_data = '[' \
                  '{"name": "beta", "parents": ["alpha", "gamma"]}, ' \
                  '{"name": "gamma", "parents": ["alpha"]}, ' \
                  '{"name": "alpha", "parents": []}, ' \
                  '{"name": "delta", "parents":["gamma", "zeta"]}, ' \
                  '{"name": "epsilon", "parents":["delta"]}, ' \
                  '{"name": "zeta", "parents":[]}' \
                  ']'


def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct


input_set_data = json.loads(input_json_data, object_hook=decode_complex)

# for i in input_set_data:
#     for n in i:
#         print(n)

name_space = {}

for name_and_parent in input_set_data:  # формируем новое пространство имён
    if not name_and_parent['parents']:  # если у name нет parent,
        # то name сам становится parent
        if name_and_parent['name'] not in name_space:
            # если такого ключа ещё нет, то создаём новую пару ключ-значение
            name_space[name_and_parent['name']] = []
    else:
        # print("name_and_parent['parents']:", name_and_parent['parents'])
        for parent in name_and_parent['parents']:  # если родителей несколько
            # print('"parent:"', parent)
            if parent in name_space.keys():
                # если ключ есть в пространстве, то добавляем значение по ключу
                try:
                    name_space[parent].append(name_and_parent['name'])
                    # если попадётся дубль ключ/значение
                except:
                    continue
            else:
                # если нет, добавляем новую пару ключ:значение
                name_space[parent] = name_and_parent['name']
print(name_space)  # проверяем name space

all_classes = []  # список всех классов в пространстве имён

for key, values in name_space.items():
    all_classes.append(key)
    # print('key:', key)
    # print('value:', value)
    for value in values:
        all_classes.append(value)
all_classes = sorted(list(set(all_classes)))  # без дубликатов, отсортирован


# print(all_classes)


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
                # print('итерация №', recount)
                # recount += 1
                if one_of_key == key_in_space == value_1 or value_1 == values_in_space == one_of_key:
                    return print(value_1)
                elif all_keys_above_value.intersection(values_in_space):
                    # print('key:', keys, 'values:', values, '\n')
                    all_keys_above_value.add(key_in_space)
                    if one_of_key in all_keys_above_value:
                        return print(value_1)
        # print(all_keys_above_value)
        # print('end:', in_name_space)
        pass


keys_list = [input()]  # все проверяемые имена будем записывать сюда как ключи
# если входное значение находится в пр.имён предыдущих, то его выводим на экран


for _i in range(count_answers - 1):
    input_check = input().split()
    if len(input_check) > 1:
        print('ERROR')
        print(is_key_value_in_name_space(
            name_space, input_check[0], input_check[1]))
    else:
        is_key_value_in_name_space(name_space, keys_list, input_check[0])
    keys_list.append(input_check[0])

print('keys_list:', keys_list)
print(input_name_space)
