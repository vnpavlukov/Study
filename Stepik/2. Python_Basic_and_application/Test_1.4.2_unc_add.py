count = int(input())

namespaces = {'global': None}  # ключ - namespace.значение - parent
variables = {'global': set()}  # ключ - namespace.значение - множество переменных


def func_add(name_space, var):
    return {var: name_space}


def func_create(name_space, name_parent):
    if name_parent == 'global':
        return name_space
    return {name_parent: name_space}


def func_get(name_space, arg):
    for i in name_space.values():
        if i == arg:
            return i
        continue
    return 'None'



for i in range(count):
    cmd, namesp, arg = input().split()

    if i == 'add':
        func_add(namesp, arg)
    elif i == 'create':
        func_create(namesp, arg)
    else:
        func_get(namesp, arg)
