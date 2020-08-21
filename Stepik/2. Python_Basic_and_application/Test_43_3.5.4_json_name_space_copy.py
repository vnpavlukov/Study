import json

# input_set_data = json.loads(input())
input_json_data = '[' \
                  '{"name": "Anya", "parents": []}, ' \
                  '{"name": "B", "parents": ["Anya", "C"]}, ' \
                  '{"name": "C", "parents": ["Anya"]}' \
                  ']'


# input_json_data = '[' \
#                   '{"name": "beta", "parents": ["alpha", "gamma"]}, ' \
#                   '{"name": "gamma", "parents": ["alpha"]}, ' \
#                   '{"name": "alpha", "parents": []}, ' \
#                   '{"name": "delta", "parents":["gamma", "zeta"]}, ' \
#                   '{"name": "epsilon", "parents":["delta"]}, ' \
#                   '{"name": "zeta", "parents":[]}' \
#                   ']'

def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct


input_set_data = json.loads(input_json_data, object_hook=decode_complex)

for i in input_set_data:
    print()
    print(i)
    for a, b in i.items():
        print(a, b)
print()

# print(input_set_data)
name_space = {}

                # вот тут у нас кривулина сидит!!!!!!
for name_and_parent in input_set_data:  # формируем пространство имён
    if not name_and_parent['name']:  # если у name нет parent
        print("35 name_and_parent['name']:", name_and_parent['name'])
        # то name сам становится parent
        if name_and_parent['parents'] not in name_space:
            # если такого ключа ещё нет, то создаём новую пару ключ-значение
            name_space[name_and_parent['parents']] = []
    else:
        for parent in name_and_parent['name']:  # бывает что родителей много
            if parent in name_space.keys():
                # если ключ есть в пространстве, то добавляем значение по ключу
                name_space[parent].append(name_and_parent['parents'])
            else:
                # если нет, добавляем новую пару ключ:значение
                name_space[parent] = name_and_parent['parents']

print('name_space:')
print(name_space, '\n')  # проверяем name space

all_classes = []  # список всех классов в пространстве имён
for key, values in name_space.items():
    # print('51 key:', key, 'value:', values)
    for value in values:
        all_classes.append(value)

# print(all_classes)
all_classes = sorted(list(set(all_classes)))  # без дубликатов, отсортирован
# print(all_classes)


def count_parents_in_name_space(name_space, first_value):
    # сколько классов parents находится над value
    all_parents_above_value = {first_value}  # сюда запишем всех предков value
    # сделаем множество и будем добавлять в него все ключи, что бы в конце
    # вернуть количество предков value
    all_values = {first_value}  # в первом случае value один

    for _i in range(len(name_space)):  # количество запросов = количество связей
        temp_values = set()  # множество для временного хранения ключей
        for value in all_values:  # ищем отца каждого из значений
            for parent_in_space, values_in_space in name_space.items():
                if value in values_in_space:
                    # находим все value в пространствах имён и добавляем отцов
                    # в temp_values текущего value (отцов может быть несколько)
                    temp_values.add(parent_in_space)

        all_values = temp_values  # после того как нашли всех отцов
        # обновляем список all_values что бы найти их отцов
        all_parents_above_value.update(temp_values)
        # а текущих отцов вносим в общий скисок
    return len(all_parents_above_value)
    # после всех проходов возвращаем длинну списка предков класса


for my_class in all_classes:
    print(my_class, ':', count_parents_in_name_space(name_space, my_class))
