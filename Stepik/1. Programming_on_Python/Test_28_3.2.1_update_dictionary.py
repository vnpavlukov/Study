x = {}


def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key * 2 in d:
        d[key].append(value)
    else:
        d[key * 2] = [value]


print(update_dictionary(x, 1, -1))
print(x)  # {2: [-1]}

update_dictionary(x, 2, -2)
print(x)  # {2: [-1, -2]}

update_dictionary(x, 1, -3)
print(x)  # {2: [-1, -2, -3]}

update_dictionary(x, 3, -3)
print(x)  # {2: [-1, -2, -3]. 6: [-3]}