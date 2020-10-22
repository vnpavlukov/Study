"""
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

# numbers = [1, 2, 3, 26]
# for number in numbers:
#     print(chr(number + 96))

input_number = int(input('Введите порядковый номер буквы латинского алфавита: '))
letter = chr(input_number + 96)
print("Это буква: ", letter)
