import json

input_json_data = input()


# input_json_data = '[' \
#                   '{"name": "B", "parents": ["A", "C"]},\
#                    {"name": "C", "parents": ["A"]},' \
#                   '{"name": "A", "parents": []},\
#                    {"name": "D", "parents": ["C", "F"]},\
#                    {"name": "E", "parents": ["D"]},' \
#                   '{"name": "F", "parents": []}' \
#                   ']'


def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct


input_set_data = json.loads(input_json_data, object_hook=decode_complex)

name_space = {}

for name_and_parent in input_set_data:
    if not name_and_parent['name']:
        if name_and_parent['parents'] not in name_space:
            name_space[name_and_parent['parents']] = []
    else:
        if name_and_parent['name'] in name_space.keys():
            name_space[name_and_parent['name']].append(name_and_parent['parents'])
        else:
            name_space[name_and_parent['name']] = name_and_parent['parents']

# for key, value in name_space.items():
#     print(key, value)

all_classes = []
for key, values in name_space.items():
    all_classes.append(key)
    for value in values:
        all_classes.append(value)
all_classes = sorted(list(set(all_classes)))


def count_parents_in_name_space(name_space, first_value):
    all_parents_above_value = {first_value}
    all_values = {first_value}

    for _i in range(len(name_space)):
        temp_values = set()
        for value in all_values:
            for parent_in_space, values_in_space in name_space.items():
                if value in values_in_space:
                    temp_values.add(parent_in_space)

        all_values = temp_values
        all_parents_above_value.update(temp_values)
    return len(all_parents_above_value)


for my_class in all_classes:
    print(my_class, ':', count_parents_in_name_space(name_space, my_class))
