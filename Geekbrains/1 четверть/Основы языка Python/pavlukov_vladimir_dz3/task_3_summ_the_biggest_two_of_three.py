"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов."""


def season_in_list(first, second, third):
    if third <= first >= second:
        max_num = first
        if third >= second:
            middle_num = third
        else:
            middle_num = second

    elif third <= second >= first:
        max_num = second
        if first >= third:
            middle_num = first
        else:
            middle_num = third

    else:
        max_num = third
        if first >= second:
            middle_num = first
        else:
            middle_num = second

    return max_num + middle_num


print(season_in_list(1, 2, 3))
print(season_in_list(1, 3, 2))
print(season_in_list(2, 1, 3))
print(season_in_list(2, 3, 1))
print(season_in_list(3, 1, 2))
print(season_in_list(3, 2, 1))

print(season_in_list(1, 2, 2))
print(season_in_list(2, 2, 1))
print(season_in_list(2, 1, 2))

print(season_in_list(1, 1, 1))
