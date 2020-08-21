# https://stepik.org/lesson/24470/step/11?unit=6776
import sys
import re

# for text in sys.stdin:
#     line = text.rstrip()
#     pattern = r'\w+'  # разделим все слова по пробелу
#     words = re.findall(pattern, line)  # список из слов в строке
#     for word in words:
#         if len(word) % 2 == 0:
#             half = int(len(word) / 2)
#             if word[:half] == word[half:]:
#                 print(line)

text = ['blabla is a tandem repetition',
        '123123 is good too',
        'go go',
        'aaa']

for line in text:
    pattern = r'\w+'  # разделим все слова по пробелу
    words = re.findall(pattern, line)  # список из слов в строке
    for word in words:
        if len(word) % 2 == 0:
            half = int(len(word) / 2)
            if word[:half] == word[half:]:
                print(line)
