import re

with open('Text.txt') as file:
    text = file.read()
    r = r'\d+'
    numbers = re.findall(r, text)

print(sum([int(i) for i in numbers]))
