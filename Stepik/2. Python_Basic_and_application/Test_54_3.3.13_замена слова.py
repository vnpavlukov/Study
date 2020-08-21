# https://stepik.org/lesson/24470/step/13?unit=6776
import sys
import re

# for text in sys.stdin:
#     line = text.rstrip()
#     pattern = r'a+a'  # разделим все слова по пробелу
#     if re.search(pattern, line, re.IGNORECASE):
#         new_pattern = re.search(pattern, line, re.IGNORECASE).group(0)
#         new = 'argh'
#         print(re.sub(new_pattern, new, line, count=1))

text = ['There’ll be no more "Aaaaaaaaaaaaaaa"',
        'aAb AaAaAaA']

for line in text:
    pattern = r'\ba+a\b'  # разделим все слова по пробелу
    if re.search(pattern, line, re.IGNORECASE):
        new_pattern = re.search(pattern, line, re.IGNORECASE).group(0)
        new = r'arg'
        print(re.sub(new_pattern, new, line, count=1, flags=0))

