request = 'acce'

l_list = list(request)
l_len = len(request)

index = 0
count = 1

if l_len == 1:  # проверяем если символ один
    print(request, 1, sep="")
else:
    while index < l_len:
        if l_list[index] != l_list[index + 1]:  # проверка если первый символ в одном экземпляре
            n = 1
            print(l_list[index], n, sep="", end="")
            index += 1

        if l_list[index] == l_list[index + 1]:  # алгоритм для подсчета последующих символов
            n = 1
            while l_list[index] == l_list[index + 1]:  # подсчитываем повторяющиеся символы
                index += 1
                n += 1  # посчитали
                # print(l_list[index], n, sep="", end="")
            print(l_list[index], n, sep="", end="")  # записали
            index += 1

            print('\n', index)
            print(l_len)