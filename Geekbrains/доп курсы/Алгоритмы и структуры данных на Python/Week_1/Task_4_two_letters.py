"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

# examples = ['a b', 'a c', 'c a', 'a a']
# for letters in examples:
#     first, second = letters.split()
#     ordinal_first = ord(first) - 96
#     ordinal_second = ord(second) - 96
#     if ordinal_first == ordinal_second:
#         print(ordinal_first, ordinal_second, 0)
#     else:
#         interval = abs(ordinal_first - ordinal_second) - 1
#         print(letters)
#         print(ordinal_first, ordinal_second, interval)


first = input('Введите первую букву латинского алфавита: ')
second = input('Введите вторую букву латинского алфавита: ')
ordinal_first = ord(first) - 96
ordinal_second = ord(second) - 96
if ordinal_first == ordinal_second:
    print(ordinal_first, ordinal_second, 0)
else:
    interval = abs(ordinal_first - ordinal_second) - 1
    print(ordinal_first, ordinal_second, interval)
