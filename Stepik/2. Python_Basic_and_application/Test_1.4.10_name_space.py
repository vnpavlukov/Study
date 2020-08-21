count = int(input())
input_name_space = {}


def is_key_value_in_name_space(in_name_space, key, value):
    """находим значение в пространстве имён по ключу"""
    # print('строка 19', value, key)
    for keys, values in in_name_space.items():
        "пройдем сразу по всему массиву и проверим есть ли такая пара"
        if key == keys and value in values:
            # print('строка 23,', key, value, 'есть такая же пара ключ значение')
            return key  # если есть то просто возвращаем ключ и победа!
    # print('строка 25, если нет такой пары ключ значение')
    'тогда ищем кому вообще принадлежит это значение вверх по дереву'
    for i in range(len(in_name_space)):
        'знаю что грабли, но не догоняю как сделать иначе'
        for keys, values in in_name_space.items():
            'ищем этот ключ в значениях'
            if key in values:
                # print('ключ есть в значениях', key, values)
                'если есть, то проверяем пространство в котором он находится'
                'есть ли в нем есть и значение значение'
                if value in values:
                    return keys
                else:
                    'если нет, проверяем пространство выше, меняем ключ на новый'
                    key = keys
    return None


for i in range(count):
    command, key, valye = input().split()
    if command == 'create':
        """ create <namespace> <valye>
        создать новое пространство имен с именем <namespace> внутри
        пространства <valye>" т.е. key и valye меняются местами """
        if valye in input_name_space.keys():
            input_name_space[valye].append(key)
        else:
            input_name_space[valye] = [key]
    elif command == 'add':
        """добавить в пространство <namespace> переменную <var>"""
        try:
            input_name_space[key].append(valye)
        except:
            input_name_space[key] = [valye]
    else:
        # print('строка 54')
        print(is_key_value_in_name_space(input_name_space, key, valye))

# print(input_name_space)