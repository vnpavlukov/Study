"""2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
в формате чч:мм:сс. Используйте форматирование строк."""

# seconds_input = int(input())
seconds_input = int('3666')


def print_user_time(time_in_seconds):
    seconds = time_in_seconds % 60
    minutes = time_in_seconds // 60 % 60
    hours = time_in_seconds // 3600 % 24
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")


print_user_time(seconds_input)

print('tests:')
seconds_list = ['1', '60', '61', '3600', '3661', '366661234']
for seconds_input in seconds_list:
    print_user_time(int(seconds_input))
