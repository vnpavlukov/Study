new_file = open('Test_2.4.1_read_from_file_2.txt', 'r')

for line in new_file:  # считываем файл построчно что бы не перегрузить память
    print(line.rstrip())  # repr - игнорирование технических символов
    # .rstrip() - убирает технические символы справа от строки

new_file.close()
