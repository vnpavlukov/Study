count = int(input())

data_all_users = []


def add_new_user(user_name, f_users):
    """создание пользователя с именем user_name в пространстве имём users"""
    f_users.append(user_name)
    return data_all_users


def func_add(name_space, var):
    return {var: name_space}


def func_create(name_space, name_parent):
    if name_parent == 'global':
        return name_space
    a = {name_parent: name_space}
    return a


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
