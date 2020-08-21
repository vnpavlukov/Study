# http://wombat.org.ua/AByteOfPython/modules.html
import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', '\n', sys.path, '\n')
