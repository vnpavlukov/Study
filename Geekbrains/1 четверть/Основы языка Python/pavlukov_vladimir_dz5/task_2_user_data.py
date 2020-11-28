"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

file_name = 'task_2.txt'

with open(file_name) as f:
    for num_of_line, line in enumerate(f):
        words = line.strip().split()
        print('words in line', num_of_line + 1, 'is:', len(words))
    print(f'\nnumber of lines in "{file_name}" file is: {num_of_line + 1}')
