poem = '''\
Programming is fun!
If your work is boring
For funny tone -
using Python!
Hello world!!
'''

f = open('Test_3_poem.txt', 'w')  # открываем для записи w - writing, r - read, a - input
# )
f.write(poem)  # записываем текст в файл
f.close()  # закрываем файл

# lets check what we wrote
f = open('poem.txt')  # если не указан режим, по умолчанию подразумевается режим чтения ('r'eading)
while True:
    line = f.readline()  # read all lines
    if len(line) == 0:  # Нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='') # end - delete last line
f.close()
